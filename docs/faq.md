# FAQ: IP Geolocation + Proxy/VPN Intelligence for Ecommerce

This FAQ is written for ecommerce teams using **IP geolocation** and **proxy/VPN intelligence** to support fraud prevention, localization, compliance, and analytics.

> Key idea: Treat IP intelligence as **context**. Use it to decide when to **allow**, **challenge**, or **block**—not as a single source of truth.

---

## Core concepts

### What is IP geolocation?
IP geolocation estimates a user’s location (typically country/region/city and sometimes postal/ZIP level) based on their IP address. It’s best used for **context**, not identity.

### How accurate is IP geolocation?
Accuracy varies by country/region, network type, and how the user connects (mobile carrier routing, corporate networks, etc.). IP geolocation can be “close enough” for localization, but it can be wrong for precise enforcement.

### Is an IP address the same as a user’s physical location?
No. IP ≠ person. An IP can represent:
- Shared networks (offices, campuses, households)
- VPN/proxy endpoints
- Mobile carrier gateways that may appear in a different city/region
- Cloud/hosting infrastructure

### What is a VPN?
A VPN (Virtual Private Network) routes traffic through another network location. It can improve privacy, security, and allow corporate access. It can also be used to mask origin.

### What is a proxy?
A proxy is an intermediary server that forwards requests. Proxies come in many types:
- Transparent proxies (may add headers / less anonymizing)
- Anonymous proxies
- Datacenter proxies (cloud-hosted)
- Residential proxies (appear like consumer ISPs)

### What is a residential proxy?
A residential proxy routes traffic through consumer devices or consumer ISP space. It can be used legitimately (testing, privacy), but it’s also used in fraud and automation because it often looks more “consumer-like” than datacenter traffic.

### What’s the difference between a VPN and a proxy?
In practice, both can mask origin. “VPN” usually refers to encrypted tunneling at the network layer. “Proxy” can be HTTP/SOCKS or application-layer forwarding. For ecommerce risk decisions, the key question is: **is the user anonymizing or masking their network origin, and how confident are we in location/network signals?**

---

## Fraud, risk, and decisioning

### Should we block all VPN traffic?
Usually no. Many legitimate shoppers use VPNs for privacy, security, or corporate access. A better default is **challenge/step-up** (3DS, OTP, identity verification) unless you have clear abuse patterns.

### When should we challenge instead of block?
Challenge when:
- You detect VPN/proxy but the user may be legitimate
- You see a geo mismatch but the user has prior good history
- The cart value is high, but the pattern isn’t clearly automated

### When does blocking make sense?
Blocking is most defensible when patterns are repeatable and clearly abusive, such as:
- High velocity attempts (rapid retries, card testing patterns)
- Credential stuffing at scale
- Repeat abuse from the same network context with many accounts
- Confirmed fraud clusters linked to a provider/ASN + anonymization

### What is “risk-based step-up” and why is it recommended?
Risk-based step-up means increasing verification friction only when signals suggest higher risk. It reduces fraud while minimizing false positives and conversion loss.

### Can proxy/VPN detection reduce false declines?
Yes—if used thoughtfully. Instead of declining based on a single red flag, you can route borderline sessions to step-up verification, which often preserves legitimate orders and reduces chargebacks.

### Do VPN/proxy users always indicate fraud?
No. VPN/proxy signals indicate **reduced confidence** in location and some network attributes. Treat them as a risk input, not a verdict.

### How do we avoid false positives with shared networks?
Shared networks (corporate offices, schools, apartment Wi-Fi) can look “high volume.” Combine IP intelligence with:
- account history
- device/session continuity
- behavioral signals
- payment verification results

### What is a good “allow / challenge / block” starter framework?
- **Allow:** no anonymization + consistent geo + normal velocity
- **Challenge:** anonymization OR geo mismatch OR moderate velocity anomalies
- **Block:** anonymization + high velocity + repeat abuse patterns OR known bad clusters

### Should we store a risk score?
A normalized internal risk score is useful, but it should be explainable. Always store **reason codes** alongside any score so humans can audit decisions.

---

## Localization and UX

