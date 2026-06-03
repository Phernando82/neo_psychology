# Personality Inventory — Web Application

Structured data capture · Django · ReportLab · PDF generation pipeline

---

## Overview

Web application built with Django that delivers a 240-question personality inventory form, captures structured responses, and generates a formatted PDF report on demand — without storing sensitive user data server-side beyond the active session. Demonstrates form validation at scale, session-based state management, and server-side document generation: patterns directly transferable to industrial data collection systems, operator checklists, and audit report pipelines in Industry 4.0 environments.

---

## Technical Highlights

**Large-scale form handling (240 fields)**
Django form pipeline validates, sanitizes, and processes 240 discrete inputs in a single submission cycle. Demonstrates robust server-side validation and structured data binding — equivalent to batch parameter ingestion from industrial configuration interfaces or operator inspection forms.

**Session-based state management**
User responses are tracked across the form lifecycle using Django's session framework, keeping sensitive data out of the database while maintaining continuity across page interactions. Mirrors stateful session handling in industrial HMI workflows.

**Server-side PDF generation**
On form submission, a formatted PDF report is assembled server-side and delivered as a file download — no client-side rendering dependency. The same pipeline applies to automated report generation in SCADA systems, maintenance work orders, and audit trail exports.

**Structured data-to-document pipeline**
Raw form responses are mapped to a defined document schema before rendering. Enforces output consistency regardless of input variation — the same concern found in industrial data historians exporting to standardized formats (CSV, XML, PDF) for MES/ERP integration.

**Django MVT architecture**
Clean separation between data models, business logic, and presentation layer. Facilitates maintenance and extension — adding new question sets, output formats, or scoring logic requires no changes to unrelated components.

---

## Stack

Python 3.x · Django · ReportLab · HTML/CSS · SQLite / PostgreSQL

---

## Installation

```bash
git clone https://github.com/YOUR_USER/personality-inventory
cd personality-inventory
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Access at: `http://localhost:8000`

---

## Workflow

```
User accesses the form
        │
        ▼
   240-question inventory rendered (Django form)
        │
        ▼
   Client-side progress tracking
        │
        ▼
   Form submission → server-side validation (Django)
        │
        ├── Validation errors → form re-rendered with feedback
        │
        └── Valid → responses bound to document schema
                        │
                        ▼
                PDF assembled server-side (ReportLab)
                        │
                        ▼
                File delivered to user (download)
```

---

## Relevance to Industry 4.0

The data capture → validate → structure → generate document pipeline demonstrated here maps directly to industrial workflows:

- **Large-scale structured form handling** → digital operator checklists, pre-shift inspection forms, equipment commissioning records replacing paper-based processes in smart factories
- **Server-side PDF generation** → automated work order generation, maintenance reports, calibration certificates, and audit trail exports in CMMS and ERP systems
- **Session state management** → multi-step configuration wizards in industrial HMI/SCADA interfaces where operator input spans multiple screens
- **Data-to-document schema enforcement** → standardized output for regulatory compliance reports (ISO, IEC) or MES/ERP data exchange formats

---

## License

MIT · No personally identifiable data is persisted beyond the active user session.
