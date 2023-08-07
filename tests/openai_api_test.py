import openai

openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Translate the following English text to Chinese: '{ I want to eat you!}'",
  max_tokens=60
)

print(response.choices[0].text.strip())