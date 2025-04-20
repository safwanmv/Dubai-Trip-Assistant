# 🧙‍♂️ Dubai Trip Assistant – AI Travel Chatbot

Dubai Trip Assistant is an AI-powered chatbot designed to help travelers plan their trips to Dubai. From recommending attractions, food spots, and hotels to generating day-wise itineraries — this assistant delivers quick, helpful, and professional travel insights using OpenAI's powerful language model.

Built with **Python**, **Streamlit**, and **OpenAI API**, it runs entirely in your browser.

---

## 🚀 Features

- 🤖 AI-based Dubai travel planner  
- 💬 Chat interface with memory of past messages  
- 📍 Recommendations for attractions, food, hotels, and local events  
- 🗕️ Day-wise itinerary suggestions  
- 🌐 Runs locally in browser with easy setup  

---

## 💪 Tech Stack

- Python 3.x  
- Streamlit  
- OpenAI GPT  
- Python-dotenv for secret handling  
- Git for version control  

---

## 📦 Installation & Setup

### ✅ Prerequisites

- Python 3.8 or higher  
- OpenAI API key  
- Git installed  

---

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/dubai-trip-assistant.git
cd dubai-trip-assistant
```

---

### ✅ 2. Create and Activate Virtual Environment

```bash
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install:

```bash
pip install streamlit openai python-dotenv
```

---

### ✅ 4. Add Environment Variables

Create a file named `.env` in your project root and paste your OpenAI key:

```env
OPENAI_API_KEY=your-openai-key-here
```

> 🔐 **Never share your `.env` file publicly.**

---

### ✅ 5. Run the App

```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure

```
dubai-trip-assistant/
│
├── app.py            # Main chatbot script
├── .env              # API key (excluded from Git)
├── .gitignore        # Files/folders to exclude from Git
├── requirements.txt  # Python package list
├── README.md         # This documentation
└── venv/             # Python virtual environment
```

---

## 🛄 Deploying to Streamlit Cloud

1. Push your project to GitHub.  
2. Visit: https://share.streamlit.io  
3. Click **New App**, select your repo.  
4. Add `OPENAI_API_KEY` to the **Secrets** tab.  
5. Deploy! 🚀  

---

## ✨ How to Use

1. Ask a question like “Plan my 3-day Dubai trip.”  
2. Dubai Genie will reply with curated suggestions.  
3. Ask more for hotels, foods, events, or more detail.  

---

## 🛡️ Security

- `.env` keeps your keys safe and private.  
- `.gitignore` ensures sensitive files are excluded from GitHub.  

---

## 💡 Contributing

Got improvements or ideas? Fork it, star it, improve it!

---

## 📬 Contact

Email: safwanmv007@gmail.com  
GitHub: [safwanmv](https://github.com/safwanmv)

---

## ✅ Example `.env` File

```
OPENAI_API_KEY=your-openai-api-key
```

---

## ✅ Example `.gitignore` File

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
env/

# Environment variables
.env

# Streamlit cache
.streamlit/

# VS Code settings
.vscode/
```

---

## ✅ Example `requirements.txt` File

```
streamlit
openai
python-dotenv
```

---

## 🛃️ Happy Travels with Dubai Genie!

![Dubai Trip Assistant Screenshot]

(assets/images/Screenshot 1.png)

(assets/images/Screenshot 2.png)

(assets/images/Screenshot 3.png)

(assets/images/Screenshot 4.png)

(assets/images/Screenshot 5.png)

