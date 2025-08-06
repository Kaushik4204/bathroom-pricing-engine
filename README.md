# 🛁 Bathroom Pricing Engine

A smart Python-based pricing engine that transforms renovation transcripts into structured, itemized cost estimates. Built for contractors, homeowners, or fintech startups seeking transparent, fast, and scalable bathroom remodeling cost breakdowns.

---

## 🚀 Overview

This engine:
- Parses a **voice or text-based renovation transcript**
- Matches tasks using templates (via fuzzy logic)
- Estimates **labor**, **material costs**, **VAT**, and applies **profit margins**
- Supports **location-based price adjustments**
- Outputs a clean, structured **JSON quote**
- Provides **confidence scores** for pricing accuracy

---

## 📦 Repo Structure

bathroom-pricing-engine/
├── pricing_engine.py # Main execution script

├── pricing_logic/ # Modular logic components

│ ├── material_db.py

│ ├── labor_calc.py

│ └── vat_rules.py

├── utils/

│ ├── parser.py

│ └── helpers.py

├── data/

│ ├── materials.json # Raw materials database

│ └── price_templates.csv # Task-pricing templates

├── output/

│ └── sample_quote.json # Final structured output

├── tests/

│ └── test_logic.py # Logic validation tests

├── README.md 
