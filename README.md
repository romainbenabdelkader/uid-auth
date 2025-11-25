UID_AUTH  Universal Identity for Creative Works

Open standard for origin proof and traceability of creative works (v1.0)



UID_AUTH is a sovereign, verifiable and interoperable identifier designed to provide:

- origin proof  

- cryptographic integrity  

- reliable traceability of works in the age of AI  

It can be used by:

- collective management organisations (SACEM, SOCAN, PRS, GEMA, ASCAP, …)

- cultural institutions

- DSPs (Spotify, Apple Music, YouTube, …)

- AI platforms

- publishers and producers

- individual creators

UID_AUTH is an open, neutral standard with no commercial lock-in, designed to be integrated in any ecosystem



1. Goals of the standard

UID_AUTH provides three core guarantees:

✔ Origin proof

A unique, time-stamped and verifiable identifier attached to a work.

✔ Cryptographic integrity

An independent hash allowing verification that a work has not been modified.

✔ AI Act transparency

A JSON-LD manifest describing usage conditions, including AI training and TDM opt-out.


2. UID_AUTH protocol structure

The generic format is:

text

AUTH.TIMESTAMP.ALGO.VERSION.RANDOM.CHECKSUM

Segment description:

Segment	Description

AUTH	Standard prefix

TIMESTAMP	ISO 8601 UTC timestamp

ALGO	Cryptographic algorithm (e.g. sha3-256)

VERSION	UID_AUTH protocol version (e.g. v1)

RANDOM	Base58 random string (8+ chars)

CHECKSUM	Base58 integrity check (6+ chars)

Segment	Description

AUTH	Standard prefix

TIMESTAMP	ISO 8601 UTC timestamp

ALGO	Cryptographic algorithm (e.g. sha3-256)

VERSION	UID_AUTH protocol version (e.g. v1)

RANDOM	Base58 random string (8+ chars)

CHECKSUM	Base58 integrity check (6+ chars)

AUTH.2025-11-11T00:40:07Z.sha3-256.v1.89fT1kZa.Qp9eD4


3. UID_AUTH example (JSON)

{
  "uid_auth": "AUTH.2025-11-11T00:40:07Z.sha3-256.v1.89fT1kZa.Qp9eD4",
  "spec_version": "1.0",
  "media_type": "audio/wav",
  "hash": {
    "algorithm": "sha256",
    "value": "EXAMPLE-AUDIO-HASH"
  },
  "issued_at": "2025-11-11T00:40:07Z",
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}

4. JSON-LD Manifest (AI-Act ready)

Each work can be accompanied by a JSON-LD manifest using the AI-rights context.

Audio example:

{
  "@context": "https://raw.githubusercontent.com/romainbenabdelkader/uid-auth/main/schema/ai-rights-context.jsonld",
  "@type": "CreativeWork",

  "uid_auth": "FR-2025-AUTH-MUS-000001",
  "spec_version": "1.0",
  "media_type": "audio/wav",

  "name": "Example Audio Work",
  "creator": "Anonymous",
  "origin": "human",

  "rights": {
    "ai_training": "prohibited",
    "tdm_opt_out": true
  },

  "hash": {
    "algorithm": "sha256",
    "value": "EXAMPLE-AUDIO-HASH"
  },

  "issued_at": "2025-11-11T00:40:07Z",

  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}

5. Interoperability

UID_AUTH is designed to co-exist with existing identifiers:

	•	ISRC (recordings)

	•	ISWC (works)

	•	UPC / EAN

	•	DDEX

	•	EIDR (audiovisual)

It does not compete with these systems:

it provides the missing origin-proof layer that can be attached to them.



6. Standard governance

UID_AUTH is an evolutive standard under institutional governance:

•	changes follow an open RFC-style process

•	consultation of CMOs, DSPs and cultural institutions

•	multi-stakeholder technical committee

•	backward compatibility is preserved



7. Regulatory compliance

GDPR

•	no personal data required

•	anonymised processing

•	offline verification is possible

AI Act

The AI-rights manifest provides:

•	work origin (human / AI-generated / hybrid)

•	usage conditions

•	TDM opt-out signal

•	machine-readable transparency



8. Repository structure

uid-auth/├── README.md
├── LICENSE
├── schema/
│   ├── uid_auth_schema.json
│   └── ai-rights-context.jsonld
├── context/
│   └── context.jsonld
├── examples/
│   ├── uid_auth_example.json
│   ├── manifest_example.jsonld
│   └── manifest_us_example.jsonld
└── version.txt


9. Standard status

Status	Description

🟢	UID_AUTH v1.0 – stable specification

🟡	Reference libraries – in development

🔵	Institutional pilots (CMOs & cultural bodies)

10. Licence

This standard is published under the Apache 2.0 licence, allowing:

•	free use

•	free implementation (public or commercial)

•	open contributions



11. Contact

For institutional questions or collaborations: romain@lockdna.tech
