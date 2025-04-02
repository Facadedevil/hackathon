from transformers import pipeline
import logging

class TitleGenerator:
    def __init__(self):
        try:
            self.generator = pipeline("text-generation", model="gpt2")
            self.model_loaded = True
        except Exception as e:
            logging.error(f"Failed to load GPT-2 model: {e}")
            self.model_loaded = False
    
    def generate_titles(self, summary, num_titles=3):
        if not summary:
            return ["Meeting Summary"]
            
        if not self.model_loaded:
            return ["Meeting Summary", "Call Summary", "Discussion Summary"]
            
        try:
            titles = []
            for _ in range(num_titles):
                prompt = f"Generate a concise title for a meeting summary: {summary[:100]}"
                result = self.generator(prompt, max_length=50, num_return_sequences=1)
                
                if result and isinstance(result, list) and len(result) > 0:
                    generated_text = result[0].get('generated_text', '')
                    title = generated_text.split('\n')[0].replace(prompt, '').strip()
                    
                    # If title is empty after processing, use a default
                    if not title:
                        title = f"Summary {_ + 1}"
                        
                    titles.append(title)
                else:
                    titles.append(f"Summary {_ + 1}")
                    
            # If we somehow ended up with no titles, return defaults
            if not titles:
                return ["Meeting Summary", "Call Summary", "Discussion Summary"]
                
            return titles
            
        except Exception as e:
            logging.error(f"Title generation error: {e}")
            return ["Meeting Summary", "Call Summary", "Discussion Summary"]