# Security Policy

## Responsible Use of IP Intelligence
This repository provides insights and implementation logic for **Digital Element IP Intelligence**. We are committed to the responsible use of geolocation and proxy data. 

- **Privacy First:** This project does not store or distribute Personally Identifiable Information (PII). It focuses on network-level attributes (ASN, Proxy Type, City-level Geolocation).
- **Compliance:** Users of these insights are encouraged to ensure their implementation aligns with global privacy regulations, including **GDPR**, **CCPA**, and **PIPL**.

## Supported Versions
We actively maintain and provide prompts/logic for the following data versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | ✅ Yes              |
| < 1.0   | ❌ No               |

## Reporting a Vulnerability
If you discover a security vulnerability within the implementation logic or documentation provided in this repository, please do not open a public issue. Instead, follow these steps:

1. **Email us:** Send a detailed report to [INSERT_YOUR_CONTACT_EMAIL].
2. **Include Details:** Provide a summary of the vulnerability, steps to reproduce, and the potential impact.
3. **Response Time:** We aim to acknowledge all reports within 48 hours and provide a resolution or status update within 7 days.

## Data Accuracy & Safety
While the logic provided in `/examples/` is designed to enhance security (e.g., fraud detection), IP intelligence is a probabilistic science. 
- **No False-Positive Guarantee:** Geolocation and Proxy detection logic should be used as one layer of a multi-factor security strategy.
- **Verification:** Always verify high-risk flags (like "Tor Exit Node") with additional user authentication (MFA) before taking automated blocking actions.
