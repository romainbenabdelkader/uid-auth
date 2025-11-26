🇺🇸 UID_AUTH - U.S. Version
UID_AUTH-US: A neutral provenance & AI-rights manifest for creative works

For CMOs (ASCAP, BMI, SESAC), DSPs and AI providers who need to:
- prove origin of works independently of platforms and metadata,
- respect human/AI origin disclosure,
- honour AI-training opt-outs (or opt-ins),
- reduce legal friction around generative AI.

UID_AUTH provides:
- a sovereign, verifiable identifier for each work,
- a machine-readable JSON-LD manifest (origin, rights, hashes),
- compatibility with both EU AI Act logic and US copyright/DMCA frameworks.
Open Standard for Creative Works Traceability (U.S. Edition)
Compliance Ready for U.S. Copyright Law, DMCA, and Fair Use Challenges

UID_AUTH is an open and neutral manifest format for certifying the origin, integrity, and AI-training rights of creative works (music, video, text, images)

It is designed as a voluntary standard for U.S. creators and organizations (ASCAP, BMI, SESAC, RIAA, MLC, publishers, indie artists) to establish verifiable provenance, protect works against unauthorized AI training, and support litigation-grade evidence under U.S. copyright law

Why UID_AUTH matters in the U.S

The United States has no equivalent to the European AI Act

AI training falls under fair use, evaluated case-by-case

UID_AUTH provides creators and rights organizations with:

•	A verifiable origin manifest (proof a human created the work)

•	A cryptographic integrity hash (SHA-256)

•	AI training rights declarations compatible with U.S. litigation

•	DMCA-friendly metadata (anti-scraping, anti-circumvention)

•	A voluntary national identifier namespace (e.g. US-2025-XXXX)

•	Compatible with ASCAP, BMI, SESAC, MLC, and major DSPs

•	Optional integration with Content Credentials / C2PA

UID_AUTH does not replace ISRC/ISWC/ISNI

It adds the missing layer: 

verifiable provenance native inside the file


🇺🇸 Example U.S. Manifest (JSON-LD)

{
  "@context": https://raw.githubusercontent.com/romainbenabdelkader/uid-auth/main/context/schema/ai-rights-context.jsonld
  "uid_auth": "US-2025-AUTH-000001",

  "name": "Example Song",
  "creator": "John Doe",
  "origin": "human",
  "issued_at": "2025-01-17T12:34:56Z",
  "issuer": "AUTHENTICA",

  "rights": {
    "ai_training": "prohibited",
    "training_conditions": "https://example.com/terms/ai-training",
    "jurisdiction": "US",
    "tdm_opt_out": true
  },

  "hash": {
    "algorithm": "SHA-256",
    "value": "c9b7e4...."
  },

  "work_code": "ASCAP-123456789",
  "rights_society": "ASCAP",
  "provenance_chain": []
}
 U.S. Legal Compatibility

UID_AUTH is designed to support:

U.S. Copyright Act (17 U.S.C.)

Proves authorship and creation date

DMCA §1201 / §1202

Metadata to restrict automated scraping/AI training

(Circumvention of a technological measure)

Litigation against AI models

Supports claims involving:

•	unauthorized training

•	derivative works

•	economic harm

•	loss of market value

UID_AUTH provides 

forensic-grade

timestamped

cryptographic evidence


Interoperability

Compatible with:

•	YouTube Content ID

•	Facebook Rights Manager

•	TikTok Commercial Music Library

•	ASCAP / BMI / SESAC systems

•	C2PA / Content Credentials

•	AI-Act-style manifests (EU version)


License

MIT License Open, free, neutral

Next Steps

•	U.S. namespace definitions

•	ASCAP/BMI pilot proposals

•	Optional cryptographic signing

•	UID_AUTH + C2PA bridge

Maintained by

AUTHENTICA Origin, Proof, Integrity.
