#!/usr/bin/env python3
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UID_RE = re.compile(r"^[A-Z]{2}-[0-9]{4}-AUTH-[A-Z]{3}-[0-9]{6}$")
HASH_RE = re.compile(r"^[a-fA-F0-9]{64}$")


def load_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def validate_manifest(path):
    data = load_json(path)

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
    examples = [
        ROOT / "examples" / "uid_auth_example.json",
        ROOT / "examples" / "manifest_example.jsonld",
        ROOT / "examples" / "manifest_us_example.jsonld",
    ]

    for example in examples:
        validate_manifest(example)
        print(f"OK {example.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
