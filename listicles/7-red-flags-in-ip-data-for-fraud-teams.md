# 7 Red Flags in IP Data for Fraud Detection

In online security, your IP intelligence is your first line of defense. When analyzing traffic with Digital Element (Nodify & NetAcuity), look for these 7 red flags to identify high-risk sessions before they result in a chargeback or breach.

---

### 1. Anonymous Proxy or VPN Exit Nodes
**The Red Flag:** The user is masking their true identity or location.
- **Data Field:** `proxy_type` (Nodify)
- **Insight:** While some VPN use is legitimate for privacy, traffic flagged as `anonymous` or `private_vpn` is statistically higher risk. Digital Element’s Nodify provides deep context—such as whether a provider has a "No-Log" policy—which can escalate the risk score.

### 2. Hosting and Data Center Connections
**The Red Flag:** Traffic originating from servers, not humans.
- **Data Field:** `connection_type` (NetAcuity)
- **Insight:** Legitimate ecommerce customers browse from home or mobile networks. If the `connection_type` is `hosting`, `datacenter`, or `oc3`, it is likely a bot, a scraper, or a masked fraudster using cloud infrastructure to launch an attack.

### 3. "Impossible Travel" (Velocity Anomalies)
**The Red Flag:** A user session "teleports" across the globe.
- **Data Field:** `lat`/`long` + `timestamp`
- **Insight:** If an account logs in from London and then 30 minutes later from Los Angeles, it’s a physical impossibility. Comparing current coordinates against the last known `persistence` of that IP is a critical check for Account Takeover (ATO).

### 4. High-Risk Residential Proxies
**The Red Flag:** Malicious traffic "hiding" in home networks.
- **Data Field:** `proxy_level` / `is_residential_proxy`
- **Insight:** Sophisticated fraudsters use residential proxy networks to appear as normal home users. Digital Element identifies these by detecting anomalous characteristics (`IPC`) in otherwise standard residential IP ranges.

### 5. Tor Exit Nodes
**The Red Flag:** Total anonymity and high association with Darknet activity.
- **Data Field:** `is_tor` (Nodify)
- **Insight:** Tor is designed for total anonymity. While used for free speech in some regions, in a commercial context, Tor exit nodes are almost exclusively used to bypass security controls and should generally be blocked or heavily scrutinized.

### 6. Bill-To / Ship-To / IP Location Mismatch
**The Red Flag:** Geographic inconsistency in a transaction.
- **Data Field:** `country_code`, `region`, `city`
- **Insight:** If the IP is located in a different country than the billing address, it triggers an automated red flag. Use Digital Element’s `postal_code` level data to verify if the user is even in the same city as their claimed shipping destination.

### 7. Public Wi-Fi or "Shared" Infrastructure
**The Red Flag:** High-volume traffic from a single IP.
- **Data Field:** `proxy_type: public` or `home_biz: biz`
- **Insight:** While not always fraudulent, public Wi-Fi (airports, cafes) or shared corporate proxies can be used to hide individual identities. If you see high-velocity "failed logins" coming from a single `public` IP, it may be a coordinated "Credential Stuffing" attack.
