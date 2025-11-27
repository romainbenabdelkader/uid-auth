🇬🇧 README  UID_AUTH

Open Standard for Origin Proof & Creative Works Traceability (v1.0)

UID_AUTH is a sovereign, verifiable, and interoperable identifier designed to provide:

•	reliable proof of origin

•	independent cryptographic integrity

•	AI-Act–ready traceability for creative works (music, video, image, text)

UID_AUTH is an open, minimal and extensible standard.
Each institution remains fully sovereign in how it uses and integrates it

This protocol can be used by:

•	Collective Management Organizations (CMOs): SACEM, SOCAN, PRS, GEMA, ASCAP…

•	Cultural institutions

•	DSPs (Spotify, Apple Music, YouTube…)

•	AI platforms

•	Publishers & producers

•	Independent creators

UID_AUTH is an open, neutral, vendor-independent standard that can be integrated into any existing ecosystem.



1.  Standard Objectives

UID_AUTH provides three essential guarantees:

✔ 1. Proof of Origin

A unique, timestamped identifier generated at the moment of declaration and verifiable offline

✔ 2. Cryptographic Integrity

An independent sha3-256 hash ensuring the work has not been altered

✔ 3. AI Act Transparency

A JSON-LD manifest describing usage conditions:

•	AI training (allowed / prohibited / restricted)

•	TDM opt-out

•	human vs. AI origin

•	machine-readable transparency (AI Act compliance)



2. UID_AUTH Protocol Structure

Official format (v1.0):

AUTH.TIMESTAMP.ALGORITHM.VERSION.RANDOM.CHECKSUM

Example

AUTH.2025-11-11T00:40:07Z.sha3-256.v1.89fT1kZa.Qp9eD4

Segment details

Segment	Description

AUTH	Standard prefix

TIMESTAMP	ISO-8601 UTC timestamp

ALGORITHM	sha3-256

VERSION	Protocol version (v1)

RANDOM	Base58 random string (8+ chars)

CHECKSUM	Base58 integrity checksum (6+ chars)

UID_AUTH does not replace ISRC/ISWC.
It adds the missing layer: verifiable origin & integrity



3. Full JSON Example

File: examples/uid_auth_example.json

{
  "uid_auth": "AUTH.2025-11-11T00:40:07Z.sha3-256.v1.89fT1kZa.Qp9eD4",
  "spec_version": "1.0",
  "media_type": "audio/wav",
  "hash": {
    "algorithm": "sha3-256",
    "value": "EXAMPLE-AUDIO-HASH"
  },
  "issued_at": "2025-11-11T00:40:07Z",
  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}

4. 🧾 JSON-LD Manifest (AI Act-Ready)

Each work can be accompanied by a JSON-LD manifest following the AI Rights vocabulary.

File: examples/manifest_example.jsonld

{
  "@context": "https://raw.githubusercontent.com/romainbenabdelkader/uid-auth/main/context/schema/ai-rights-context.jsonld",
  "@type": "CreativeWork",

  "uid_auth": "AUTH.2025-11-11T00:40:07Z.sha3-256.v1.89fT1kZa.Qp9eD4",
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
    "algorithm": "sha3-256",
    "value": "EXAMPLE-AUDIO-HASH"
  },

  "issued_at": "2025-11-11T00:40:07Z",

  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  }
}

5. Interoperability

UID_AUTH coexists seamlessly with existing identifiers:

•	ISRC (recordings)

•	ISWC (works)

•	UPC / EAN

•	DDEX

•	EIDR (audiovisual)

It complements (does not replace) these standards by adding:

👉 verifiable origin

👉 cryptographic integrity

👉 AI Act transparency layer


6. Regulatory Compliance

GDPR

•	no personal data required

•	fully anonymized metadata

•	offline verification possible

AI Act

The JSON-LD manifest provides required transparency signals:

•	human / AI origin

•	usage conditions

•	TDM opt-out

•	machine-readable compliance markers



7.  Repository Structure

uid-auth/
│
├── README.md
├── LICENSE
│
├── schema/
│   └── uid_auth_schema.json
│
├── context/
│   └── ai-rights-context.jsonld
│
├── examples/
│   ├── uid_auth_example.json
│   ├── manifest_example.jsonld
│   └── manifest_us_example.jsonld
│
└── version.txt

8.  Standard Status
    
Status	Description

🟢 Stable	UID_AUTH v1.0 released

🟡 Implementations	Reference libraries in development

🔵 Pilots	Institutional pilots (CMOs & cultural institutions)


9. 📜 License

This standard is published under the Apache 2.0 License, allowing:

•	free usage

•	public or commercial implementation

•	open contributions



10. Contact

For institutional inquiries or collaboration:
romain_ee@yahoo.fr
