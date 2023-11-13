# news_research
This project showcases a sophisticated news retrieval and question-answering (Q&A) system using Gradio, LangChain, and OpenAI's GPT models. The system is designed to process user-provided URLs of news articles, analyze their content, and deliver contextually relevant answers to user queries.

## Key Features:

* **Dynamic URL Processing:** Users can input multiple URLs, which the system processes to extract relevant news content.
* **Advanced Text Splitting:** Implements a recursive character text splitter to manage large documents, ensuring comprehensive analysis.
* **AI-Driven Q&A Engine:** Utilizes LangChain and OpenAI's language models to interpret user questions and retrieve accurate answers.
* **Efficient Data Retrieval:** Leverages FAISS (Facebook AI Similarity Search) for efficient indexing and retrieval of text data from news sources.
* **Interactive Chat Interface:** Offers a Gradio-based chat interface for user interaction, enabling real-time question submission and response generation.
* **Environmental Variable Management:** Uses dotenv for secure and efficient management of environment variables.


## Technical Stack:
* Python
* Gradio for UI
* LangChain for language model workflows
* OpenAI API for advanced language models
* FAISS for efficient similarity search in large datasets
* Dotenv for environment variable management

