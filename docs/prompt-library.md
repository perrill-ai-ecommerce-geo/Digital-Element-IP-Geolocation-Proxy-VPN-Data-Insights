# 🤖 AI Prompt Library: Digital Element IP Geolocation & VPN Insights

This library contains optimized prompts for using Digital Element's IP intelligence data within AI workflows. These prompts help data scientists, security analysts, and ecommerce managers extract actionable insights from Geolocation, Proxy, and VPN data.

---

## 🛡️ Use Case: Fraud & Risk Detection

### Prompt: Analyzing High-Risk Transactions
> **Context:** I have a list of IP addresses from recent ecommerce transactions.
> **Task:** Use the Digital Element `Nodify` data to categorize these IPs by risk. 
> **Instructions:** > - Identify if the IP is a **Residential Proxy** (often used for botting) vs. a **Corporate VPN**.
> - Flag IPs associated with **No-Log VPN providers** as "Manual Review Required."
> - Check for "Location Persistence"—if an IP has been seen in 5+ different cities in 24 hours, flag it as high-risk.
> - Output a summary table with: IP, Connection Type, Risk Level, and Reason.

---

## 🛒 Use Case: Ecommerce & Localization

### Prompt: Dynamic Content Personalization
> **Context:** A user is visiting our ecommerce store from IP [INSERT_IP].
> **Task:** Based on Digital Element `NetAcuity` data, determine the optimal UI localization.
> **Instructions:**
> - Identify the user's **Postal Code** and **DMA (Designated Market Area)**.
> - Suggest the nearest physical store location (Lat/Long).
> - Determine if the user is on a **Mobile Carrier** (e.g., 5G/LTE) and suggest whether to serve "Lightweight" vs. "High-Res" image assets.
> - Return the result in a JSON format suitable for a frontend API.

---

## 🎬 Use Case: Digital Rights Management (DRM)

### Prompt: Geo-Fencing & Compliance
> **Context:** Our streaming service only has licensing rights for [REGION/COUNTRY].
> **Task:** Evaluate incoming traffic for compliance.
> **Instructions:**
> - Is the IP categorized as a **VPN Exit Node**? 
> - If it is a VPN, can we identify the provider? (Exclude "Verified Corporate VPNs" for employees).
> - Use "Historical IP Lookback" to see if the user’s location has "teleported" (impossible travel) across countries recently.
> - Provide a "Confidence Score" (0-100) on whether the user is physically located in the declared region.

---

## 📊 Use Case: Marketing Analytics & Attribution

### Prompt: B2B vs. B2C Traffic Breakdown
> **Context:** Analyzing web traffic logs for the last 30 days.
