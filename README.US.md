# UID_AUTH - U.S. Profile

UID_AUTH can be used as a voluntary provenance and AI-rights manifest profile for creative works in the United States.

It is designed for creators, publishers, labels, CMOs, DSPs and AI providers who need a machine-readable declaration for:

- origin
- integrity
- AI-training rights
- TDM or scraping opt-out signals
- interoperability with existing identifiers

> UID_AUTH provides a verifiable technical artefact. It does not decide legal ownership, fair use, infringement or liability.

## U.S. Identifier Example

```text
US-2025-AUTH-MUS-000001
```

This follows the UID_AUTH v1.0 format:

```text
COUNTRY.YEAR.AUTH.CATEGORY.SEQUENCE
```

## U.S. JSON-LD Example

```json
{
  "@context": "https://raw.githubusercontent.com/romainbenabdelkader/uid-auth/main/context/schema/ai-rights-context.jsonld",
  "@type": "CreativeWork",
  "uid_auth": "US-2025-AUTH-MUS-000001",
  "spec_version": "1.0",
  "media_type": "audio/wav",
  "name": "Example Song",
  "creator": "Anonymous",
  "origin": "human",
  "issued_at": "2025-01-17T12:34:56Z",
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  },
  "rights": {
    "ai_training": "prohibited",
    "training_conditions": "https://example.com/terms/ai-training",
    "jurisdiction": "US",
    "tdm_opt_out": true
  },
  "hash": {
    "algorithm": "sha256",
    "value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  }
}
```

Reference file:

```text
examples/manifest_us_example.jsonld
```

## Relationship With U.S. Law

UID_AUTH may support documentation and audit workflows around:

- authorship declarations
- creation or declaration dates
- provenance metadata
- AI-training opt-out declarations
- rights-management metadata

It does not replace legal analysis under U.S. copyright law, DMCA, fair use doctrine, contracts, audits, regulators or courts.

## Interoperability

UID_AUTH can coexist with:

- ISRC
- ISWC
- ISNI
- ASCAP / BMI / SESAC / MLC workflows
- DDEX
- C2PA / Content Credentials
- platform rights-management systems

## Privacy And Personal Data

UID_AUTH is designed around data minimization.

The standard does not require personal data to work. Fields such as `creator` or `issuer.name` may contain a public name, pseudonym, institutional identifier or neutral value such as `Anonymous`.

UID_AUTH itself does not provide:

- usage monitoring
- automated legal decisions
- platform enforcement
- personal-data collection requirements

Organizations implementing UID_AUTH remain responsible for their own privacy, data-retention and legal compliance obligations.

## License

Apache License 2.0
