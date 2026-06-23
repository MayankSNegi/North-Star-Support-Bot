# North Star Support Bot 🏕️

## Project Overview

North Star Support Bot is a customer support chatbot designed for a small e-commerce business specializing in outdoor apparel and camping gear.

The chatbot provides quick and friendly assistance for common customer support inquiries, including order tracking, returns and exchanges, product recommendations, shipping information, and live agent handoff.

Built with Python and Streamlit, the chatbot demonstrates conversational flow design, intent recognition, state management, and customer support automation.

---

## Features

### 📦 Order Tracking

Users can track orders by providing an order number.

Supported mock orders:

| Order Number | Status                        |
| ------------ | ----------------------------- |
| 111          | Shipped, arriving tomorrow    |
| 222          | Processing, ships in 24 hours |
| 333          | Delivered                     |

Invalid order numbers are handled with a friendly error message.

---

### ↩️ Returns & Exchanges

Provides return policy information:

* 30-day returns
* Item must be unused
* Original packaging required

Returns link:

https://northstaroutdoors.com/returns

---

### 🎒 Product Recommendations

The chatbot asks clarifying questions before recommending products.

Supported recommendation flows:

* Camping → Camping Tents
* Hiking → Hiking Apparel and Daypacks
* Backpacking → Lightweight Backpacking Gear

---

### 👨‍💼 Human Handoff

Users can request assistance from a live agent at any time.

The chatbot collects:

* Name
* Email
* Brief Issue Description

The request is then forwarded to a simulated live agent queue.

---

### 🚚 Shipping Information

Provides shipping options and estimated delivery times.

* Standard Shipping: 3–5 business days
* Expedited Shipping: 1–2 business days

---

### ❓ Fallback Handling

When the chatbot cannot understand a request, it:

* Informs the user
* Displays available support options
* Guides the user back to the main conversation flow

---

## Technologies Used

* Python 3
* Streamlit
* State-Based Conversation Management

---

## Project Structure

```text
North-Star-Support-Bot/
│
├── chatbot/
│   ├── __init__.py
│   ├── conversation.py
│   ├── intents.py
│   ├── order_data.py
│   └── responses.py
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd North-Star-Support-Bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the chatbot:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Usage

### Order Tracking

Example:

```text
Track my order
222
```

Response:

```text
Order #222

Status: Processing, ships in 24 hours
```

---

### Returns & Exchanges

Example:

```text
I want to return an item
```

Response:

```text
Returns & Exchanges

30-day returns
Unused items only
Original packaging required
```

---

### Product Recommendation

Example:

```text
Recommend camping gear
Hiking
Multi-Day Trips
```

Response:

```text
Based on your needs, I recommend our Hiking Apparel and Daypack categories.
```

---

### Human Handoff

Example:

```text
I want a human agent
```

Response:

```text
Please provide:
- Name
- Email
- Brief Issue Description
```

---

## Demo Scenarios

### Scenario 1 – Order Tracking

Input:

```text
Track my order
111
```

Expected Output:

```text
Shipped, arriving tomorrow
```

---

### Scenario 2 – Returns & Exchanges

Input:

```text
Return item
```

Expected Output:

```text
30-day returns
Unused items only
Original packaging required
```

---

### Scenario 3 – Product Recommendations

Input:

```text
Recommend camping gear
Backpacking
Yes
```

Expected Output:

```text
Lightweight Backpacking Gear category
```

---

### Scenario 4 – Human Handoff

Input:

```text
Human agent
```

Expected Output:

```text
Live Agent handoff process initiated
```

---

### Scenario 5 – Shipping Information

Input:

```text
Shipping
Standard Shipping
```

Expected Output:

```text
Delivery Time: 3–5 business days
```

---

### Scenario 6 – Fallback Handling

Input:

```text
Tell me a joke
```

Expected Output:

```text
Sorry, I didn't understand that.
```

---

## Future Improvements

* Integration with real e-commerce APIs
* Database-backed order tracking
* Live chat integration
* Natural Language Processing (NLP)
* User authentication
* Email notifications

---

## Author

[Mayank Singh Negi](https://github.com/MayankSNegi)
