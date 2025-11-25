UID_AUTH Open Standard for Creative Work Identity & Traceability

Universal manifest for provenance, copyright enforcement, and AI-training rights

UID_AUTH is an open, interoperable and neutral standard for assigning a unique, verifiable identity to any creative work (audio, video, text, image) and describing its rights, provenance, and AI-training permissions using JSON-LD

The goal is to provide a universal identifier layer compatible with both:

•	🇪🇺 EU regulations (AI Act, Copyright Directive, TDM opt-out)

•	🇺🇸 US copyright & fair-use environment (DMCA, C2PA compatibility)

UID_AUTH is technology-neutral:

no blockchain required

no proprietary watermark

no dependency on closed SDKs


1. Objectives

UID_AUTH provides:

• A unique sovereign identifier

Stable ID for any creative work
(e.g., 
“FR-SACEM-2025-001234”, 
“US-ASCAP-2026-002781”).

• A JSON-LD manifest for machine-readable rights

Including:

	•	human origin declaration

•	AI-training permissions

•	TDM opt-out

•	jurisdiction

•	hash & integrity

•	issuer identity

•	provenance chain

• Compatibility with EU, US and global ecosystems

Designed to interoperate with:

•	SACEM, ADAMI, SPEDIDAM

•	ASCAP, BMI, SESAC

•	SOCAN

•	C2PA / Content Authenticity Initiative

•	Digital platforms (YouTube, Spotify, Deezer…)

2. Repository Structure

uid-auth/
│
├── context/        # JSON-LD @context files
├── schema/         # JSON Schemas for validation
├── examples/       # Manifest examples (EU / US)
├── us/             # US-compatible profiles
│   └── .keep
│
├── README.md
├── README_en.md
├── README.US.md
└── version.txt

3. EU Manifest Example (AI Act Ready)

➡️ See examples/eu_manifest_example.jsonld


4. US Manifest Example

➡️ See examples/manifest_us_example.jsonld

Includes fields specific to:

•	DMCA compatibility

•	Fair-use considerations

•	C2PA alignment

•	US CMOs like ASCAP/BMI

5. JSON Schema

/schema/uid_auth_schema.json

Covers:

•	rights (AI training permissions)

•	jurisdiction

•	tdm_opt_out

•	hash integrity

•	issuer metadata

•	provenance chain

6. License

Apache-2.0 License free to use in commercial or institutional contexts.

7. Contact & Usage

UID_AUTH can be integrated into:

•	content ingestion workflows

•	rights management systems

•	copyright societies

•	DSP ingestion pipelines

•	generative AI safety layers

For institutional pilots (EU or US), contact:

romain@lockdna.tech
