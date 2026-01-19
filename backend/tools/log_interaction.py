def log_interaction(notes: str):
    """
    Captures and summarizes HCP interaction notes.
    """
    return {
        "status": "success",
        "summary": notes,
        "hcp_name": "Dr. Sample",
        "interaction_type": "Visit"
    }
