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


---

## 🛠️ How to Run the Code

### Prerequisites

- Python 3.7+
- `pip install -r requirements.txt` (if using external libraries like `fuzzywuzzy`)

### Run Locally

```bash
git clone https://github.com/Kaushik4204/bathroom-pricing-engine.git
cd bathroom-pricing-engine

python pricing_engine.py
```

##  Output JSON Schema
The system outputs an itemized JSON file: output/sample_quote.json


```json
{
  "zone": "Bathroom",
  "location": "Marseille",
  "tasks": [
    {
      "task": "replace the toilet",
      "labor_cost": 60.0,
      "material_cost": 70,
      "estimated_duration_hours": 1.5,
      "vat_rate": 0.2,
      "margin": 0.2,
      "total_price": 156.0,
      "confidence_score": 0.9
    },
    ...
  ],
  "global_confidence_score": 0.87
}
```
---

Each task includes:

📦 material_cost: From materials.json

👷 labor_cost: labor_hours × hourly_rate

⏱ estimated_duration_hours: From template

💸 vat_rate: From vat_rules.py (location + type)

📈 margin: From template

💰 total_price: (labor + material) * (1 + margin) * (1 + VAT)

🧠 confidence_score: Indicates pricing template relevance

## Pricing & Margin Logic
Each task uses a pricing template (data/price_templates.csv) that defines:

Typical labor time

Hourly labor cost

Material cost

Default profit margin

Confidence in accuracy

Price Calculation Formula

base_price = labor_cost + material_cost

with_margin = base_price * (1 + margin)

final_price = with_margin * (1 + VAT) * city_factor

Note - City Factor is an adjustment multiplier (e.g., 1.1 for expensive cities).

---

## Assumptions & Edge Cases
If a task is not matched, an error is logged in JSON.

City adjustment uses hardcoded city factors (can be improved).

Confidence scoring is rule-based (can use ML in future).

VAT is uniform per task; in reality, some may be exempt or different.

Transcript parsing is based on keyword extraction (extendable to NLP).



