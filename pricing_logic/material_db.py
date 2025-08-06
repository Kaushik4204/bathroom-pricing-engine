import json

def get_material_cost(task):
    with open("data/materials.json") as f:
        material_db = json.load(f)
    
    for keyword, details in material_db.items():
        if keyword.lower() in task.lower():
            return {"cost": details["cost"], "name": keyword}
    return {"cost": 0, "name": "N/A"}
