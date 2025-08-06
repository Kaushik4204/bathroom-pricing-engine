import pandas as pd

# Load the template CSV once
df = pd.read_csv("data/price_templates.csv")

def get_template_for_task(task):
    task_lower = task.lower()

    # 1. Try exact keyword match as substring
    for _, row in df.iterrows():
        if row['task_keyword'].lower() in task_lower:
            print(f"✅ Matched task: '{task}' with keyword: '{row['task_keyword']}'")
            return row.to_dict()

    # 2. Try partial word match (word overlap)
    task_words = set(task_lower.split())
    for _, row in df.iterrows():
        keyword_words = set(row['task_keyword'].lower().split())
        if keyword_words & task_words:  # if there's any word overlap
            print(f"✅ Fuzzy matched task: '{task}' with keyword: '{row['task_keyword']}'")
            return row.to_dict()

    # 3. No match found
    print(f"❌ No pricing template found for task: {task}")
    return None
