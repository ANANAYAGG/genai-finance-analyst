# GenAI-Powered Financial Analytics Platform

A sophisticated financial analytics platform that combines natural language processing with SQL query generation to provide intelligent business insights for financial data analysis.

## 🚀 Features

- **Natural Language SQL Query Generation**: Convert business questions into SQL queries using LangChain and OpenAI
- **Interactive Dashboard**: Streamlit-powered web interface for seamless user experience
- **Automated Data Visualization**: Dynamic chart generation based on query results
- **AI-Powered Business Insights**: Intelligent analysis and recommendations for financial data
- **Fraud Detection Analytics**: Specialized tools for identifying high-risk customers and transactions
- **Sample Data Generation**: Built-in synthetic financial data for testing and demonstration

## 🛠️ Technology Stack

- **Backend**: Python, SQLite, LangChain
- **Frontend**: Streamlit
- **AI/ML**: OpenAI GPT-3.5-turbo
- **Data Processing**: Pandas
- **Visualization**: Plotly
- **Data Generation**: Faker

## 📸 Application Screenshots

### Main Dashboard Interface
The platform features a clean, professional interface with natural language query capabilities:



### SQL Query Generation & Results
The system automatically converts natural language questions into SQL queries and displays results in an organized table format:



### Data Visualization & AI Insights
Interactive charts and AI-powered business insights help analysts understand patterns and make data-driven decisions:



## 📋 Prerequisites

- Python 3.8+
- OpenAI API Key
- Required Python packages (see requirements.txt)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone 
   cd genai-financial-analytics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install additional LangChain dependencies**
   ```bash
   pip install langchain langchain-openai langchain-community
   ```

## 🚀 Usage

1. **Start the Streamlit application**
   ```bash
   streamlit run streamlit_langchain_app.py
   ```

2. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`
   - Enter your OpenAI API key in the sidebar
   - Wait for the "Analyst ready!" confirmation

3. **Query your data**
   - Use natural language questions like:
     - "Find customers at high risk of fraud"
     - "Show me customers with credit scores above 750"
     - "Which customers have the highest transaction amounts?"
   - Click "Analyze with AI" to generate insights

## 📊 Sample Queries

The platform supports various types of financial analysis queries:

- **Risk Assessment**: "Find customers at high risk of fraud"
- **Credit Analysis**: "Show customers with low credit scores"
- **Transaction Analysis**: "What are the most popular merchant categories?"
- **Customer Segmentation**: "Group customers by annual income ranges"

## 🏗️ Project Structure

```
genai-financial-analytics/
├── langchain_financial_analyzer.py    # Core analyzer class
├── streamlit_langchain_app.py         # Streamlit dashboard
├── requirements.txt                   # Python dependencies
├── financial_data.db                  # SQLite database (auto-generated)
└── README.md                          # Project documentation
```

## 🔍 Core Components

### LangChainFinancialAnalyzer
- Manages database connections and operations
  ![image](https://github.com/user-attachments/assets/257dd723-f40a-4093-89d7-99aae2152677)
- Integrates with OpenAI for natural language processing 
- Generates SQL queries from business questions
  ![image](https://github.com/user-attachments/assets/9441886f-4bb0-4275-b2cc-f11a3cc6bf7b)
- Genarates Visualization with zoom features,downloading plot and other tools for fullscreen also
  ![image](https://github.com/user-attachments/assets/8600fbee-225c-4b9d-b291-d2df5cc4e0b8)
- Provides AI-powered insights and recommendations
![image](https://github.com/user-attachments/assets/84e65891-3fd8-433b-8389-dd7358f9119e)

### Database Schema
- **customers**: Customer information including credit scores, income, and risk categories
- **transactions**: Transaction history with fraud indicators and merchant categories

## 🎯 Key Features Explained

### Natural Language Processing
The platform uses LangChain's SQL query chain to convert natural language questions into executable SQL queries, making data analysis accessible to non-technical users.

### Automated Insights
After executing queries, the system generates business insights using AI, providing actionable recommendations for financial analysts.

### Interactive Visualizations
Results are automatically visualized using Plotly charts, including scatter plots for multi-dimensional data and histograms for single-variable analysis.

## 🔒 Security Notes

- API keys are handled securely through Streamlit's sidebar input
- Database operations use parameterized queries to prevent SQL injection
- Sample data uses synthetic information generated by Faker library

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 👨‍💻 Author

**Ananay Aggarwal**

## 🆘 Support

For support and questions, please open an issue in the GitHub repository.

## 🔮 Future Enhancements

- Integration with real financial data sources
- Advanced machine learning models for fraud detection
- Multi-database support
- Enhanced visualization options
- Real-time data streaming capabilities

*Built with ❤️ By Ananay Aggarwal*

