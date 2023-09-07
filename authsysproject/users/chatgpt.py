import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
       response = openai.Completion.create(
           engine='text-davinci-003',
           prompt=prompt,
           max_tokens=100,
           temperature=0.7,
           n=1,
           stop=None,
           timeout=5
       )
       return response.choices[0].text.strip()

