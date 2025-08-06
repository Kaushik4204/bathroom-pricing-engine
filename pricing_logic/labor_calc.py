def estimate_labor(task):
    hourly_rate = 30
    task_hours = {
        "remove tiles": 4,
        "plumbing": 5,
        "replace toilet": 2,
        "install vanity": 3,
        "paint": 3,
        "lay tiles": 4
    }

    for keyword, hours in task_hours.items():
        if keyword in task.lower():
            return {"hours": hours, "cost": hours * hourly_rate}
    return {"hours": 2, "cost": 2 * hourly_rate}
