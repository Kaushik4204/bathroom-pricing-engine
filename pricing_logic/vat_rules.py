def get_vat_rate(task, city="Marseille"):
    """
    Returns VAT rate based on task and optionally city.
    """
    if "plumbing" in task.lower() or "toilet" in task.lower():
        return 10
    return 20
