from openai import OpenAI


from dotenv import load_dotenv
load_dotenv()







client = OpenAI()

SYSTEM_PROMPT = """You are a helpful assistant. solve user queries in a simple and easy to understand way..

you have to follow below example in that way you can answer 


Example:
user query: Nagpur?

output: Nagpur bole to zhakas place 

user_query: gen ai
output: Gen bole currier ka zannat 



"""

user_qurey= "Nagpuri poha means?"

client_response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content":  SYSTEM_PROMPT},
        {"role": "user", "content": user_qurey}
    ]
)

print(client_response.choices[0].message.content)