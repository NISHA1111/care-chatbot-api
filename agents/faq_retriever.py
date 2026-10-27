import json
import os
import re


STOP_WORDS = {
    "a", "an", "the", "is", "are", "do", "does", "did",
    "i", "me", "my", "you", "your", "we", "our",
    "can", "could", "should", "would",
    "how", "what", "where", "when", "why",
    "to", "for", "of", "in", "on", "at", "with",
    "and", "or", "be", "am", "was", "were"
}


SYNONYM_GROUPS = [
    {"cost", "price", "pricing", "fare", "charge"},
    {"book", "booking", "reserve", "request"},
    {"cancel", "cancellation"},
    {"track", "tracking", "location"},
    {"eta", "arrival", "time"},
    {"pay", "payment"},
    {"ambulance", "vehicle"},
    {"schedule", "advance", "future"}
]


def load_faqs():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    faq_path = os.path.join(project_root, "data", "faq_dataset.json")

    with open(faq_path, "r", encoding="utf-8") as file:
        return json.load(file)


def normalize_words(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return {
        word for word in words
        if word not in STOP_WORDS
    }


def expand_synonyms(words):
    expanded = set(words)

    for group in SYNONYM_GROUPS:
        if words.intersection(group):
            expanded.update(group)

    return expanded


def retrieve_faq(user_message):
    faqs = load_faqs()

    user_words = normalize_words(user_message)
    user_words = expand_synonyms(user_words)

    best_match = None
    best_score = 0

    for faq in faqs:
        faq_words = normalize_words(faq["question"])
        faq_words = expand_synonyms(faq_words)

        shared_words = user_words.intersection(faq_words)
        score = len(shared_words)

        if score > best_score:
            best_score = score
            best_match = faq

    if best_match and best_score > 0:
        return {
            "match_found": True,
            "faq_id": best_match["id"],
            "question": best_match["question"],
            "answer": best_match["answer"],
            "score": best_score
        }

    return {
        "match_found": False,
        "faq_id": None,
        "question": None,
        "answer": None,
        "score": 0
    }