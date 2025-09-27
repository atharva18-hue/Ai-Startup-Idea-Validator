# utils.py - Dynamic SWOT Analyzer
import random

# Predefined SWOT keyword mapping
SWOT_KEYWORDS = {
    "AI": {
        "Strengths": ["AI-powered", "High scalability", "Automation capability"],
        "Weaknesses": ["Complex technology", "Requires expertise"],
        "Opportunities": ["AI market growth", "High investor interest"],
        "Threats": ["Competition", "Regulatory challenges"]
    },
    "Health": {
        "Strengths": ["Improves wellbeing", "Personalization"],
        "Weaknesses": ["Sensitive data required", "Compliance issues"],
        "Opportunities": ["Rising health awareness", "Telehealth adoption"],
        "Threats": ["Data privacy regulations", "Market competition"]
    },
    "Nutrition": {
        "Strengths": ["Personalized diet plans", "Health improvement"],
        "Weaknesses": ["Requires user input", "Limited datasets"],
        "Opportunities": ["Growing health-conscious market", "Fitness trend"],
        "Threats": ["Competition", "Regulatory requirements"]
    },
    "Education": {
        "Strengths": ["Adaptive learning", "Scalable knowledge delivery"],
        "Weaknesses": ["Dependence on digital literacy", "Content creation cost"],
        "Opportunities": ["E-learning market growth", "Online adoption increase"],
        "Threats": ["Competition", "User engagement challenges"]
    },
    "Travel": {
        "Strengths": ["Virtual guidance", "Cost saving"],
        "Weaknesses": ["Limited physical experience", "Requires AR/VR tech"],
        "Opportunities": ["Travel market expansion", "Remote tourism"],
        "Threats": ["Competition", "Tech limitations"]
    }
}

def analyze_idea(text):
    """
    Dynamic SWOT analysis based on keywords in the startup idea.
    """
    text = text.lower()
    swot_result = {"Strengths": [], "Weaknesses": [], "Opportunities": [], "Threats": []}

    for keyword, items in SWOT_KEYWORDS.items():
        if keyword.lower() in text:
            for key in swot_result:
                swot_result[key].extend(items[key])

    # If no keyword matched, return generic placeholder
    if all(len(v) == 0 for v in swot_result.values()):
        swot_result = {
            "Strengths": ["Innovative", "AI-powered"],
            "Weaknesses": ["Requires data", "Hardware dependency"],
            "Opportunities": ["Market gap", "Investors interest"],
            "Threats": ["Competition", "Regulatory risk"]
        }

    # Optional: randomly select up to 3 items per category for brevity
    for key in swot_result:
        if len(swot_result[key]) > 3:
            swot_result[key] = random.sample(swot_result[key], 3)

    return swot_result
