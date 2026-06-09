# UID_AUTH

Open standard for creative work identification, origin declaration and traceability.

UID_AUTH defines a sovereign, verifiable and interoperable identifier for creative works. It provides a minimal layer for linking a work to an origin declaration, timestamp, integrity hash and machine-readable rights signals.

> UID_AUTH identifies and structures a declaration. It does not decide legal ownership, infringement or liability.

## Purpose

UID_AUTH provides three technical guarantees:

- declarative proof of origin
- cryptographic integrity through `sha256`
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

UID_AUTH does not replace ISRC, ISWC, UPC, EAN, DDEX or EIDR. It adds an identification, origin and integrity layer.

## JSON Manifest

Minimal example:

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

It checks:

- `uid_auth` format
- declared origin: `human`, `ai`, `hybrid`
- ISO 8601 timestamp
- issuing authority
- AI/TDM rights
- `sha256` hash

## Local Validation

Run the minimal example validator:

```bash
python scripts/validate_examples.py
```

or:

```bash
python3 scripts/validate_examples.py
```

This does not replace a full JSON Schema validator. It keeps repository examples aligned with UID_AUTH v1.0.

## Interoperability

UID_AUTH coexists with existing identifiers:

- ISRC
- ISWC
- UPC / EAN
- DDEX
- EIDR

It complements them with:

- an origin identifier
- integrity proof
- AI/TDM transparency signals

## Relationship With AURA

UID_AUTH can be used as a work identifier inside an AURA manifest, but remains independent.

Example:

```json
{
  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "aura_id": "AURA-LOCAL-2026-000001-TEST",
  "asset_hash": "..."
}
```

In this model:

- `uid_auth` identifies the work
- `aura_id` identifies the AURA proof
- `asset_hash` verifies file integrity
- the AURA signature verifies manifest integrity

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
