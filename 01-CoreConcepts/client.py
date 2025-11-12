# Cliente que usa la API de OpenAI (no MCP)
# Corrige el warning de asyncio y usa el método correcto del SDK

import os
import asyncio
import json
from dotenv import load_dotenv
from openai import OpenAI
from mcp_server import weather_tools

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def chat_with_streaming():
    """
    Cliente que usa OpenAI para interactuar con el usuario
    y genera respuestas en streaming.
    """

    print("🤖 Iniciando conversación con OpenAI")
    print("=" * 50)
    print("Escribe 'salir' para terminar")

    messages = []

    while True:
        user_input = input("Tú: ").strip()

        if user_input.lower() in ["salir", "quit", "exit"]:
            print("🤖 Hasta luego!")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            print("\n🤖 Asistente: ", end="", flush=True)

            # Crear respuesta con streaming (nota: completions con 's')
            stream = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL"),
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un asistente útil que proporciona información del clima.",
                    }
                ]
                + messages,
                temperature=0.7,
                stream=True,
                tools=json.loads(weather_tools),
            )

            # Recopilar la respuesta completa mientras se muestra
            full_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].deltna.content
                    print(content, end="", flush=True)
                    full_response += content

            print("\n")  # Nueva línea al final

            # Añadir respuesta completa al historial
            messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: No se encontró OPENAI_API_KEY en el archivo .env")
        exit(1)

    # Ejecutar correctamente la función async
    asyncio.run(chat_with_streaming())
