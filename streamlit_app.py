import os
import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')  # Assuming 'gemini-pro' is the model for general purposes

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("Empower.AI: Rethinking Equality, Reinventing Tomorrow🔄🌏")

# Sidebar with resources and information on gender equality topics
st.sidebar.title("Gender equality is not only a fundamental human right, but a necessary foundation for a peaceful, prosperous and sustainable world🌍")

st.sidebar.subheader("Project Overview")
st.sidebar.write("This AI-powered project leverages Google's Gemini-Pro to support gender equality by tackling specific challenges that women and girls face around the world.")

st.sidebar.subheader("Features")
st.sidebar.write("""
- **Ending Discrimination**: Provides information and resources to combat discrimination against women and girls.
- **Eliminating Violence**: Offers guidance on preventing and addressing violence against women and girls.
- **Healthcare Access**: Ensures access to healthcare resources and information for women and girls globally.
- **Economic Empowerment**: Supports women and girls in achieving financial independence and leadership opportunities.
""")

st.sidebar.subheader("References")
st.sidebar.write("- [UN Women - Gender Equality](https://www.unwomen.org/en)")
st.sidebar.write("- [WHO - Violence Against Women](https://www.who.int/news-room/fact-sheets/detail/violence-against-women)")
st.sidebar.write("- [UNICEF - Health for Women and Children](https://www.unicef.org/health)")
st.sidebar.write("- [World Bank - Gender Equality and Development](https://www.worldbank.org/en/topic/gender)")

# Social Media Links Section
st.sidebar.subheader("Connect With Me")

# Add Social Media Links
st.sidebar.write("You can find me on the following platforms:")

# Adding Social Media Links
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/roshnikumari1) :blue_heart:")
st.sidebar.markdown("[GitHub](https://github.com/RSN601KRI) :black_cat:")
st.sidebar.markdown("[Twitter](https://x.com/rsnkyx) :bird:")
st.sidebar.markdown("[Portfolio](https://bento.me/roshnikri) :earth_africa:")

# Function to detect gender equality and social impact project topics
def is_gender_equality_or_project_topic(user_input):
    
    keywords = ["gender equality", "women's rights", "online harassment", "pay gap", "STEM education", "project idea", "social impact", "empowering women"]
    return any(keyword in user_input.lower() for keyword in keywords)

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask about gender equality projects, social impact ideas, and more...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Determine if the user's prompt is related to gender equality or social impact project ideas
    if is_gender_equality_or_project_topic(user_prompt):
        # Generate a response focused on gender equality topics
        response_text = (
            "This chatbot provides information and support on various aspects of gender equality:\n\n"
            "- Ending discrimination by promoting equal rights and opportunities.\n"
            "- Preventing and addressing violence against women and girls.\n"
            "- Improving access to healthcare for women and girls.\n"
            "- Supporting economic empowerment and leadership opportunities for women."
        )
        st.chat_message("assistant").markdown(response_text)
        
    else:
        # For other general queries, proceed as usual
        gemini_response = st.session_state.chat_session.send_message(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
