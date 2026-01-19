def edit_interaction(interaction_id: int, updated_notes: str):
    """
    Edits an existing interaction.
    """
    return {
        "status": "updated",
        "interaction_id": interaction_id,
        "notes": updated_notes
    }
