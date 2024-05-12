import streamlit as st
import ollama

# Function to display chat messages
def display_messages(messages):
    for msg in messages:
        if msg["role"] == "user":
            st.chat_message("user", avatar="🧑‍💻").write(msg["content"])
        else:
            st.chat_message("assistant", avatar="🤖").write(msg["content"])

# Function to generate a response using the ollama model
def generate_response():
    response = ollama.chat(model='llama3', stream=True, messages=st.session_state[st.session_state["current_chat"]])
    full_message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        full_message += token
        yield token
    return full_message

# Set the title of the main app
st.title("💬 Local LLMBot")

# Sidebar for managing chat sessions
with st.sidebar:
    st.header("Chat Sessions")
    # Option to create a new chat session
    if st.button("New Chat"):
        # Generate a unique session key based on the number of existing sessions
        new_key = f"chat_{len([key for key in st.session_state.keys() if key.startswith('chat_')]) + 1}"
        st.session_state[new_key] = [{"role": "assistant", "content": "How can I help you?"}]
        st.session_state["current_chat"] = new_key

    # Display existing chat sessions in a selectbox for navigation
    chat_keys = [key for key in st.session_state.keys() if key.startswith("chat_")]
    if chat_keys:
        selected_key = st.selectbox("Select Chat Session", options=chat_keys, index=chat_keys.index(st.session_state.get("current_chat", chat_keys[0])))
        st.session_state["current_chat"] = selected_key

        # Button to clear the selected chat history
        if st.button('Clear Current Chat History'):
            st.session_state[st.session_state["current_chat"]] = [{"role": "assistant", "content": "How can I help you again?"}]

        # Button to delete the selected chat session
        if st.button('Delete Current Chat'):
            del st.session_state[st.session_state["current_chat"]]
            # Update current chat to another existing chat if available, or remove 'current_chat' key if none are left
            if chat_keys := [key for key in st.session_state.keys() if key.startswith("chat_")]:
                st.session_state["current_chat"] = chat_keys[0]
            else:
                if "current_chat" in st.session_state:
                    del st.session_state["current_chat"]
            st.experimental_rerun()

# Main area where the current chat is displayed and interacted with
if "current_chat" in st.session_state:
    display_messages(st.session_state[st.session_state["current_chat"]])

    if prompt := st.chat_input():
        st.session_state[st.session_state["current_chat"]].append({"role": "user", "content": prompt})
        response = generate_response()
        st.chat_message("assistant", avatar="🤖").write_stream(response)
        st.session_state[st.session_state["current_chat"]].append({"role": "assistant", "content": response})
else:
    st.write("No active chat sessions. Create a new chat using the sidebar.")
