# RecallOps

### AI Incident Response with Persistent Organizational Memory

RecallOps is an AI-powered incident investigation system that uses **Hindsight** to remember how an organization handled previous production incidents.

Instead of treating every incident as a completely new problem, RecallOps retrieves relevant historical experiences, reasons over the current incident together with that memory, and recommends a resolution while keeping the engineer in control.

---

## 🚨 The Problem

Production incidents are often repetitive.

Teams may have already experienced:

- Similar database failures
- Connection pool exhaustion
- Deployment-related outages
- Cache failures
- Service-specific failure patterns
- Previous fixes that successfully restored the system

But that knowledge is often scattered across incident tickets, post-mortems, Slack messages, runbooks, and engineers' experience.

A conventional AI assistant can analyze the **current** incident.

The missing piece is:

> **What did our organization learn the last time this happened?**

---

## 💡 The Solution

RecallOps makes organizational memory part of the incident-response workflow.

```text
Production Incident
        ↓
Hindsight Recall
        ↓
Relevant Historical Experience
        ↓
Reason Over Current Incident + Memory
        ↓
AI Recommendation
        ↓
Engineer Reviews / Approves
        ↓
Incident Resolved
        ↓
Store Resolution in Hindsight
        ↓
Future Incidents Reuse the Experience
```

The key idea is simple:

> **RecallOps doesn't just investigate incidents. It remembers how the organization solved them.**

---

## 🧠 Why Hindsight Matters

Hindsight is the persistent memory layer of RecallOps.

It allows the system to:

1. Store previous incident experiences
2. Retrieve relevant historical incidents
3. Use those memories during new investigations
4. Learn from newly resolved incidents
5. Make future recommendations using accumulated organizational knowledge

This creates a continuous memory loop:

```text
Past Incident
     ↓
Resolution
     ↓
Hindsight Memory
     ↓
Future Incident
     ↓
Better Investigation
     ↓
New Resolution
     ↓
Updated Memory
```

As more incidents are resolved and remembered, the system builds an organizational memory of production failures and their resolutions.

---

# 🎬 Demo

RecallOps demonstrates the complete memory-powered incident-response workflow.

## 1. New Production Incident

A critical incident occurs in `payment-api`.

The system detects:

- HTTP error rate: 31%
- Latency: 4.5 seconds
- Database connection pool exhaustion
- Recent deployment: `v4.1.4`

![Current Incident](docs/screenshots/01-current-incident.png)

---

## 2. Hindsight Recalls Previous Experience

RecallOps searches organizational memory and retrieves a relevant historical incident.

The system finds `INC-029`, a previous `payment-api` incident involving:

- Database connection exhaustion
- A recent deployment
- Similar failure behavior
- A successful rollback and worker restart

![Hindsight Memory](docs/screenshots/02-hindsight-memory.png)

The recommendation is therefore grounded not only in the current incident, but also in **what the organization successfully did before**.

---

## 3. AI Recommendation

RecallOps combines the current incident with the retrieved organizational memory.

The system recommends:

> Roll back deployment `v4.1.4` and restart payment workers.

The recommendation includes supporting evidence and an alternative investigation path.

The engineer remains responsible for approving the action.

---

## 4. Resolution Becomes New Memory

After the engineer approves the resolution, the incident is resolved.

RecallOps then stores the outcome in Hindsight.

![Recommendation and Learning](docs/screenshots/03-recommendation-and-learning.png)

The next incident can now reuse this newly learned experience.

---

# 🔁 The Memory Loop

```text
New Incident
     ↓
Hindsight Recall
     ↓
Relevant Past Experience
     ↓
AI Reasoning
     ↓
Recommendation
     ↓
Engineer Decision
     ↓
Resolution
     ↓
Hindsight Learns
     ↓
Better Future Investigations
```

This is the core of RecallOps.

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   Production Incident │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     RecallOps API    │
                    │       FastAPI        │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   Hindsight Recall   │
                    │                      │
                    │ Historical incidents │
                    │ Previous resolutions │
                    │ Organizational memory│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    AI Reasoning      │
                    │                      │
                    │ Current incident +   │
                    │ historical memory    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Recommendation    │
                    │                      │
                    │ Action               │
                    │ Confidence           │
                    │ Evidence             │
                    │ Alternative           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Engineer Approval  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Incident Resolution │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Hindsight Memory  │
                    │      Updated        │
                    └──────────────────────┘
