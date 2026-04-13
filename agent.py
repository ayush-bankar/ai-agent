import requests

history = []
# requests.post()= send data and get back the response while the get only read the data and does not bring back the response

def chat(message):
    history.append(f"User: {message}")

    full_conversation = "\n".join(history)
    prompt = f"""You are a helpful personal assistant. 
    Only respond as Agent. Do not generate User messages.
    Stop after your single response.

    {full_conversation}
    Agent:"""
        
    response = requests.post(
        "http://localhost:11434/api/generate",
        json = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    reply = response.json()["response"]
    history.append(f"Agent: {reply}")
    return reply


while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    elif user_input == "clear":
        history = []
        print("Memory cleared.")
        continue
    
    reply = chat(user_input)
    print(f"Agent: {reply}\n")






