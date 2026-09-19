from openai import OpenAI

key = "Your_Gemini_API_Key" # Replace with your actual Gemini API key  

messages = []

client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" 
)


def completion(message):
    global messages

    # Add user's message
    messages.append({
        "role": "user",
        "content": message
    })

    chat_completion = client.chat.completions.create(
        model="gemini-3.8-flash",
        messages=messages
    ) 

    # Get Jarvis's response
    assistant_message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    # Add Jarvis's response to conversation history
    messages.append(assistant_message)

    print(f"Jarvis: {assistant_message['content']}")


if __name__ == "__main__":

    print("Jarvis: Hi I am Jarvis, your AI assistant. How can I help you today?")

    while True:
        user_question = input("You: ")

        if user_question.lower() == "exit":
            break

        completion(user_question)