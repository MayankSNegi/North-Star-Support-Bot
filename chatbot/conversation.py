from chatbot.intents import detect_intent
from chatbot.order_data import ORDERS
from chatbot.responses import (
    RETURN_POLICY,
    FALLBACK_MESSAGE
)

def process_message(message, state):

    message = message.strip()

    if state == "LIVE_AGENT":
        return (
            "Thank you.\n\n"
            "Your request has been forwarded to a Live Agent.\n\n"
            "A support representative will contact you shortly.",
            "MAIN_MENU"
        )
        
    # Global human handoff override
    if any(word in message.lower() for word in [
        "agent",
        "human",
        "representative",
        "support"
    ]):
        return (
            "I'll transfer you to a Live Agent.\n\n"
            "Please provide:\n"
            "- Name\n"
            "- Email\n"
            "- Brief Issue Description",
            "LIVE_AGENT"
        )

    # ----------------------
    # Waiting for Order Number
    # ----------------------
    if state == "WAITING_ORDER":

        if message in ORDERS:

            status = ORDERS[message]

            if message == "333":
                return (
                    "Order #333 has been delivered.\n\n"
                    "Did you receive your package successfully? (Yes/No)",
                    "ORDER_333_FOLLOWUP"
                )
    
            return (
                f"📦 Order #{message}\n\n"
                f"Status: {status}",
                "MAIN_MENU"
            )

        return (
            "❌ Invalid order number.\n\n"
            "Please check the number and try again, or request a Live Agent for assistance.",
            "MAIN_MENU"
        )

    # ----------------------
    # Delivered Follow-up
    # ----------------------
    if state == "ORDER_333_FOLLOWUP":

        if message.lower() == "yes":
            return (
                "Great! Glad everything arrived safely. 🏕️",
                "MAIN_MENU"
            )

        return (
            "I'm sorry to hear that.\n\n"
            "I'll connect you with a Live Agent.",
            "LIVE_AGENT"
        )

    # ----------------------
    # Product Recommendations
    # ----------------------
    if state == "RECOMMEND_ACTIVITY":

        if message.lower() in ["camping", "camp"]:
            return (
                "How many people will use the gear?\n\n"
                "- Solo\n- 2-4 People\n- Family",
                "RECOMMEND_CAMPING"
            )

        if message.lower() in ["hiking", "hike"]:
            return (
                "Are you planning Day Hikes or Multi-Day Trips?",
                "RECOMMEND_HIKING"
            )

        if message.lower() in ["backpacking", "backpack", "bag"]:
            return (
                "Are you looking for lightweight gear? (Yes/No)",
                "RECOMMEND_BACKPACKING"
            )

        return (
            "Please choose Camping, Hiking, or Backpacking.",
            "RECOMMEND_ACTIVITY"
        )

    if state == "RECOMMEND_CAMPING":
        return (
            "Based on your needs, I recommend exploring our Camping Tents category. 🏕️",
            "MAIN_MENU"
        )

    if state == "RECOMMEND_HIKING":
        return (
            "Based on your needs, I recommend our Hiking Apparel and Daypack categories. 🥾",
            "MAIN_MENU"
        )

    if state == "RECOMMEND_BACKPACKING":
        return (
            "Based on your needs, I recommend our Lightweight Backpacking Gear category. 🎒",
            "MAIN_MENU"
        )
        
    # ----------------------
    # Shipping Information
    # ----------------------
    if state == "SHIPPING_INFO":

        if "standard" in message.lower():
            return (
                "📦 Standard Shipping\n\n"
                "- Delivery Time: 3-5 business days",
                "MAIN_MENU"
            )

        if "expedited" in message.lower():
            return (
                "🚚 Expedited Shipping\n\n"
                "- Delivery Time: 1-2 business days",
                "MAIN_MENU"
            )

        return (
            "Please choose:\n\n"
            "- Standard Shipping\n"
            "- Expedited Shipping",
            "SHIPPING_INFO"
        )
        
    # ----------------------
    # Main Intent Detection
    # ----------------------
    intent = detect_intent(message)

    if intent == "order":
        return (
            "I'd be happy to help.\n\nPlease provide your order number.",
            "WAITING_ORDER"
        )

    if intent == "returns":
        return (
            RETURN_POLICY,
            "MAIN_MENU"
        )

    if intent == "recommendation":
        return (
            "What activity are you shopping for?\n\n"
            "- Camping\n- Hiking\n- Backpacking",
            "RECOMMEND_ACTIVITY"
        )

    if intent == "handoff":
        return (
            "I'll transfer you to a Live Agent.\n\n"
            "Please provide:\n"
            "- Name\n"
            "- Email\n"
            "- Brief Issue Description",
            "LIVE_AGENT"
        )
        
    if intent == "shipping":
        return (
            "📦 Shipping Information\n\n"
            "- Standard Shipping\n"
            "- Expedited Shipping\n\n"
            "Which shipping option are you interested in?",
            "SHIPPING_INFO"
        )

    return (
        FALLBACK_MESSAGE,
        "MAIN_MENU"
    )