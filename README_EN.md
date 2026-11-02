# UID_AUTH

Open format for creative work identification and declarations.

UID_AUTH defines an identifier format with accompanying metadata: declared
origin, declared date, digest and machine-readable rights signals. The schema
checks structure; the identifier alone does not certify origin, the declarant's
identity or file integrity.

[Documentation en francais](README.md) · [U.S. profile](README.US.md)

> UID_AUTH identifies and structures a declaration. It does not decide legal ownership, infringement or liability.

## Purpose

UID_AUTH structures three kinds of information:

- an origin declaration
- a declared `sha256` digest, to compare separately with asset bytes
- AI and TDM opt-out transparency signals

The standard can be used by:

- collective management organizations
- cultural institutions
- DSPs and distribution platforms
- AI platforms
- publishers, producers and labels
- independent creators

## Official Format

UID_AUTH v1.0 format:

```text
COUNTRY-YEAR-AUTH-CATEGORY-SEQUENCE
```

Example:

```text
FR-2025-AUTH-MUS-000001
```

Segments:

| Segment | Description |
| --- | --- |
| `COUNTRY` | ISO alpha-2 country code, e.g. `FR`, `US`, `CA` |
| `YEAR` | Declaration year |
| `AUTH` | Fixed standard prefix |
| `CATEGORY` | Creative category, e.g. `MUS`, `VID`, `IMG`, `TXT` |
| `SEQUENCE` | Six-digit numeric sequence |

UID_AUTH does not replace ISRC, ISWC, UPC, EAN or EIDR identifiers, or DDEX
exchange formats. Identifier shape does not establish global uniqueness:
implementations must separately organize sequence allocation and collision
prevention. The schema checks segment shape, not actual country-code or
category allocation.

## JSON Manifest

Minimal example:

The examples are fictional. The `e3b0c442...b855` digest below and in the three
example files is SHA-256 of an empty byte sequence, not evidence of an audio
file's integrity. No audio asset or signature accompanies these examples.

```json
{
  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "spec_version": "1.0",
  "issued_at": "2025-11-11T10:30:00Z",
  "media_type": "audio/wav",
  "name": "Example Audio Work",
  "creator": "Anonymous",
  "origin": "human",
  "rights": {
    "ai_training": "prohibited",
    "tdm_opt_out": true,
    "jurisdiction": "EU"
  },
  "hash": {
    "algorithm": "sha256",
    "value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}
```

Reference file:

```text
examples/uid_auth_example.json
```

## JSON-LD Manifest

A JSON-LD manifest can add machine-readable context for AI and TDM rights.

Reference file:

```text
examples/manifest_example.jsonld
```

JSON-LD context:

```text
context/schema/ai-rights-context.jsonld
```

## Schema

The official JSON Schema is available at:

```text
schema/uid_auth_schema.json
```

It imposes structural constraints on:

- `uid_auth` format
- declared origin: `human`, `ai`, `hybrid`
- the declared `issued_at` date field
- declared issuer fields
- AI/TDM rights
- the `sha256` algorithm and hexadecimal digest shape

## Local Validation

Run the minimal example validator:

```bash
python scripts/validate_examples.py
```

or:

```bash
python3 scripts/validate_examples.py
```

With the optional `jsonschema` library (`pip install jsonschema`), the script
uses `schema/uid_auth_schema.json` without enabling date and URI format checks.
Otherwise it uses minimal standard-library checks. Neither path recomputes an
asset digest, verifies a signature or authenticates issuer authority.

## Interoperability

Integrations may reference existing identifiers or formats:

- ISRC
- ISWC
- UPC / EAN
- DDEX
- EIDR

The profile adds structured declarations:

- a declared work identifier
- a declared asset digest
- AI/TDM transparency signals

Coexistence does not establish a DDEX exchange, C2PA integration or lossless
conversion. Mappings need specified rules and tests. See the
[format boundaries and versions](ARCHITECTURE.md).

## Architecture

The roles are separate:

- AURA defines signed declarations and exact-byte asset-integrity evidence. Its required identifier is `aura_uid`; UID_AUTH and institutional identifiers remain optional in its core.
- UID_AUTH defines the declared work identifier format and metadata published here.
- AUTHENTICA AI Rights publishes a separate JSON-LD profile whose schema requires `uid_auth`. A document conforming to that profile is not automatically a signed AURA manifest.

An AURA extension can carry a UID_AUTH identifier without making it mandatory
in the AURA core. The integration must document its extension path and meaning;
the AURA verifier does not certify those semantics.

Keep the identified objects distinct:

| Element | Scope |
| --- | --- |
| `uid_auth` | Declared work identifier in this profile |
| `aura_uid` | Required identifier of an AURA 1.0/1.1 declaration |
| `asset.hash` | Digest of the asset bytes in an AURA manifest |
| AURA signature | Binding between the signed declaration and a public key |

The AURA `aura_id` field is optional and does not replace `aura_uid`. A valid
signature does not establish the truth of the declared information.

## Non-Goals

UID_AUTH does not provide:

- absolute legal proof of ownership
- automated infringement decisions
- usage monitoring
- automatic sanctions
- DRM
- watermarking
- content recognition

UID_AUTH provides a verifiable technical artefact. Legal qualification belongs to law, audit, regulators or competent courts.

## Status

UID_AUTH v1.0 is published as a minimal open standard. Reference implementations may evolve separately.

## License

Apache License 2.0
