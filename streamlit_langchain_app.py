# streamlit_langchain_app.py - Working Version
import streamlit as st
import pandas as pd
import plotly.express as px

# Import your analyzer
from langchain_financial_analyzer import LangChainFinancialAnalyzer

def create_langchain_dashboard():
    st.set_page_config(
        page_title="LangChain Financial Analytics", 
        layout="wide",
        page_icon="🏦"
    )
    
    st.title("🏦 LangChain-Powered Financial Analytics Platform")
    st.markdown("*AI-SQL Integration for American Express Data Analysis*")
    
    # Get OpenAI API key
    openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
    
    if not openai_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar to continue")
        return
    
    # Initialize analyzer
    try:
        if 'analyzer' not in st.session_state:
            with st.spinner("Initializing LangChain analyzer..."):
                st.session_state.analyzer = LangChainFinancialAnalyzer(openai_key)
        
        analyzer = st.session_state.analyzer
        st.success("✅ LangChain analyzer ready!")
        
    except Exception as e:
        st.error(f"❌ Error initializing analyzer: {str(e)}")
        return
    
    # Main interface
    st.header("🤖 Natural Language SQL Query")
    
    # Example questions
    with st.expander("💡 Try these example questions"):
        examples = [
            "Show me customers with credit scores above 750",
            "Which customers have the highest transaction amounts?",
            "Find customers at high risk of fraud",
            "What are the most popular merchant categories?"
        ]
        
        for i, example in enumerate(examples):
            if st.button(f"Try: {example}", key=f"ex_{i}"):
                st.session_state.current_question = example
    
    # Query input
    question = st.text_area(
        "Ask your business question:",
        value=st.session_state.get('current_question', ''),
        placeholder="e.g., Which customers have the highest credit utilization?",
        height=100
    )
    
    if st.button("🔍 Analyze with AI", type="primary") and question:
        with st.spinner("🧠 AI is analyzing your question..."):
            result = analyzer.natural_language_query(question)
        
        if result["success"]:
            st.success("✅ Analysis Complete!")
            
            # Show SQL query
            st.markdown("### 🔍 Generated SQL Query")
            st.code(result["sql_query"], language="sql")
            
            # Show results
            if not result["results_df"].empty:
                st.markdown("### 📊 Query Results")
                st.dataframe(result["results_df"], use_container_width=True)
                
                # Auto-visualization
                numeric_cols = result["results_df"].select_dtypes(include=['number']).columns
                if len(numeric_cols) >= 1:
                    st.markdown("### 📈 Visualization")
                    if len(numeric_cols) >= 2:
                        fig = px.scatter(result["results_df"], 
                                       x=numeric_cols[0], 
                                       y=numeric_cols[1])
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        fig = px.histogram(result["results_df"], 
                                         x=numeric_cols[0])
                        st.plotly_chart(fig, use_container_width=True)
            
            # Show AI insights
            st.markdown("### 🧠 AI Business Insights")
            st.markdown(result["agent_response"])
            
        else:
            st.error(f"❌ Analysis failed: {result['error']}")

if __name__ == "__main__":
    create_langchain_dashboard()
