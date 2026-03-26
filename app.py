import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from openai import OpenAI
import os

# Configure Streamlit page
st.set_page_config(
    page_title="Finance AI Personal Advisor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .header-title {
        color: #1f77b4;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}
if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = False

# Sidebar Configuration
st.sidebar.markdown("# ⚙️ Configuration")

# API Key Input
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password", key="api_key_input")
if api_key:
    st.session_state.api_key_set = True
    os.environ["OPENAI_API_KEY"] = api_key

st.sidebar.markdown("---")

# Sidebar Navigation
app_mode = st.sidebar.radio(
    "Choose a Feature",
    ["📊 Dashboard", "🤖 AI Advisor Chat", "💼 Portfolio Manager", "📈 Investment Analysis", "🎯 Financial Goals", "📚 Education"]
)

# Initialize AI Client
def get_ai_advisor():
    """Initialize OpenAI client"""
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_financial_advice(user_input):
    """Get financial advice from AI using OpenAI API"""
    try:
        client = get_ai_advisor()
        
        # Build conversation messages
        messages = st.session_state.chat_history.copy()
        messages.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are an expert financial advisor AI. Provide personalized, 
                 accurate financial advice considering:
                 - Risk tolerance and investment goals
                 - Diversification principles
                 - Tax efficiency
                 - Long-term wealth building
                 - Current market conditions
                 Always include a disclaimer that this is for educational purposes."""},
                *messages
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}. Please check your API key and try again."

# DASHBOARD PAGE
if app_mode == "📊 Dashboard":
    st.markdown('<div class="header-title">💰 Finance AI Personal Advisor</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Portfolio Value", "$25,000", "+5.2%")
    with col2:
        st.metric("Monthly Savings", "$1,200", "+8.3%")
    with col3:
        st.metric("Investment Return", "7.5%", "YTD")
    with col4:
        st.metric("Financial Score", "78/100", "+2 pts")
    
    st.markdown("---")
    
    # Financial Overview Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Asset Allocation")
        allocation_data = {
            "Asset Class": ["Stocks", "Bonds", "Cash", "Crypto"],
            "Percentage": [60, 25, 10, 5]
        }
        df_allocation = pd.DataFrame(allocation_data)
        fig_pie = px.pie(df_allocation, values="Percentage", names="Asset Class",
                         title="Current Portfolio Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.subheader("Portfolio Growth (Last 12 Months)")
        dates = pd.date_range(end=datetime.now(), periods=12, freq='M')
        values = np.cumsum(np.random.randn(12) * 500 + 200) + 20000
        df_growth = pd.DataFrame({"Date": dates, "Value": values})
        fig_line = px.line(df_growth, x="Date", y="Value",
                          title="Portfolio Value Over Time")
        st.plotly_chart(fig_line, use_container_width=True)
    
    st.markdown("---")
    
    # Monthly Breakdown
    st.subheader("Monthly Financial Summary")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.info("💵 Income\n$4,500")
    with col2:
        st.warning("💸 Expenses\n$2,800")
    with col3:
        st.success("💾 Savings\n$1,200")
    with col4:
        st.error("💳 Debt\n$5,000")
    with col5:
        st.success("📈 Investments\n$800")

# AI ADVISOR CHAT PAGE
elif app_mode == "🤖 AI Advisor Chat":
    st.markdown('<div class="header-title">🤖 AI Financial Advisor</div>', unsafe_allow_html=True)
    
    if not st.session_state.api_key_set:
        st.warning("⚠️ Please enter your OpenAI API Key in the sidebar to use the AI Advisor.")
    else:
        st.info("💡 Ask me anything about personal finance, investment strategies, budgeting, retirement planning, or financial goals!")
        
        # Chat container
        st.markdown("---")
        st.subheader("Conversation History")
        
        # Display chat history
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    st.write(f"**You:** {message['content']}")
                else:
                    st.write(f"**AI Advisor:** {message['content']}")
        
        st.markdown("---")
        
        # Input area
        col1, col2 = st.columns([0.85, 0.15])
        
        with col1:
            user_input = st.text_input("Your question:", placeholder="Ask about investing, budgeting, taxes, retirement...")
        
        with col2:
            send_button = st.button("Send", use_container_width=True)
        
        if send_button and user_input:
            with st.spinner("AI Advisor is thinking..."):
                response = get_financial_advice(user_input)
                
                # Add to chat history
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.session_state.chat_history.append({"role": "assistant", "content": response})
                
                st.rerun()
        
        # Clear history button
        if st.button("Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

# PORTFOLIO MANAGER PAGE
elif app_mode == "💼 Portfolio Manager":
    st.markdown('<div class="header-title">💼 Portfolio Manager</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([0.6, 0.4])
    
    with col1:
        st.subheader("Add Investment")
        
        with st.form("add_investment"):
            asset_name = st.text_input("Asset Name (e.g., Apple Stock, Bitcoin)")
            asset_type = st.selectbox("Type", ["Stock", "Bond", "ETF", "Crypto", "Real Estate", "Other"])
            quantity = st.number_input("Quantity/Amount", min_value=0.01, step=0.01)
            purchase_price = st.number_input("Purchase Price ($)", min_value=0.01, step=0.01)
            purchase_date = st.date_input("Purchase Date")
            
            submitted = st.form_submit_button("Add to Portfolio")
            
            if submitted and asset_name:
                st.success(f"✅ Added {quantity} units of {asset_name} to your portfolio!")
    
    with col2:
        st.subheader("Portfolio Summary")
        st.metric("Total Holdings", 8)
        st.metric("Current Value", "$25,000")
        st.metric("Total Gain/Loss", "+$3,500", "+16.3%")
    
    st.markdown("---")
    st.subheader("Your Holdings")
    
    # Sample portfolio data
    portfolio_data = {
        "Asset": ["Apple Stock", "Vanguard S&P 500", "Bitcoin", "Corporate Bonds", "Real Estate"],
        "Type": ["Stock", "ETF", "Crypto", "Bond", "Real Estate"],
        "Quantity": [50, 30, 0.5, 10000, 0.25],
        "Purchase Price": [150, 400, 45000, 100, 500000],
        "Current Price": [175, 450, 48000, 102, 520000],
        "Current Value": [8750, 13500, 24000, 1020000, 130000]
    }
    
    df_portfolio = pd.DataFrame(portfolio_data)
    df_portfolio["Gain/Loss"] = df_portfolio["Current Value"] - (df_portfolio["Purchase Price"] * df_portfolio["Quantity"])
    df_portfolio["Return %"] = (df_portfolio["Gain/Loss"] / (df_portfolio["Purchase Price"] * df_portfolio["Quantity"]) * 100).round(2)
    
    st.dataframe(df_portfolio, use_container_width=True)

# INVESTMENT ANALYSIS PAGE
elif app_mode == "📈 Investment Analysis":
    st.markdown('<div class="header-title">📈 Investment Analysis</div>', unsafe_allow_html=True)
    
    st.subheader("Stock/Asset Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, GOOGL)", value="AAPL")
    
    with col2:
        analysis_type = st.selectbox("Analysis Type", ["Technical", "Fundamental", "Sentiment"])
    
    if st.button("Analyze"):
        st.info(f"Analysis for {ticker} - {analysis_type} mode")
        
        # Simulated analysis
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Current Price", "$175.50", "+2.3%")
        with col2:
            st.metric("52 Week High", "$199.62")
        with col3:
            st.metric("52 Week Low", "$124.17")
        
        st.write("**Key Metrics:**")
        metrics_df = pd.DataFrame({
            "Metric": ["P/E Ratio", "Dividend Yield", "Market Cap", "Beta", "RSI"],
            "Value": ["28.5", "0.65%", "$2.8T", "1.2", "62"]
        })
        st.table(metrics_df)

# FINANCIAL GOALS PAGE
elif app_mode == "🎯 Financial Goals":
    st.markdown('<div class="header-title">🎯 Financial Goals</div>', unsafe_allow_html=True)
    
    st.subheader("Set Your Financial Goals")
    
    col1, col2 = st.columns(2)
    
    with col1:
        goal_name = st.text_input("Goal Name", placeholder="e.g., Buy a House, Retirement")
        goal_amount = st.number_input("Target Amount ($)", min_value=100, step=100)
        target_date = st.date_input("Target Date")
    
    with col2:
        current_savings = st.number_input("Current Savings ($)", min_value=0, step=100)
        monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0, step=50)
        expected_return = st.slider("Expected Annual Return (%)", 0.0, 15.0, 7.0)
    
    if st.button("Calculate Goal Progress"):
        months_remaining = (target_date - datetime.now().date()).days / 30
        total_contributions = current_savings + (monthly_contribution * months_remaining)
        
        projected_value = total_contributions * (1 + expected_return/100) ** (months_remaining/12)
        progress_pct = (projected_value / goal_amount * 100) if goal_amount > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Target Amount", f"${goal_amount:,.0f}")
        with col2:
            st.metric("Projected Value", f"${projected_value:,.0f}")
        with col3:
            st.metric("Progress", f"{min(progress_pct, 100):.1f}%")
        
        st.progress(min(progress_pct / 100, 1.0))
        
        if progress_pct >= 100:
            st.success("✅ Goal on track!")
        else:
            st.warning(f"⚠️ Need ${goal_amount - projected_value:,.0f} more")
    
    st.markdown("---")
    st.subheader("Your Financial Goals")
    
    goals_data = {
        "Goal": ["House Down Payment", "Retirement Fund", "Emergency Fund", "Vacation Fund"],
        "Target": ["$100,000", "$1,000,000", "$25,000", "$10,000"],
        "Saved": ["$35,000", "$280,000", "$20,000", "$6,500"],
        "Progress": [35, 28, 80, 65]
    }
    
    df_goals = pd.DataFrame(goals_data)
    
    for idx, row in df_goals.iterrows():
        col1, col2 = st.columns([0.7, 0.3])
        with col1:
            st.write(f"**{row['Goal']}**")
            st.progress(row["Progress"] / 100)
        with col2:
            st.write(f"{row['Progress']}%\n{row['Saved']}")

# EDUCATION PAGE
elif app_mode == "📚 Education":
    st.markdown('<div class="header-title">📚 Financial Education Hub</div>', unsafe_allow_html=True)
    
    topic = st.selectbox(
        "Select a Topic",
        [
            "Introduction to Investing",
            "Understanding Stocks",
            "Bonds and Fixed Income",
            "Mutual Funds & ETFs",
            "Cryptocurrency Basics",
            "Real Estate Investing",
            "Retirement Planning",
            "Tax Strategies",
            "Risk Management",
            "Behavioral Finance"
        ]
    )
    
    education_content = {
        "Introduction to Investing": "Investing is the process of putting your money into financial assets with the goal of growing your wealth over time...",
        "Understanding Stocks": "A stock represents ownership in a company. When you buy stock, you become a shareholder...",
        "Bonds and Fixed Income": "Bonds are debt securities issued by governments and corporations. They provide fixed income...",
        "Mutual Funds & ETFs": "Mutual funds and ETFs allow you to invest in a diversified portfolio with a single purchase...",
        "Cryptocurrency Basics": "Cryptocurrency is digital currency secured by cryptography. Bitcoin is the first and most well-known...",
        "Real Estate Investing": "Real estate is a tangible asset that can provide income through rent or appreciation...",
        "Retirement Planning": "Retirement planning involves determining how much money you need and creating a strategy to save...",
        "Tax Strategies": "Understanding tax-efficient investing can help you keep more of your investment gains...",
        "Risk Management": "Diversification and asset allocation are key strategies for managing investment risk...",
        "Behavioral Finance": "Behavioral finance studies how emotions and psychology affect financial decisions..."
    }
    
    st.write(education_content.get(topic, "Content not found"))
    
    st.markdown("---")
    st.subheader("Quick Tips")
    
    tips = [
        "✅ Start investing early - compound interest is your friend",
        "✅ Diversify your portfolio across different asset classes",
        "✅ Maintain an emergency fund of 3-6 months of expenses",
        "✅ Automate your savings and investments",
        "✅ Review and rebalance your portfolio annually",
        "✅ Understand your risk tolerance before investing",
        "✅ Keep investment costs low through low-fee index funds",
        "✅ Invest for the long term, not short-term gains"
    ]
    
    for tip in tips:
        st.write(tip)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
    <p>💰 Finance AI Personal Advisor v1.0</p>
    <p><small>Disclaimer: This is for educational purposes only. Not financial advice. Always consult a professional.</small></p>
    </div>
""", unsafe_allow_html=True)
