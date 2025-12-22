# 📖 Glossary: IP Intelligence & Geolocation Terms

This glossary defines the key technical terms and data points used throughout this repository. Understanding these terms is essential for accurate fraud detection, ecommerce localization, and network analytics.

---

### 🌍 Geolocation Fundamentals

* **ASN (Autonomous System Number):** A unique identifier for a collection of IP networks managed by a single entity (e.g., an ISP, a university, or a large corporation). Helpful for identifying the "owner" of the traffic.
* **DMA (Designated Market Area):** A region where the population can receive the same local television and radio offerings. Crucial for media targeting and localized marketing.
* **Lat/Long (Latitude & Longitude):** The geographic coordinates of an IP. In Digital Element data, this represents the centroid of the identified location (e.g., city or postal code), not a specific street address.
* **Postal Code / Zip+4:** High-resolution geographic data used to target specific neighborhoods or calculate shipping logistics in ecommerce.

---

### 🛡️ Proxy & VPN Detection (Nodify)

* **Proxy Piercing:** The technical ability to "see through" a proxy or VPN to identify the true originating IP address or the actual location of the user.
* **Exit Node:** The point where internet traffic leaves a private network (like a VPN or Tor) and enters the public internet. This is the IP address seen by your web server.
* **Residential Proxy:** An IP address assigned by an ISP to a homeowner. These are highly valued by bots because they appear to be "real people" and are harder to block than data center IPs.
* **Darknet / Tor:** A network that anonymizes a user's IP by routing traffic through multiple layers. High-risk for ecommerce but vital for privacy in certain regions.
* **No-Log VPN:** A VPN service that claims not to keep records of user activity. These are frequently used by bad actors to hide their identity during fraudulent transactions.

---

### 💻 Connection & Intelligence

* **Connection Speed:** A classification of the user's bandwidth (e.g., Dial-up, Broadband, OC-3). Used to optimize content delivery (e.g., serving a low-res video to a mobile user).
* **Edge Node:** A server located at the "edge" of a network, close to the user, to reduce latency.
* **IP Intelligence:** The broader practice of extracting non-personal data from an IP address to determine its location, connection type, and risk profile.
* **Location Persistence:** A metric indicating how often an IP address is associated with a specific geographic location over time. Low persistence can indicate a mobile or rotating proxy.

---

### 🏢 Enterprise Data Fields

* **Home/Biz:** A classification indicating whether an IP is likely a residential home or a place of business.
* **Carrier ID:** The specific mobile network operator (e.g., Verizon, Vodafone, T-Mobile) providing the data connection.
* **NAICS Code:** (North American Industry Classification System) A code used to identify the industry type of the business associated with the IP address.
