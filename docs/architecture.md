# System Architecture: IP Intelligence Pipeline

This document describes the high-level architecture of the Digital Element IP Intelligence integration. It provides a blueprint for how data flows from raw IP discovery to actionable business logic (Fraud Prevention and Ecommerce Localization).

## Data Flow Overview

The following diagram illustrates the lifecycle of an IP intelligence request:

```mermaid
graph TD
    A[End User / Request] -->|IP Address| B[Integration Layer]
    B --> C{Data Source}
    C -->|API/Flat File| D[NetAcuity: Geolocation]
    C -->|API/Flat File| E[Nodify: Proxy/VPN]
    
    D --> F[Logic Engine]
    E --> F
    
    F -->|Fraud Scoring| G[Security Gateway]
    F -->|Localization Data| H[UI/UX Controller]
    
    G -->|Block/Flag| I[Risk Management]
    H -->|Currency/Store| J[Personalized Web App]
