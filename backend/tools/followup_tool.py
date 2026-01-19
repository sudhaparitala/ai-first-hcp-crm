def generate_followup(hcp_name: str):
    """
    Suggests next follow-up action.
    """
    return {
        "hcp": hcp_name,
        "suggestion": "Schedule follow-up visit in 2 weeks"
    }