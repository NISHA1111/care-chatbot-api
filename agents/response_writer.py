def write_response(faq_result):
    """
    Converts a matched FAQ result into a clean chatbot response.
    """

    if not faq_result.get("match_found"):
        return "I’m sorry, I couldn’t find a reliable answer for that. Please contact Care support for help."

    answer = faq_result.get("answer")

    return f"Here’s what I found: {answer}"