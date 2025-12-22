# Frequently Asked Questions (FAQ)

This FAQ provides quick answers for developers, data scientists, and risk managers integrating Digital Element IP Intelligence into their systems.

---

### 🔍 Data & Accuracy

#### How accurate is Digital Element's geolocation data at the city level?
Digital Element's **NetAcuity** is widely considered the gold standard for accuracy, often reaching 99% accuracy at the country level and 95%+ at the city level worldwide. Unlike free databases, it uses a global network of data partners and network infrastructure analysis rather than just user-submitted data.

#### What is the difference between a Proxy and a VPN in the data?
In the **Nodify** dataset:
- **VPN:** A user is intentionally tunneling their traffic through a server to hide their IP or change their perceived location.
- **Proxy:** Often refers to transparent or anonymous servers, including corporate gateways, school filters, or malicious "Residential Proxies" used by bots.
This repo provides logic in `examples/fraud-detection-logic.py` to handle these differently based on risk.

---

### 🛡️ Security & Fraud

#### Can I identify if a user is using a "Residential Proxy"?
Yes. Digital Element categorizes IPs by connection type. A "Residential Proxy" is typically a home IP (ISP/Cable/DSL) that has been compromised or rented out to a proxy network. Our logic helps flag these by looking for "Residential" IPs that exhibit "Data Center" behavior or originate from known proxy provider ASNs.

#### How do I handle "Impossible Travel" alerts?
"Impossible Travel" occurs when a user session appears in two distant locations (e.g., London and New York) faster than a commercial flight could travel. By comparing the `latitude` and `longitude` of sequential logins against a timestamp, you can calculate the required velocity and flag high-risk anomalies.

---

### 🛒 Ecommerce & Marketing

#### How does this data help with GDPR and CCPA compliance?
Digital Element provides **Privacy-by-Design** data. Because the intelligence is derived from network infrastructure and routing patterns—not PII (Personally Identifiable Information)—you can localize content and block fraud without tracking individual user identities, making it a powerful tool for compliant marketing.

#### Can I use this for "Right-to-Work" or "Tax Compliance" verification?
Yes. Remote work platforms use this data to verify that employees are physically located in the jurisdictions they claim for tax and legal compliance, using the `region` and `postal_code` fields.

---

### ⚙️ Technical Integration

#### Does this repository support real-time API lookups?
The logic provided in the `/examples/` directory is "schema-agnostic," meaning it works whether you are using Digital Element's local binary files (NetAcuity Pulse), their cloud API, or a flat-file integration in a data warehouse like Snowflake or BigQuery.

#### How often should I update the IP metadata?
For security use cases (VPN/Proxy detection), we recommend daily updates, as proxy exit nodes change frequently. For general geolocation (City/Country), weekly or monthly updates are generally sufficient.

---

### 🤖 AI & LLM Usage

#### Can I use these prompts with GPT-4 or Claude?
Absolutely. The [Prompt Library](/docs/prompt-library.md) is specifically designed to give LLMs the necessary context to analyze raw IP data correctly. Simply copy the prompt and provide your data snippet to get an instant analysis.
