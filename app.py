import streamlit as st

from chatbot.conversation import process_message
from chatbot.responses import WELCOME_MESSAGE

st.set_page_config(
    page_title="North Star Support Bot",
    page_icon="🏕️"
)

st.title("🏕️ North Star Support Bot")

# Row 1
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📦 Track Order", use_container_width=True):
        st.session_state.quick_message = "track my order"

with col2:
    if st.button("↩️ Returns", use_container_width=True):
        st.session_state.quick_message = "return item"

with col3:
    if st.button("🎒 Recommendations", use_container_width=True):
        st.session_state.quick_message = "recommend camping gear"

# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    if st.button("👨‍💼 Live Agent", use_container_width=True):
        st.session_state.quick_message = "human agent"
   
with col5:
    if st.button("🚚 Shipping", use_container_width=True):
        st.session_state.quick_message = "shipping"
                
with col6:
    if st.button("🔄 Reset Chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": WELCOME_MESSAGE}
        ]
        st.session_state.state = "MAIN_MENU"
        st.rerun()
        
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": WELCOME_MESSAGE}
    ]

if "state" not in st.session_state:
    st.session_state.state = "MAIN_MENU"

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat_input = st.chat_input("Type your message...")

user_input = None

if "quick_message" in st.session_state:
    user_input = st.session_state.quick_message
    del st.session_state.quick_message

elif chat_input:
    user_input = chat_input
    
if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response, new_state = process_message(
        user_input,
        st.session_state.state
    )

    st.session_state.state = new_state

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()