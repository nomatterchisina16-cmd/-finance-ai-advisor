# 💰 Finance AI Personal Advisor

A comprehensive AI-powered personal finance advisor built with Streamlit and OpenAI, helping you make informed financial decisions.

## 🌟 Features

### 📊 Dashboard
- Real-time portfolio overview
- Asset allocation visualization
- Portfolio growth tracking
- Monthly financial summary

### 🤖 AI Advisor Chat
- Interactive chat with AI financial advisor
- Personalized investment recommendations
- Budgeting guidance
- Retirement planning assistance
- Custom financial advice

### 💼 Portfolio Manager
- Add and track investments
- Monitor holdings performance
- Calculate gains/losses
- Asset diversification tracking

### 📈 Investment Analysis
- Stock ticker analysis
- Technical analysis
- Fundamental metrics
- Market sentiment analysis

### 🎯 Financial Goals
- Set and track financial goals
- Calculate goal progress
- Project future savings
- Plan for retirement, house, emergencies

### 📚 Education Hub
- Financial literacy content
- Investment concepts
- Trading strategies
- Risk management tips

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API Key
- Git (for GitHub integration)

### Installation

1. **Clone the repository** (after pushing to GitHub)
```bash
git clone https://github.com/yourusername/finance-ai-advisor.git
cd finance-ai-advisor
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the app**
Open your browser and go to `http://localhost:8501`

## 🔐 Configuration

### Setting up OpenAI API Key

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Enter it in the app's sidebar under Configuration
3. Or set environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Environment Variables (Optional)
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your-api-key-here
```

## 📦 Project Structure

```
finance-ai-advisor/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── .gitignore               # Git ignore file
└── .env                     # Environment variables (not tracked)
```

## 📝 Usage Examples

### Using the AI Advisor
1. Navigate to "🤖 AI Advisor Chat"
2. Enter your OpenAI API Key in the sidebar
3. Ask questions like:
   - "How should I diversify my $50,000 portfolio?"
   - "What's the best way to save for retirement?"
   - "Which ETFs would you recommend for passive investing?"

### Managing Your Portfolio
1. Go to "💼 Portfolio Manager"
2. Click "Add Investment" and fill in details
3. Monitor your holdings and performance
4. Track gains/losses in real-time

### Setting Financial Goals
1. Navigate to "🎯 Financial Goals"
2. Fill in goal name, target amount, and date
3. Enter current savings and monthly contribution
4. Calculate and track progress toward your goals

## 🌐 Deployment to Streamlit Cloud

### Step 1: Push to GitHub

```bash
# Initialize git repo (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Finance AI Personal Advisor"

# Add remote repository
git remote add origin https://github.com/yourusername/finance-ai-advisor.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Connect your GitHub account
4. Select your repository: `finance-ai-advisor`
5. Select branch: `main`
6. Set main file path: `app.py`
7. Click "Deploy"

### Step 3: Add Secrets (for API Keys)

In Streamlit Cloud dashboard:
1. Click on your app settings (three dots)
2. Go to "Secrets"
3. Add your secrets in TOML format:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

The app will then use `st.secrets` to access these securely.

## 📊 Features Detail

### Dashboard
- Displays key financial metrics
- Shows portfolio distribution
- Tracks investment performance
- Monthly spending breakdown

### AI Advisor
- Powered by GPT-3.5-turbo
- Context-aware responses
- Financial expertise focused
- Chat history preserved

### Portfolio Manager
- Add/track multiple assets
- Support for various asset types
- Real-time P&L calculation
- Performance metrics

### Investment Analysis
- Stock ticker lookup
- Technical indicators
- Fundamental analysis
- Market trends

### Financial Goals
- Goal creation and tracking
- Progress visualization
- Savings projector
- Timeline management

### Education
- 10+ topics covered
- Beginner-friendly content
- Investment strategies
- Financial tips

## 🔧 Customization

### Modify App Title and Theme
Edit the `page_title` in `app.py`:
```python
st.set_page_config(
    page_title="Your Custom Title",
    page_icon="💰",
    layout="wide"
)
```

### Add Custom CSS
Modify the CSS section in `app.py` to customize colors and styling.

### Add New Features
1. Create new functions for your features
2. Add them to the sidebar radio buttons
3. Implement the feature logic

## 📚 Documentation

- [Streamlit Docs](https://docs.streamlit.io)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Plotly Docs](https://plotly.com/python)
- [Pandas Docs](https://pandas.pydata.org/docs)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

**This application is for educational purposes only.** It is NOT professional financial advice. Always consult with a qualified financial advisor before making investment decisions. The creators are not responsible for any financial losses or decisions made based on this application.

## 💡 Tips for Best Results

1. **Secure your API Key**: Never commit your API key to GitHub
2. **Use .env files**: Store sensitive data locally
3. **Test locally first**: Test your changes with `streamlit run app.py` before pushing to GitHub
4. **Keep dependencies updated**: Regularly update packages with `pip install --upgrade -r requirements.txt`
5. **Monitor usage**: Keep track of OpenAI API usage to manage costs

## 🐛 Troubleshooting

### App won't start
- Check Python version: `python --version` (should be 3.8+)
- Verify all dependencies: `pip install -r requirements.txt`
- Check for syntax errors: `python -m py_compile app.py`

### API errors
- Verify your OpenAI API key is correct
- Check your account has API credits
- Ensure you're in an allowed region

### Deployment issues on Streamlit Cloud
- Ensure `requirements.txt` is in repo root
- Check GitHub connection is authorized
- Verify app.py is in root directory
- Add secrets in Streamlit Cloud dashboard

## 📞 Support

For issues and questions:
1. Check GitHub Issues
2. Review Streamlit documentation
3. Check OpenAI API status page

---

**Made with ❤️ for your financial future**

**Current Version**: 1.0.0  
**Last Updated**: 2024
