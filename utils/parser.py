def extract_tasks_from_transcript(transcript):
    # Naive keyword matching; can be replaced with LLM or NLP parser
    known_tasks = [
        "remove the old tiles",
        "redo the plumbing for the shower",
        "replace the toilet",
        "install a vanity",
        "repaint the walls",
        "lay new ceramic floor tiles"
    ]
    return known_tasks
