import os
from dotenv import dotenv_values

import openai
from canopy.tokenizer import Tokenizer
from canopy.chat_engine import ChatEngine
from canopy.knowledge_base import KnowledgeBase
from canopy.context_engine import ContextEngine
from canopy.models.data_models import Messages, UserMessage, AssistantMessage


env = dotenv_values('.env')
os.environ["PINECONE_API_KEY"] = env['PINECONE_API_KEY']
os.environ["PINECONE_ENVIRONMENT"] = 'us-east1-gcp'
openai.api_key = env['OPENAI_API_KEY']


class Assistant:
    def __init__(self, index_name):
        super(Assistant).__init__()
        self.tokinzer = Tokenizer.initialize()
        self.index_name = index_name
        self.history = list()

    def __initialize_knowledgebase(self):
        '''
        Initialize return the knowledge base.
        '''
        kb = KnowledgeBase(index_name=self.index_name)
        kb.connect()
        kb.verify_index_connection()

        return kb
    
    def __initialize_contextengine(self):
        '''
        Initialize and retun the context engine.
        '''
        kb = self.__initialize_knowledgebase()
        context_engine = ContextEngine(
            knowledge_base=kb
                                    )

        return context_engine
    
    def __initialize_chatengine(self):
        '''
        Initialize and return the chat engine.
        '''
        context_engine = self.__initialize_contextengine()
        chat_engine = ChatEngine(
            context_engine=context_engine
        )
        return chat_engine
    
    def run(self, new_message: str) -> tuple[str, Messages]:
        chat_engine = self.__initialize_chatengine() 
        messages = self.history + [UserMessage(content=new_message)]
        response = chat_engine.chat(messages)
        assistant_response = response.choices[0].message.content        
        return assistant_response, messages + [AssistantMessage(content=assistant_response)]        