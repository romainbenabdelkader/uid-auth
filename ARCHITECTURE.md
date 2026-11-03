# Ecosystem Architecture

Documentation checked on 2026-11-03. The layers have separate formats and
versions; a shared field name does not establish interchangeable manifests.

## The three layers

1. **AURA** defines signed origin declarations and exact-byte asset bindings.
   Manifest schemas 1.0 and 1.1 require `aura_uid` and an Ed25519 signature over
   the RFC 8785 JCS payload. The reference verifier supports SHA3-256 asset
   hashes. Cryptographic verification does not establish the truth of origin,
   authorship or issuer authority.
2. **UID_AUTH** defines a declared work identifier and accompanying metadata.
   The schema checks identifier shape, not global allocation or uniqueness.
   Its identifier is optional in the AURA core.
3. **AUTHENTICA AI Rights & Origin Manifest** is the separate JSON-LD rights
   profile in `authentica-ai-rights`. Its own schema requires `uid_auth`.
   This public profile is distinct from the private AUTHENTICA application.

The AURA core covers different digital asset types and requires no professional
identifier or institutional affiliation. A profile may add its own fields;
those fields do not become prerequisites for every AURA declaration.

## Format boundaries

| Property | UID_AUTH schema v1.0 | AUTHENTICA AI Rights draft schema |
| --- | --- | --- |
| `rights.ai_training` | `prohibited`, `allowed`, `restricted`, `conditional` | `prohibited`, `permitted`, `license_required`, `unknown` |
| `hash.algorithm` | `sha256` | `sha256` or `sha3-256` |
| `hash.value` | 64 hexadecimal characters | Any nonempty string |
| `uid_auth` shape | Category segment required | Category segment optional |
| `spec_version` | Required, exactly `1.0` | Not required |
| JSON-LD fields | Not required by the schema | `@context` and `@type: CreativeWork` required |

Sources: [UID_AUTH schema](https://github.com/romainbenabdelkader/uid-auth/blob/c99fbe03ec374dc71ffbd9b30081a7fe90b6d0d4/schema/uid_auth_schema.json)
and [AI Rights schema](https://github.com/romainbenabdelkader/authentica-ai-rights/blob/76cddff75b21d94535561af5077096a828cb4c2e/manifest/schema.json).
The table lists selected differences, not a complete conversion contract.

Neither schema requires an AURA signature or the full AURA manifest envelope.
AURA-VERIFIER v1.2.2 does not accept these standalone documents as AURA evidence.
A separately specified integration can carry declarations in a signed AURA
manifest, but its signature does not validate the domain-specific semantics.
Any mapping needs versioned field rules and tests. Never silently substitute
rights vocabulary or rewrite existing signed material. SHA3-256 of an asset
must be computed from its bytes; it cannot be derived from its SHA-256 digest.

## Independence and verification scope

AURA does not depend on UID_AUTH, AUTHENTICA or a particular issuer registry.
The TPKR is a conceptual model; the reference verifier's local issuer-snapshot
contract is documented in its integrator guide.

Schema validation checks declared structure. It does not authenticate a creator,
verify authority, compare an asset's bytes or establish a trusted date.
The profile's `issued_at` is declared. Omission of a rights signal is not
permission, a licence or absence of rights.

## Repositories and current references

| Repository | Role |
| --- | --- |
| [AURA-STANDARD](https://github.com/romainbenabdelkader/AURA-STANDARD) | Open specification; archived release v1.2.1, manifest schemas 1.0/1.1 |
| [AURA-VERIFIER](https://github.com/romainbenabdelkader/AURA-VERIFIER) | Published reference verifier v1.2.2 |
| [aura-core](https://github.com/romainbenabdelkader/aura-core) | Historical Python v0.1 educational primitives |
| [aura-cli](https://github.com/romainbenabdelkader/aura-cli) | Historical Python v0.1 demonstration |
| [uid-auth](https://github.com/romainbenabdelkader/uid-auth) | Separate identifier format and metadata schema |
| [authentica-ai-rights](https://github.com/romainbenabdelkader/authentica-ai-rights) | Separate draft AI rights and origin profile |

The Python demonstrations are not current-format signing SDKs. Start a current
AURA integration with the [v1.2.2 integrator guide](https://github.com/romainbenabdelkader/AURA-VERIFIER/blob/08d7c70404bab16e2e3b09bb9e59aefaf6fa5391/INTEGRATORS.md).
Archives: [AURA-STANDARD v1.2.1](https://doi.org/10.5281/zenodo.22071523)
and [AURA-VERIFIER v1.2.2](https://doi.org/10.5281/zenodo.23917182).
These references do not certify either application profile or its implementations.
