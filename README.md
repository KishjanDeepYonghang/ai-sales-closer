# Omnichannel AI Sales & Inbound Lead Qualifier

A production-ready conversational pipeline connecting Meta (WhatsApp/Instagram) webhooks to Supabase and CRM systems for automated lead qualification and instant customer inquiry handling.

## 🎯 Business Value
- **24/7 Sales Pipeline:** Never miss a lead on social media or WhatsApp.
- **High Conversion Rate:** State-machine logic prevents the LLM from endlessly chatting without driving toward a sale.
- **Accurate Catalog Specs:** Queries Supabase directly to provide verified product specs and pricing with zero hallucinations.
- **Single Source of Truth:** Bi-directional CRM syncing ensures the sales team has full visibility.

## 🏗️ System Architecture

```mermaid
sequenceDiagram
    participant Customer
    participant Meta as WhatsApp / IG
    participant App as FastAPI Webhook
    participant Funnel as Sales State Machine
    participant DB as Supabase (Catalog & Leads)
    participant CRM as HubSpot / CRM

    Customer->>Meta: "Is this still available?"
    Meta->>App: POST Webhook Payload
    App->>Funnel: Process Intent & State
    Funnel->>DB: Query Live Inventory & Specs
    DB-->>Funnel: Return Product Record
    Funnel-->>App: "Yes! Here are the specs & EMI options..."
    App->>Meta: Send Instant WhatsApp Reply
    App->>CRM: Upsert Lead & Interaction Sentiment
```

## 🛠️ Tech Stack

- **Core:** Python 3.11, FastAPI

- **Integrations:** Twilio, Meta Graph API, HubSpot API

- **Infrastructure:** Docker, Redis (for session state)


## 🚀 Quick Start

```bash

docker-compose up --build

```



## Connect with Me



- **Portfolio:** [kishjandeepyonghang.me](https://kishjandeepyonghang.me)

- **LinkedIn:** [Kishjan Deep Yonghang](https://www.linkedin.com/in/kishjan-yonghang-b6a324430/)

- **Facebook:** [Kishjan Deep Yonghang](https://www.facebook.com/profile.php?id=61575446859939)

- **WhatsApp:** [+977-9815972075](https://wa.me/9779815972075)

- **Email:** yonghangkishjan608@gmail.com

