from ollama import Client

from config_loader import load_config


client = Client()


def ask(prompt):

    config = load_config()

    response = client.chat(
        model=config["model"],
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": config["temperature"],
            "num_predict": config["max_tokens"]
        }
    )

    return response["message"]["content"]