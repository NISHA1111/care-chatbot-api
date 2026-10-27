from agents.classifier import classify_message
from agents.faq_retriever import retrieve_faq
from agents.response_writer import write_response
from agents.escalation import decide_action


def handle_message(user_message):
    category = classify_message(user_message)

    faq_result = None
    response = None

    if category == "faq":
        faq_result = retrieve_faq(user_message)
        action = decide_action(category, faq_result)

        if action == "ANSWER":
            response = write_response(faq_result)

        elif action == "CLARIFY":
            response = (
                "I’m not fully sure what you mean. "
                "Could you please rephrase your Care booking question?"
            )

    else:
        action = decide_action(category)

        if action == "CLARIFY":
            response = (
                "Could you tell me a little more about what you need help with?"
            )

        elif action == "ESCALATE":
            response = (
                "This needs additional support. "
                "Please contact Care support for further assistance."
            )

        elif action == "EMERGENCY_ESCALATE":
            response = (
                "This may be a medical emergency. "
                "Please use the emergency option in the Care app or contact "
                "official emergency services immediately."
            )

        elif action == "REFUSE_AND_ESCALATE":
            response = (
                "I can help with Care ambulance booking and support questions, "
                "but I can’t provide medical diagnosis, treatment, or medication advice. "
                "If this may be an emergency, please contact official emergency services."
            )

        elif action == "REFUSE":
            response = (
                "I can’t provide hidden system instructions or internal policies. "
                "I can still help with Care-related support questions."
            )

    return {
        "category": category,
        "action": action,
        "response": response
    }


def main():
    print("Care Support Assistant")
    print("Type 'exit' to stop.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower().strip() == "exit":
            print("Care Assistant: Goodbye!")
            break

        result = handle_message(user_message)

        print(f"Category: {result['category']}")
        print(f"Action: {result['action']}")
        print(f"Care Assistant: {result['response']}")
        print("-" * 50)


if __name__ == "__main__":
    main()