```

---

# 🔧 Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite |
| Backend | Python + FastAPI |
| Memory | Hindsight Cloud |
| API Client | Hindsight Python Client |
| Environment | Python virtual environment |
| Styling | CSS |
| Version Control | Git + GitHub |

---

# 📁 Project Structure

```text
recallops/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── ...
│   ├── package.json
│   └── ...
│
├── docs/
│   └── screenshots/
│       ├── 01-current-incident.png
│       ├── 02-hindsight-memory.png
│       └── 03-recommendation-and-learning.png
│
├── main.py
├── recallops_agent.py
├── seed_incidents.py
├── new_incident_test.py
├── reasoning_test.py
├── recall_test.py
├── resolve_incident.py
├── test_hindsight.py
├── README.md
├── .gitignore
└── .env
```

`.env` is intentionally excluded from Git.

---

# 🚀 Running RecallOps Locally

## 1. Clone the repository

```bash
git clone https://github.com/codeguy-srihas/recallops.git
cd recallops
```

## 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Python dependencies

```bash
pip install hindsight-client python-dotenv fastapi uvicorn
```

## 4. Configure environment variables

Create a `.env` file:

```env
HINDSIGHT_API_KEY=your_hindsight_api_key
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
HINDSIGHT_BANK_ID=Recallops
```

Never commit the `.env` file.

---

# ▶️ Start the Backend

From the project root:

```bash
source venv/bin/activate
uvicorn main:app --reload
```

The API runs locally on:

```text
http://127.0.0.1:8000
```

---

# 🌐 Start the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend runs locally on:

```text
http://localhost:5173
```

Keep both the backend and frontend running during the demo.

---

# 🔌 API Endpoints

## Health Check

```text
GET /
```

Checks whether the RecallOps backend is running.

## Investigate Incident

```text
GET /investigate?incident_id=INC-030
```

Investigates the incident using current incident information and historical Hindsight memories.

## Resolve Incident

```text
GET /resolve?incident_id=INC-030
```

Records the approved resolution and updates organizational memory.

---

# 🧪 Demo Scenario

The primary demonstration uses `INC-030`.

### Current Incident

```text
Incident: INC-030
Service: payment-api
Severity: CRITICAL
HTTP Errors: 31%
Latency: 4.5 seconds
Deployment: v4.1.4
Failure: Database connection pool exhausted
```

### Retrieved Organizational Memory

```text
Historical Incident: INC-029
Service: payment-api
Failure: Database connection exhaustion
Deployment: v4.1.3

Previous resolution:
Rollback deployment + restart payment workers
```

### Recommendation

```text
Roll back deployment v4.1.4
and restart payment workers.
```

### Human Decision

The engineer reviews the evidence and approves the proposed resolution.

### Learning

The final resolution is stored in Hindsight and becomes available to future investigations.

---

# 👤 Human-in-the-Loop

RecallOps is designed as a **decision-support system**, not an autonomous production deployment system.

The workflow is:

```text
Investigate
    ↓
Retrieve Memory
    ↓
Recommend
    ↓
Engineer Reviews
    ↓
Engineer Approves
    ↓
Resolve
    ↓
Learn
```

The engineer remains responsible for production actions.

This allows the system to provide useful historical context while keeping operational control with the human operator.

---

# 🎯 Why RecallOps

Traditional incident assistants primarily reason from:

```text
Current incident
+
General knowledge
```

RecallOps adds:

```text
Current incident
+
Organizational memory
+
Previous successful resolutions
```

This allows the agent to use the organization's own operational history as part of its reasoning process.

The value compounds as more incidents are resolved and remembered.

---

# 📈 Learning Over Time

Imagine an organization experiencing repeated production incidents.

### Incident 1

```text
Payment API
Database connection exhaustion
        ↓
Rollback deployment
```

### Incident 2

```text
Similar payment API failure
        ↓
Recall previous incident
        ↓
Recommend rollback
```

### Incident 3

```text
Another related failure
        ↓
Recall multiple historical experiences
        ↓
Compare previous resolutions
        ↓
Generate evidence-backed recommendation
```

The organization's operational experience becomes reusable knowledge.

---

# 🛡️ Scope and Limitations

RecallOps is intentionally focused on one workflow:

> **Production incident investigation using organizational memory.**

The current prototype uses realistic synthetic incident data rather than connecting to a live production monitoring platform.

It is designed to demonstrate the memory-powered workflow:

```text
Incident
   ↓
Recall
   ↓
Reason
   ↓
Recommend
   ↓
Resolve
   ↓
Learn
```

A production deployment could integrate with monitoring, observability, deployment, ticketing, and incident-management systems.

---

# 🔮 Future Extensions

Potential production extensions include:

- Integration with PagerDuty
- Integration with Slack incident channels
- Integration with GitHub deployments
- Integration with Kubernetes
- Integration with Prometheus/Grafana
- Automatic incident timeline construction
- Post-mortem generation
- Runbook retrieval
- Multiple service dependency analysis
- Incident similarity scoring
- Team-specific operational memory
- Approval workflows
- Incident analytics
- Recurring failure detection

---

# 🧠 Hindsight Memory Workflow

RecallOps uses Hindsight as the persistent memory layer for the agent.

Conceptually:

```text
RETAIN
  ↓
Store incident experience
  ↓
RECALL
  ↓
Retrieve relevant historical experience
  ↓
REFLECT
  ↓
Reason using current context + memory
  ↓
Store the outcome
  ↓
Future investigations reuse the experience
```

This creates a continuously evolving organizational memory.

---

# 📸 Demo Screenshots

## Current Production Incident

![Current Incident](docs/screenshots/01-current-incident.png)

## Hindsight Memory Retrieval

![Hindsight Memory](docs/screenshots/02-hindsight-memory.png)

## Recommendation → Resolution → Learning

![Recommendation and Learning](docs/screenshots/03-recommendation-and-learning.png)

---

# 👨‍💻 Project

**RecallOps**

AI incident response powered by persistent organizational memory using Hindsight.

---

## 📜 License

This project is currently a prototype.