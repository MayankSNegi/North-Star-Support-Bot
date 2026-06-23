def detect_intent(message):
    message = message.lower()

    if any(word in message for word in [
        "order",
        "track",
        "package",
        "shipment",
        "status"
    ]):
        return "order"

    if any(word in message for word in [
        "return",
        "refund",
        "exchange",
        "returns"
    ]):
        return "returns"

    if any(word in message for word in [
        "recommend",
        "suggest",
        "camping",
        "hiking",
        "backpacking"
    ]):
        return "recommendation"

    if any(word in message for word in [
        "agent",
        "human",
        "representative",
        "support"
    ]):
        return "handoff"

    if any(word in message for word in [
        "shipping",
        "delivery",
        "ship",
        "shipping time",
        "delivery time"
    ]):
        return "shipping"
    return "fallback"
    