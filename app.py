from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role":"system","content":"you are a automotive software designer"},
        {"role":"user","content":"Can you explain what is the need of autosar"}
    ],
    temperature=1,
    max_tokens=1024
)

print(completion.choices[0].message.content)