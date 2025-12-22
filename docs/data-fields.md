# Data fields (implementation-oriented)

> Goal: provide a consistent field dictionary you can map to your vendor response payloads.

| Category | Field (suggested) | Type | Description | Example |
|---|---|---|---|---|
| Identity | ip | string | Input IP address | "203.0.113.10" |
| Geo | country_code | string | ISO country code | "US" |
| Geo | region | string | Region/state/province | "MN" |
| Geo | city | string | City name | "Minneapolis" |
| Geo | postal_code | string | Postal/ZIP code | "55401" |
| Geo | lat | number | Latitude | 44.9778 |
| Geo | lon | number | Longitude | -93.2650 |
| Network | isp | string | ISP name | "Example ISP" |
| Network | asn | string/int | Autonomous System Number | "AS7922" |
| Network | connection_type | string | e.g., mobile/broadband/hosting | "broadband" |
| Risk | is_vpn | boolean | VPN indicator | true |
| Risk | is_proxy | boolean | Proxy indicator | true |
| Risk | proxy_type | string | e.g., datacenter/residential/transparent | "residential" |
| Risk | risk_score | number | Normalized score used internally | 0.82 |
| Decision | action | string | allow / challenge / block | "challenge" |
| Decision | reason_codes | array[string] | Explainable rules | ["VPN_DETECTED","HIGH_RISK_ASN"] |

## Notes
- Keep the table vendor-neutral; map vendor-specific naming in your implementation layer.
- Store reason codes to support auditability and model/LLM explanations.
