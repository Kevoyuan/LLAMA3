import streamlit as st
import ollama

# Function to display chat messages
def display_messages(messages):
    for msg in messages:
        role = "user" if msg["role"] == "user" else "assistant"
        avatar = "🧑‍💻" if role == "user" else "🤖"
        st.chat_message(role, avatar=avatar).write(msg["content"])

# Function to generate a response using the ollama model
def generate_response():
    response = ollama.chat(model='llama3', stream=True, messages=st.session_state[st.session_state["current_chat"]])
    full_message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        full_message += token
    return full_message

# Function to generate a chat name based on its content
def generate_chat_name(chat):
    user_messages = " ".join([msg["content"] for msg in chat if msg["role"] == "user"])
    return user_messages[:20] + "..." if len(user_messages) > 20 else user_messages

# Set the title of the main app
st.title("💬 Local LLMBot")

# Sidebar for managing chat sessions
with st.sidebar:
    st.header("Chat Sessions")
    
    # Option to create a new chat session
    if st.button("New Chat"):
        new_key = f"chat_{len([key for key in st.session_state.keys() if key.startswith('chat_')]) + 1}"
        st.session_state[new_key] = [{"role": "assistant", "content": "How can I help you?"}]
        st.session_state["current_chat"] = new_key

    # Display existing chat sessions in a selectbox for navigation
    chat_keys = [key for key in st.session_state.keys() if key.startswith("chat_")]
    chat_names = {key: generate_chat_name(st.session_state[key]) for key in chat_keys}
    
    if chat_keys:
        selected_key = st.selectbox("Select Chat Session", options=chat_keys, format_func=lambda x: chat_names[x], index=chat_keys.index(st.session_state.get("current_chat", chat_keys[0])))
        st.session_state["current_chat"] = selected_key

        # Button to clear the selected chat history
        if st.button('Clear Current Chat History'):
            st.session_state[st.session_state["current_chat"]] = [{"role": "assistant", "content": "How can I help you again?"}]

        # Button to delete the selected chat session
        if st.button('Delete Current Chat'):
            del st.session_state[st.session_state["current_chat"]]
            remaining_chat_keys = [key for key in st.session_state.keys() if key.startswith("chat_")]
            if remaining_chat_keys:
                st.session_state["current_chat"] = remaining_chat_keys[0]
            else:
                del st.session_state["current_chat"]
            st.rerun()

# Main area where the current chat is displayed and interacted with
if "current_chat" in st.session_state:
    display_messages(st.session_state[st.session_state["current_chat"]])

    if prompt := st.chat_input():
        st.session_state[st.session_state["current_chat"]].append({"role": "user", "content": prompt})
        response = generate_response()
        st.session_state[st.session_state["current_chat"]].append({"role": "assistant", "content": response})
        
        # Rename the current chat based on its new content
        current_chat_key = st.session_state["current_chat"]
        new_chat_name = generate_chat_name(st.session_state[current_chat_key])
        chat_names[current_chat_key] = new_chat_name

        # Rerun to display the new messages
        st.rerun()
else:
    st.write("No active chat sessions. Create a new chat using the sidebar.")
