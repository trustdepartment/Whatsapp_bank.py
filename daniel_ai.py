import gradio as gr
from groq import Groq

API_KEY = "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"
client = Groq(api_key=API_KEY)

def chat_fn(message, history):
    low = message.lower()
    if "who created you" in low or "who made you" in low:
        return "I am DANIEL SOMTO AI - WORLD INSTANT, created by Daniel Somto from Ufuma, Anambra State, Nigeria! 🌍"

    msgs = [{"role": "system", "content": "You are DANIEL SOMTO AI WORLD INSTANT created by Daniel Somto from Ufuma Nigeria. Answer any question. Never say OpenAI."}]

    for item in history:
        if isinstance(item, dict):
            r = item.get("role")
            c = item.get("content")
            if r and c:
                msgs.append({"role": r, "content": str(c)})
        elif isinstance(item, (list, tuple)) and len(item) >= 2:
            if item[0]: msgs.append({"role": "user", "content": str(item[0])})
            if item[1]: msgs.append({"role": "assistant", "content": str(item[1])})

    msgs.append({"role": "user", "content": message})

    resp = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=msgs,
        max_tokens=1500
    )
    return resp.choices[0].message.content

gr.ChatInterface(
    fn=chat_fn,
    title="🌍 DANIEL SOMTO AI - WORLD INSTANT",
    description="Created by Daniel Somto from Ufuma"
).launch(share=True)