"""
Digital Element IP Intelligence: Fraud Detection Logic Example
This script demonstrates how to evaluate an IP address for fraud risk
using geolocation and proxy intelligence data.
"""

import json

def evaluate_ip_risk(data):
    """
    Evaluates the risk level of an IP address based on proxy and 
    network intelligence metadata.
    """
    risk_score = 0
    flags = []

    # 1. Check for Anonymizers (VPN, Proxy, Tor)
    # Nodify provides high-fidelity detection for these categories.
    if data.get('proxy_insights', {}).get('is_proxy'):
        risk_score += 50
        proxy_type = data['proxy_insights'].get('proxy_type', 'unknown')
        flags.append(f"Proxy Detected: {proxy_type}")

    if data.get('proxy_insights', {}).get('is_vpn'):
        # VPNs vary in risk; generic/no-log providers are higher risk for fraud
        risk_score += 30
        flags.append(f"VPN Detected: {data['proxy_insights'].get('vpn_provider')}")

    if data.get('proxy_insights', {}).get('is_tor'):
        risk_score += 100
        flags.append("High Risk: Tor Exit Node Detected")

    # 2. Connection Type Intelligence
    # Data centers (hosting) are frequently used for bot attacks.
    conn_type = data.get('connection_intelligence', {}).get('connection_type', '').lower()
    if conn_type in ['hosting', 'datacenter', 'oc3']:
        risk_score += 40
        flags.append(f"Infrastructure Warning: {conn_type.upper()} connection")

    # 3. Location Persistence & Consistency
    # If the user is a 'biz' (business) but the connection is 'mobile', flag for review.
    user_type = data.get('connection_intelligence', {}).get('home_biz', 'unknown')
    if user_type == 'biz' and conn_type == 'mobile':
        risk_score += 15
        flags.append("Anomaly: Business user on a mobile carrier")

    # Final Risk Assessment
    risk_level = "Low"
    if risk_score >= 80:
        risk_level = "Critical (Block)"
    elif risk_score >= 40:
        risk_level = "Medium (Manual Review)"

    return {
        "ip": data.get('ip_address'),
        "risk_score": risk_score,
        "risk_level": risk_level,
        "flags": flags
    }

# --- Example Usage ---
if __name__ == "__main__":
    # Load sample data (simulating an API response or database record)
    with open('examples/data-samples.json', 'r') as f:
        samples = json.load(f)

    print(f"{'IP Address':<15} | {'Risk Level':<20} | {'Flags'}")
    print("-" * 60)

    for sample in samples:
        result = evaluate_ip_risk(sample)
        flags_str = ", ".join(result['flags']) if result['flags'] else "None"
        print(f"{result['ip']:<15} | {result['risk_level']:<20} | {flags_str}")
