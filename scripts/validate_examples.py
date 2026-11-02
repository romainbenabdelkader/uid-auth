#!/usr/bin/env python3
"""Validate the example manifests against the UID_AUTH JSON Schema.

The JSON Schema (schema/uid_auth_schema.json) is the source of truth. The jsonschema
library is required; if it cannot be imported, validation stops with exit code 2.
No reduced validation mode is used. Date and URI formats remain annotations.
This script does not verify asset hashes, signatures or issuer authority.

Install the schema validator with: python3 -m pip install 'jsonschema>=4,<5'
"""

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "uid_auth_schema.json"
EXAMPLES = [
    ROOT / "examples" / "uid_auth_example.json",
    ROOT / "examples" / "manifest_example.jsonld",
    ROOT / "examples" / "manifest_us_example.jsonld",
]

def load_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        print(
            "Schema validation unavailable: jsonschema and its dependencies are required. "
            "Install with: python3 -m pip install 'jsonschema>=4,<5'",
            file=sys.stderr,
        )
        return 2

    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    failures = 0
    for example in EXAMPLES:
        data = load_json(example)
        rel = example.relative_to(ROOT)
        errors = sorted(validator.iter_errors(data), key=lambda e: str(list(e.path)))
        if errors:
            failures += 1
            print(f"INVALID {rel}")
            for error in errors:
                print(f"  - {list(error.path)}: {error.message}")
        else:
            print(f"OK {rel}")

    print("[validated with: jsonschema (schema-driven)]")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
