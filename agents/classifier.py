def classify_message(message):
    """
    Classifies the user's message into one support category.
    """

    text = message.lower()

    # Prompt injection
    if (
        "ignore previous instructions" in text
        or "ignore all previous instructions" in text
        or "system prompt" in text
        or "hidden prompt" in text
        or "internal policies" in text
    ):
        return "prompt_injection"

    # Emergency
    emergency_keywords = [
        "unconscious",
        "heavy bleeding",
        "not breathing",
        "can't breathe",
        "cannot breathe",
        "severe chest pain",
        "life threatening"
    ]

    for keyword in emergency_keywords:
        if keyword in text:
            return "emergency"

    # Medical advice / diagnosis
    medical_keywords = [
        "what medicine",
        "which medicine",
        "diagnose",
        "heart attack",
        "what treatment",
        "what should i take",
        "medical advice"
    ]

    for keyword in medical_keywords:
        if keyword in text:
            return "medical"

    # Complaints
    complaint_keywords = [
        "payment failed",
        "paid but",
        "charged more",
        "very late",
        "nobody is responding",
        "driver problem",
        "booking failed"
    ]

    for keyword in complaint_keywords:
        if keyword in text:
            return "complaint"

    # Unclear / vague messages
    unclear_messages = [
        "help",
        "i need help",
        "help me",
        "my ambulance is not coming"
    ]

    if text.strip() in unclear_messages:
        return "unclear"

    # FAQ-related keywords
    faq_keywords = [
        "book",
        "booking",
        "ambulance type",
        "ambulance types",
        "price",
        "pricing",
        "fare",
        "cost",
        "track",
        "tracking",
        "eta",
        "cancel",
        "cancellation",
        "payment",
        "schedule",
        "account",
        "location",
        "support"
    ]

    for keyword in faq_keywords:
        if keyword in text:
            return "faq"

    # If nothing matches
    return "unsupported"