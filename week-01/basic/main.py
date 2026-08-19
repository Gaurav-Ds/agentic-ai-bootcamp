import tiktoken 

en= tiktoken.encoding_for_model("gpt-4")

text = "typically billed per 1 million tokens (MTok). Output tokens cost more than input tokens across all major providers."

tokens = en .encode(text)
print ("tokens -", tokens  )
print(len(tokens))
'''if len(tokens) > 100:
    print("The text is too long for the model. Please shorten it.")
    '''
    
    
print(en.decode(tokens))
# use tokenization it 
"""
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

Brain=OpenAI()
text=""

embedding_model =Brain.embeddings.create(
    model="text-embedding-3-small",
    input=text)


print('meanig full number of tokens used in the text:',len(embedding_model.data[0].embedding)) 
"""

