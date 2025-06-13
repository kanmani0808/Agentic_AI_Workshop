import streamlit as st
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from duckduckgo_search import DDGS  # ✅ correct import

# ==== Hardcoded Gemini API Key ====
GOOGLE_API_KEY = "AIzaSyBU1UvNgeswPmzSnp-fBeGbt_TPmLgG2Qs"  # Replace with your actual Gemini API Key

# ==== Initialize Gemini LLM ====
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY
)

# ==== Search Tool Function ====
def get_search_links(query: str, max_results=5):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            return [res["href"] for res in results if "href" in res]
    except Exception:
        return []

def search_tool_func(query):
    sources = get_search_links(query)
    return "Use the following sources to answer the question:\n" + "\n".join(sources)

# ==== Register Tool ====
search_tool = Tool(
    name="DuckDuckGo Search",
    func=search_tool_func,
    description="Useful for searching current events and real-time information."
)

# ==== Initialize Agent ====
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=False
)

# ==== Streamlit Interface ====
st.set_page_config(page_title="🔍 Ask AI - Gemini + DuckDuckGo", layout="centered")
st.title("🔍 Ask Me Anything")
st.markdown("💬 Real-time answers on current events, news, facts using Gemini + DuckDuckGo")

query = st.text_input("❓ What do you want to know?")
submit = st.button("Ask")

if submit and query.strip():
    with st.spinner("🤖 Generating response..."):
        try:
            links = get_search_links(query)
            response = agent.run(query)
            st.success("✅ Answer:")
            st.write(response)

            if links:
                st.markdown("🔗 **Sources:**")
                for link in links:
                    st.markdown(f"- [{link}]({link})")

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

elif submit:
    st.warning("Please enter a question to ask.")

st.markdown("---")
st.caption("Powered by 🧠 Gemini AI and 🌍 DuckDuckGo | Built with ❤️ using Streamlit")
