from openai import OpenAI

client = OpenAI()

prompt = "Please generate a JSON list of 50 descriptions of diverse human portraits. Each description should specify attributes such as age, gender, ethnicity, hair and eye color, facial expression, and visible teeth. Include a brief description of the background for each portrait. Give this info as diffusion prompt. only describe the portraits, do not include any other information."

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant and answer with JSON format."},
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

json_list = completion.choices[0].message.content

with open("portraits.json", "w") as f:
    f.write(json_list)