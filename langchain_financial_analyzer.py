# langchain_financial_analyzer.py - Simplified Working Version
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import random
from faker import Faker

# LangChain imports (working versions)
from langchain.chains import create_sql_query_chain
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI

class LangChainFinancialAnalyzer:
    def __init__(self, openai_api_key: str, db_path: str = "financial_data.db"):
        """Initialize LangChain-powered financial analyzer"""
        self.db_path = db_path
        self.setup_database()
        
        # Initialize LangChain components
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
            openai_api_key=openai_api_key
        )
        
        # Create SQLDatabase object for LangChain
        self.langchain_db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
        
        # Create SQL query chain
        self.sql_query_chain = create_sql_query_chain(self.llm, self.langchain_db)
    
    def setup_database(self):
        """Create and populate the financial database"""
        conn = sqlite3.connect(self.db_path)
        
        # Create tables
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(100),
            credit_score INTEGER,
            annual_income DECIMAL(12,2),
            risk_category VARCHAR(20)
        );
        
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            transaction_date DATETIME,
            merchant_category VARCHAR(50),
            transaction_amount DECIMAL(10,2),
            is_fraud BOOLEAN,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );
        """)
        
        # Check if data exists
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM customers")
        if cursor.fetchone()[0] == 0:
            self.generate_sample_data(conn)
        
        conn.close()
    
    def generate_sample_data(self, conn):
        """Generate sample financial data"""
        fake = Faker()
        
        # Generate customers
        customers_data = []
        for i in range(100):
            customers_data.append({
                'customer_id': i + 1,
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.email(),
                'credit_score': random.randint(300, 850),
                'annual_income': random.randint(25000, 200000),
                'risk_category': random.choice(['Low', 'Medium', 'High'])
            })
        
        customers_df = pd.DataFrame(customers_data)
        customers_df.to_sql('customers', conn, if_exists='replace', index=False)
        
        # Generate transactions
        transactions_data = []
        transaction_id = 1
        
        for customer_id in range(1, 101):
            num_transactions = random.randint(5, 20)
            
            for _ in range(num_transactions):
                transactions_data.append({
                    'transaction_id': transaction_id,
                    'customer_id': customer_id,
                    'transaction_date': fake.date_time_between(start_date='-1y', end_date='now'),
                    'merchant_category': random.choice(['Grocery', 'Gas', 'Restaurant', 'Shopping']),
                    'transaction_amount': round(random.uniform(10.0, 1000.0), 2),
                    'is_fraud': random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])  # 10% fraud
                })
                transaction_id += 1
        
        transactions_df = pd.DataFrame(transactions_data)
        transactions_df.to_sql('transactions', conn, if_exists='replace', index=False)
    
    def natural_language_query(self, question: str) -> dict:
        """Process natural language questions using LangChain SQL chain"""
        try:
            # Generate SQL query
            sql_query = self.sql_query_chain.invoke({"question": question})
            
            # Execute the query
            conn = sqlite3.connect(self.db_path)
            result_df = pd.read_sql_query(sql_query, conn)
            conn.close()
            
            # Generate insights using LLM
            insights_prompt = f"""
            Based on this SQL query and results, provide business insights:
            
            Question: {question}
            SQL Query: {sql_query}
            Results: {result_df.to_string() if not result_df.empty else "No results found"}
            
            Provide actionable business insights for American Express analysts.
            """
            
            insights = self.llm.invoke(insights_prompt)
            
            return {
                "question": question,
                "sql_query": sql_query,
                "results_df": result_df,
                "agent_response": insights.content,
                "success": True
            }
            
        except Exception as e:
            return {
                "question": question,
                "error": str(e),
                "success": False
            }

