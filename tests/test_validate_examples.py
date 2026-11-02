"""Regression checks for schema validation and missing dependencies.

Run with: python3 -m unittest discover -s tests -v
Fixtures are temporary copies; published examples and schemas stay unchanged.
"""

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ExampleValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ("scripts", "examples", "schema"):
            shutil.copytree(ROOT / folder, self.root / folder)
        self.example = self.root / "examples" / "uid_auth_example.json"
        self.original = json.loads(self.example.read_text(encoding="utf-8"))

    def run_validator(self, without_dependencies=False):
        options = ["-I", "-S"] if without_dependencies else []
        return subprocess.run(
            [sys.executable, *options, str(self.root / "scripts/validate_examples.py")],
            cwd=self.root, capture_output=True, text=True, timeout=30,
        )

    def write_example(self, data):
        self.example.write_text(json.dumps(data), encoding="utf-8")

    def test_published_examples(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertEqual(sum(line.startswith("OK ") for line in result.stdout.splitlines()), 3)
        self.assertIn("jsonschema (schema-driven)", result.stdout)

    def test_invalid_declarations_are_rejected(self):
        # These wrong types were accepted or caused TypeError in the former
        # reduced validator. Each must now produce a controlled schema failure.
        mutations = [
            (("creator",), 17),
            (("name",), 17),
            (("uid_auth",), 17),
            (("issuer", "name"), 17),
            (("hash", "value"), 17),
            (("rights", "tdm_opt_out"), 1),
        ]
        for field, value in mutations:
            with self.subTest(field=field):
                data = copy.deepcopy(self.original)
                target = data
                for segment in field[:-1]:
                    target = target[segment]
                target[field[-1]] = value
                self.write_example(data)
                result = self.run_validator()
                self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
                self.assertIn("INVALID examples/" + self.example.name, result.stdout)
                self.assertNotIn("Traceback", result.stderr)
        data = copy.deepcopy(self.original)
        del data["uid_auth"]
        self.write_example(data)
        result = self.run_validator()
        self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
        self.assertIn("required property", result.stdout)

    def test_format_annotations_remain_annotations(self):
        data = copy.deepcopy(self.original)
        data["issued_at"] = "not-a-date"
        self.write_example(data)
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_missing_dependency_does_not_validate(self):
        result = self.run_validator(without_dependencies=True)
        self.assertEqual(result.returncode, 2, result.stderr + result.stdout)
        self.assertIn("Schema validation unavailable", result.stderr)
        self.assertIn("python3 -m pip install", result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
