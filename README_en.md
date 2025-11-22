# UID_AUTH – AI Origin & Rights Manifest (Open Standard, JSON-LD)

UID_AUTH is an open, neutral, machine-readable standard that links any creative work  
(audio, video, text, image…) to a verifiable origin, rights declaration, and AI Act transparency.

It is not a software product.  
It is an open specification that any institution, CMO, DSP or AI provider can implement  
to guarantee human-origin traceability and legal compliance.

AUTHENTICA provides the reference implementation, but the manifest itself is fully open.

---

## 🎯 Objectives of the Standard

1. Provide a sovereign, unique identifier for creative works (UID_AUTH).
2. Enable AI Act compliance (articles 52, 53, 54 – transparency, labeling, TDM opt-out).
3. Make works readable by AI systems, DSPs and institutions.
4. Offer a neutral layer that Collective Management Organisations can integrate immediately.
5. Enable global interoperability without relying on any single infrastructure.

---

## 📦 Structure of the Manifest (JSON-LD)

Every manifest must follow the structure:

```json
{
  "@context": "https://raw.githubusercontent.com/romainbenabdelkader/uid-auth/main/context/context.jsonld",
  "@type": "CreativeWork",

  "uid_auth": "FR-2025-AUTH-000001",
  "name": "Example Work",
  "creator": "Anonymous",
  "origin": "human",

  "issued_at": "2025-11-11T00:40:07Z",

  "issuer": {
    "name": "AUTHENTICA",
    "type": "IdentityAuthority"
  },

  "rights": {
    "ai_training": "prohibited",
    "tdm_opt_out": true
  },

  "hash": {
    "algorithm": "sha256",
    "value": "EXAMPLE-HASH"
  }
}

🔒 Mandatory Fields
Field	Description
uid_auth	Sovereign unique identifier of the work
origin	“human” or “ai”
issued_at	Timestamp (ISO 8601)
hash	Integrity proof (SHA-256 or stronger)
rights	AI training and TDM usage declarations

🤝 Interoperability Targets

Collective Management Organisations (CMOs)
	•	SACEM
	•	STIM
	•	GEMA
	•	PRS
	•	SIAE

Digital Service Providers (DSPs)
	•	Spotify
	•	YouTube
	•	TikTok
	•	Deezer

AI Providers
	•	OpenAI
	•	Google
	•	Anthropic
	•	Stability

Labels & Publishers
	•	Universal
	•	Warner
	•	Sony
	•	Believe

These organisations can read the manifest immediately without any dependency on AUTHENTICA.

⸻

❓ Why JSON-LD?

JSON-LD is:
	•	used by Google & Schema.org
	•	machine-readable by AI systems
	•	compatible with the EU AI Act
	•	stable, extensible and interoperable

It is the only format combining legal transparency and machine-level readability.


📁 Repository Structure

uid-auth/
│
├── README.md         ← French version
├── README_en.md      ← English version
├── LICENSE           ← MIT open license
├── version.txt
│
├── context/
│   └── context.jsonld
│
├── schema/
│   └── uid_auth_schema.json
│
└── examples/
    └── manifest_example.jsonld


🛠 Licence

This project is released under the MIT license to encourage adoption and interoperability.

🧩 Governance and Contributions

The standard is open.
Institutions, CMOs, DSPs and AI actors may propose improvements through GitHub issues or pull requests.

🧭 Reference Implementation

AUTHENTICA provides the sovereign infrastructure to issue and verify UID_AUTH identifiers.
Any organisation remains free to implement its own validator if needed.

If you need help improving the English version further or adding advanced sections (Security, Governance, AI Act Mapping), I can generate them immédiatement.
