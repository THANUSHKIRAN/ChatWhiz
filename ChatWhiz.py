import openai
import gradio as gr



openai.api_key = "CHAT_GPT API KEY"

messages = [{"role": "system", "content": "Enter your message and ChatWhiz will respond"}]

def chat(Question):
    messages.append({"role": "user", "content": Question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply


iface = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="ChatWhiz - Chatbot",
    description="ChatWhiz is here to assist you!",
    examples=[
        ["Tell me a joke."],
        ["What is Devops?"],
        ["Can you recommend a good book?"],
    ],
    theme="default"
)

iface.launch()
