# Retrieval Augmented Generation System using Canopy

Canopy is an SDK released by pinecone. This allows us to build, test and package RAG applications using pinecone vector DB.<br>
<br>
Canopy, powered by Pinecone, is an open-source RAG (Retrieval Augmented Generation) framework for building scalable GenAI applications. It simplifies and accelerates the creation of RAG-powered applications, offering free storage for up to 100K vectors. Canopy supports multiple data formats and is compatible with OpenAI LLMs, including GPT-4 Turbo. It comprises three main components: Knowledge Base, Context Engine, and Canopy Chat Engine, for comprehensive RAG workflow management. 

## Improvements
1. **Free Storage**: Allows free storage for up to 100K vectors, equivalent to about 15M words or 30K pages of text.
2. **Easy Implementation**: Supports text data in various formats and is compatible with OpenAI LLMs, including GPT-4 Turbo.
3. **Scalability and Reliability** : Designed for fast and reliable GenAI applications at scale.
4. **Modularity and Extensibility**: Canopy can run as a web service or application, with a REST API for easy integration into existing OpenAI applications.
 

## Prerequisites
Pinecone API : https://www.pinecone.io/
OpenAI API: https://openai.com/

## Setup
1. Create a `.env` file and store the above listed APIs
```
Pinecone API : https://www.pinecone.io/
OpenAI API: https://openai.com/

```
2. Install dependencies in your virtual environment.
```
pip install -r requirements.txt
```
3. Run the command from your CLI.
```
python main.py
```