def adjusted_score(module, score):
    module = module.lower()

    # Increase risk for sensitive modules
    if "payment" in module:
        score = score * 1.5
    elif "authentication" in module:
        score = score * 1.4
    elif "security" in module:
        score = score * 1.3

    return round(score)


def priority_score(risk_level):

    if risk_level == "High":
        return "Test First"

    elif risk_level == "Medium":
        return "Test Soon"

    else:
        return "Test Later"