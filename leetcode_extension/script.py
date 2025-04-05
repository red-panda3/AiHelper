import streamlit as st
from google import genai

# Initialize the Google GenAI client
client = genai.Client(api_key="AIzaSyAMrHhEcDZEHQSE3tJuGV-uPI66MTwYv1Q")

# Streamlit App Title
st.title("Multi-Line Conversation with Talk AI")

# Store conversation history in Session State
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# User Input
user_input = st.text_input("You:", key="input")
if st.button("Clear"):
   st.session_state.conversation = [] 
# Handle Empty Input
if user_input.strip() == "":
    st.warning("Please enter a valid prompt.")
else:
    # Process User Input and Generate Response
    if user_input:  # Ensure there's meaningful input
        try:
            # Generate AI response
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=user_input
            )
            ai_response = response.text

            # Append AI response to conversation history
            st.session_state.conversation.append(f"AI: {ai_response}")
             # Append user message to conversation history
            st.session_state.conversation.append(f"You: {user_input}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display the Conversation History
st.subheader("Conversation:")
for message in reversed(st.session_state.conversation):
    st.write(message)
