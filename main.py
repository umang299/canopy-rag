from assistant import Assistant
from utils import logger

if __name__ == '__name__':
    assistant = Assistant(index_name='docqa-demo')
    while True:
        user_msg = input(str('User: '))
        logger(message=user_msg, role='User')
        response, history = assistant.run(new_message=user_msg)
        print(f'Assistant: {response}')
        logger(message=response, role='Assistant')