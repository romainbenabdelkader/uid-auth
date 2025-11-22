AI Origin Manifest Open Standard (v1.0)

Machine-readable metadata model for human-origin proof, AI Act transparency, and TDM opt-out declarations.

This repository defines an open, neutral, interoperable JSON manifest enabling:
	•	Human-origin declaration
	•	AI Act transparency compliance (Art. 52–54)
	•	TDM (Text-and-Data Mining) opt-out
	•	Sovereign unique identifier (UID_AUTH)
	•	Integrity hashing (SHA-256)
	•	Interoperability with CMOs (collecting societies), DSPs and AI systems
	•	Non-personal rights attribution (GDPR-safe)

It is not tied to any platform and can be implemented by:
	•	collecting societies (SACEM, STIM, GEMA, PRS, JASRAC…)
	•	DSPs (Spotify, Apple, TikTok, Deezer…)
	•	labels / publishers
	•	archives / libraries / cultural institutions
	•	AI models and dataset builders

The manifest is deliberately simple, extensible, and adapted to the AI era.

⸻

🌍 Purpose of the standard

The European AI Act requires:
	•	clear disclosure of whether content is human or AI-generated
	•	machine readable transparency metadata
	•	mandatory opt-out for AI training (TDM)
	•	traceability and verifiable origin
	•	auditability for cultural institutions

However, no cross-industry open format currently fulfils these requirements.

This standard provides a simple, sovereign, European-aligned metadata format.

📦 Manifest fields

Field Description

uidAuth
Sovereign unique identifier for the work (non-personal).

origin
"human", "ai", or "hybrid".

tdmOptOut
Prevents AI models from training on the work (AI Act).

integrityHash
SHA-256 hash of the source file at creation.

createdAt
ISO 8601 timestamp of first registration.

rightsSociety
Collecting society (CMO) handling rights (optional).

workCode
Registered work identifier (ISWC or internal code).

version
Manifest version.

aiActPolicy
Additional AI usage constraints.

📄 Example manifest

See file: manifest-example.json

{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "version": "1.0",
  "uidAuth": "AUTH-FR-2025-00001234",
  "origin": "human",
  "tdmOptOut": true,
  "integrityHash": "sha256:3b6f0e1a8c91c0b2d2bb5f0d9f674dbf1c3c0dd120f7e3fb5a88bc1d9aef2e01",
  "createdAt": "2025-11-22T14:32:00Z",
  "rightsSociety": "SACEM",
  "workCode": "ISWC-T1234567890",
  "aiActPolicy": {
    "trainingAllowed": false,
    "generationAllowed": false,
    "disclosureRequired": true
  }
}

🧩 Compatibility with AUTHENTICA

AUTHENTICA provides:
	•	UID_AUTH generation
	•	integrity hashing
	•	verification logic
	•	origin certification
	•	interoperability with collecting societies

AUTHENTICA is an implementation reference, but the manifest
remains open, neutral and free to use.

⸻

📜 License

This specification is available under a permissive open license,
allowing any organization to adopt or extend it.

⸻

🏛️ Versioning
	•	v1.0 → core transparency fields, AI Act alignment, CMO compatibility

	•	Future versions may extend provenance, signatures, cryptographic binding

while maintaining backward compatibility.

