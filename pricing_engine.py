import json
import pprint
from pricing_logic.template_lookup import get_template_for_task
from utils.parser import extract_tasks_from_transcript
from utils.helpers import apply_margin, get_confidence_score, adjust_city_factor

TRANSCRIPT = """Client wants to renovate a small 4m² bathroom. 
They’ll remove the old tiles, redo the plumbing for the shower, 
replace the toilet, install a vanity, repaint the walls, 
and lay new ceramic floor tiles. Budget-conscious. Located in Marseille."""

def generate_quote(transcript):
    tasks = extract_tasks_from_transcript(transcript)
    location = "Marseille"  # Could be extracted automatically
    quote = {
        "zone": "Bathroom",
        "location": location,
        "tasks": [],
        "global_confidence_score": 0
    }

    task_confidences = []

    for task in tasks:
        print(f"🔍 Processing task: {task}")
        template = get_template_for_task(task)

        if not template:
            print(f"❌ No pricing template found for task: {task}")
            quote["tasks"].append({
                "task": task,
                "error": "No pricing template found"
            })
            continue

        labor_cost = template['labor_hours'] * template['hourly_rate']
        base_price = labor_cost + template['material_cost']
        price_with_margin = apply_margin(base_price, template['margin'])
        final_price = adjust_city_factor(price_with_margin, location)

        confidence = template['confidence_score']
        task_confidences.append(confidence)

        quote["tasks"].append({
            "task": task,
            "labor_cost": round(labor_cost, 2),
            "material_cost": template['material_cost'],
            "estimated_duration_hours": template['labor_hours'],
            "vat_rate": template['vat_rate'],
            "margin": template['margin'],
            "total_price": round(final_price, 2),
            "confidence_score": confidence
        })

    if task_confidences:
        quote["global_confidence_score"] = round(sum(task_confidences) / len(task_confidences), 2)

    # Debug print the full quote before saving
    print("\n📦 Final Quote:")
    pprint.pprint(quote)

    # Save the file and catch any potential errors
    try:
        with open("output/sample_quote.json", "w") as f:
            json.dump(quote, f, indent=4)
        print("✅ Quote generated and saved to output/sample_quote.json")
    except Exception as e:
        print(f"❌ Failed to save quote: {e}")

if __name__ == "__main__":
    generate_quote(TRANSCRIPT)
