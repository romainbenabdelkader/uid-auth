#!/usr/bin/env python3
"""Validate the example manifests against the UID_AUTH JSON Schema.

The JSON Schema (schema/uid_auth_schema.json) is the source of truth. When the
optional `jsonschema` library is available the examples are validated directly
against it, so the schema and the examples can never silently drift apart. If
`jsonschema` is not installed the script falls back to an equivalent built-in
check that uses only the Python standard library, so it still runs anywhere.

Install the schema validator with:  pip install jsonschema
"""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "uid_auth_schema.json"
EXAMPLES = [
    ROOT / "examples" / "uid_auth_example.json",
    ROOT / "examples" / "manifest_example.jsonld",
    ROOT / "examples" / "manifest_us_example.jsonld",
]

UID_RE = re.compile(r"^[A-Z]{2}-[0-9]{4}-AUTH-[A-Z]{3}-[0-9]{6}$")
HASH_RE = re.compile(r"^[a-fA-F0-9]{64}$")


def load_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def builtin_validate(data, path):
    """Standard-library fallback mirroring the JSON Schema constraints."""
    require(UID_RE.match(data.get("uid_auth", "")), f"{path}: invalid uid_auth")
    require(data.get("spec_version") == "1.0", f"{path}: invalid spec_version")
    require(data.get("origin") in {"human", "ai", "hybrid"}, f"{path}: invalid origin")
    require(isinstance(data.get("issued_at"), str), f"{path}: missing issued_at")

    issuer = data.get("issuer")
    require(isinstance(issuer, dict), f"{path}: issuer must be an object")
    require(issuer.get("name"), f"{path}: missing issuer.name")
    require(
        issuer.get("type")
        in {"IdentityAuthority", "CollectingSociety", "Label", "TrustedEntity"},
        f"{path}: invalid issuer.type",
    )

    rights = data.get("rights")
    require(isinstance(rights, dict), f"{path}: rights must be an object")
    require(
        rights.get("ai_training")
        in {"prohibited", "allowed", "restricted", "conditional"},
        f"{path}: invalid rights.ai_training",
    )
    require(isinstance(rights.get("tdm_opt_out"), bool), f"{path}: invalid tdm_opt_out")

    digest = data.get("hash")
    require(isinstance(digest, dict), f"{path}: hash must be an object")
    require(digest.get("algorithm") == "sha256", f"{path}: invalid hash.algorithm")
    require(HASH_RE.match(digest.get("value", "")), f"{path}: invalid hash.value")


def main():
    schema = load_json(SCHEMA_PATH)

    try:
        from jsonschema import Draft202012Validator

        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        mode = "jsonschema (schema-driven)"
    except ModuleNotFoundError:
        validator = None
        mode = "built-in fallback (install jsonschema for schema-driven checks)"

    failures = 0
    for example in EXAMPLES:
        data = load_json(example)
        rel = example.relative_to(ROOT)
        try:
            if validator is not None:
                errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
                if errors:
                    raise AssertionError(
                        "; ".join(f"{list(e.path)}: {e.message}" for e in errors)
                    )
            else:
                builtin_validate(data, rel)
        except AssertionError as exc:
            failures += 1
            print(f"INVALID {rel}\n  - {exc}")
            continue
        print(f"OK {rel}")

    print(f"[validated with: {mode}]")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
