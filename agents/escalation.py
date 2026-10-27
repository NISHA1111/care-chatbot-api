def decide_action(category, faq_result=None):
    """
    Decides the safest action based on the classified category.
    """

    if category == "emergency":
        return "EMERGENCY_ESCALATE"

    if category == "medical":
        return "REFUSE_AND_ESCALATE"

    if category == "complaint":
        return "ESCALATE"

    if category == "prompt_injection":
        return "REFUSE"

    if category == "unclear":
        return "CLARIFY"

    if category == "unsupported":
        return "ESCALATE"

    if category == "faq":
        if faq_result and faq_result.get("match_found"):
            return "ANSWER"
        return "CLARIFY"

    return "ESCALATE"