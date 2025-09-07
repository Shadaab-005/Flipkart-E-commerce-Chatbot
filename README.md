🛒 Flipkart E-commerce Chatbot
==============================

An intelligent chatbot that answers **product, order, and policy-related queries** using data scraped from Flipkart.The chatbot combines **semantic routing**, **vector search**, and **LLM-powered responses** to deliver contextual and accurate answers.

🚀 Features
-----------

*   ✅ **Web Scraping** – Collected and structured Flipkart product & FAQ data.
    
*   ✅ **Semantic Routing** – Classifies queries into FAQ, SQL, or Small Talk using transformer-based embeddings.
    
*   ✅ **Retrieval-Augmented Responses** – Uses **ChromaDB** for FAQ retrieval and **Groq LLM** for generating context-aware answers.
    
*   ✅ **Interactive UI** – Built with **Streamlit** for a user-friendly chat interface.
    

🏗️ Architecture
----------------

1.  **Web Scraping** → Extract Flipkart product + policy FAQs.
    
2.  **ChromaDB** → Store FAQs as vector embeddings for retrieval.
    
3.  **Semantic Router** → Route queries to faq, sql, or small-talk.
    
4.  **Groq LLM** → Generate conversational answers from retrieved context.
    
5.  **Streamlit UI** → Chat interface for end-users.
    

⚙️ Tech Stack
-------------

*   **Python**
    
*   **Streamlit** (UI)
    
*   **ChromaDB** (vector database)
    
*   **Semantic-Router** (intent classification)
    
*   **HuggingFace Transformers** (multi-qa-mpnet-base-dot-v1)
    
*   **Groq LLM API**
    
*   **Pandas** (data handling)
    
*   **BeautifulSoup** (web scraping)
    
*   **dotenv** (environment variables)
    

📂 Project Structure
--------------------
flipkart-chatbot/

│── main.py           # Streamlit app

│── faq.py            # FAQ ingestion + retrieval

│── router.py         # Semantic router setup

│── smalltalk.py      # Small talk handler (LLM powered)

│── resources/        # FAQ dataset (from Flipkart scraping)

│── db.sqlite         # ChromaDB persistent storage

│── .env              # API keys & config

│── requirements.txt  # Dependencies


▶️ Getting Started
------------------

### 1️⃣ Clone repo
`   git clone https://github.com/yourusername/flipkart-chatbot.git  cd flipkart-chatbot   `

### 2️⃣ Install dependencies
`   pip install -r requirements.txt   `

### 3️⃣ Setup environment variables

Create a .env file in the root folder:

`   GROQ_API_KEY=your_api_key_here 
   GROQ_MODEL=llama-3.3-70b-versatile `   

### 4️⃣ Run the chatbot
`   streamlit run main.py   `

🧠 Example Queries
------------------

*   _"What is the refund policy?"_ → (FAQ)
    
*   _"Show me Puma shoes under 3000"_ → (SQL)
    
*   _"How are you?"_ → (Small Talk)
    

📌 Future Enhancements
----------------------

*   🔍 Add product recommendation using scraped data.
    
*   📦 Integrate real-time order tracking API.
    
*   🌍 Support multilingual queries (Hindi/English mix).
    

✨ Demo Screenshot
-----------------



![Flipkart Chatbot Demo](resource/product-ss.png)


🤝 Contributing
---------------

Contributions are welcome! Feel free to open issues or submit PRs.