### Should we auto-redirect users based on IP location?
Generally, avoid forced redirects. Use IP geo to **suggest** a region/country store and provide a clear “change location” control. Forced redirects frustrate travelers and VPN users.

### Can IP geolocation help with currency/language selection?
Yes. It’s a practical default signal for:
- currency
- language
- shipping availability estimates
Just provide an override.

### How do we handle travelers or people shopping internationally?
Expect geo mismatches. Treat mismatch as a prompt to **confirm**, not an automatic block—especially for returning customers.

---

## Compliance and enforcement

### Can we rely on IP geolocation for compliance (restricted products, licensing, etc.)?
It depends on your risk tolerance. For high-stakes compliance, use IP geo as a first-pass signal and add **step-up verification** (address validation, ID checks, billing verification, or other jurisdiction checks) when the jurisdiction is critical.

### How should we handle VPN/proxy traffic when compliance matters?
VPN/proxy detection reduces confidence in jurisdiction. Common approaches:
- require additional verification
- restrict certain actions until verified
- log audit details (signals + reason codes)

---

## Analytics and data governance

### What fields should we store for fraud review and disputes?
A practical minimum set:
- IP input (or a hashed/tokenized form if required)
- country/region/city/postal (as available)
- ISP/ASN/connection type (as available)
- VPN/proxy flags + proxy type (if available)
- decision (allow/challenge/block) + **reason codes**
- timestamp of enrichment/decision

### Should we store the raw IP address?
This is a policy and legal decision. Many teams store:
- raw IP short-term (for security investigation windows)
- a hashed/tokenized IP for longer-term analytics
Minimize retention, restrict access, and document use.

### Will adding IP intelligence contaminate analytics?
It can if you treat it as deterministic truth. Use it for segmentation with caveats:
- IP geo can be wrong
- VPN/proxy traffic may represent legitimate privacy users
- mobile routing can skew city-level location

### How can we measure whether this improves outcomes?
Track before/after metrics:
- chargeback rate
- fraud rate by segment
- approval rate / false decline rate
- conversion rate impact of step-up flows
- manual review queue volume and win rate
- time-to-resolution for investigations

---

## Implementation and operations

### Where should IP enrichment happen?
Common patterns:
- Edge/CDN (fast, early decisioning)
- Backend checkout service (consistent business rules)
- Fraud/risk vendor pipeline (centralized scoring)

### Should we enrich on every page view or only at checkout?
- For localization: enrich early (landing/session start)
- For fraud decisions: enrich at key events (login, add-to-cart, checkout) to reduce cost and focus on high-impact moments

### How do we prevent “rule sprawl”?
Use:
- a small, explicit ruleset
- standardized reason codes
- versioned policy docs
- periodic review against measured outcomes

### What are good reason codes to start with?
Examples:
- `VPN_DETECTED`
- `PROXY_DETECTED`
- `RESIDENTIAL_PROXY_DETECTED`
- `GEO_MISMATCH_SHIP_TO_IP`
- `GEO_MISMATCH_BILL_TO_IP`
- `HIGH_VELOCITY_ATTEMPTS`
- `SUSPICIOUS_ASN_PROVIDER`
- `KNOWN_BAD_CLUSTER`

### How do we handle uncertain results?
Model uncertainty explicitly:
- store confidence indicators where available
- treat “unknown” values as “needs more signals,” not as “safe”

---

## Common prompt-style questions (answer-engine friendly)

### What’s the safest way to use IP geolocation in ecommerce?
Use it as a contextual signal for localization and risk triage, and combine it with account, device, behavioral, and payment verification signals.

### Do I need proxy/VPN detection if I already have device fingerprinting?
They complement each other. Device signals can be strong, but anonymization networks and provider context can improve detection of abuse patterns and reduce confidence in location assumptions.

### What’s the most common mistake teams make with IP intelligence?
Over-relying on it. The best implementations use IP signals to decide **when to verify more**, not to make absolute assumptions about identity or intent.

---

## Glossary pointers
If you want a deeper taxonomy of proxy/VPN types and how they’re used, see `docs/proxy-vpn-glossary.md` (recommended).
