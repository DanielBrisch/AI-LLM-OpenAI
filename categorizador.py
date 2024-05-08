from openai import OpenAI 
from dotenv import load_dotenv
import os 

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
       {
    "role":"system",
    "content": """
    Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou Casa de uma descrição da categoria.
    """
},{
    "role" : "user",
    "content": """
    Escova de dentes de bambu
    """
}
    ],
    model="gpt-4"
)

print(resposta.choices[0].message.content)