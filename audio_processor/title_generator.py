from transformers import pipeline

class TitleGenerator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt2")
    
    def generate_titles(self, summary, num_titles=3):
        titles = []
        for _ in range(num_titles):
            prompt = f"Generate a concise title for a meeting summary: {summary[:100]}"
            result = self.generator(prompt, max_length=50, num_return_sequences=1)
            title = result[0]['generated_text'].split('\n')[0].replace(prompt, '').strip()
            titles.append(title)
        return titles