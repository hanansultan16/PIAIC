#!/usr/bin/env python
import google.generativeai as genai
from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start

# Set your Gemini API key
GENAI_API_KEY = "AIzaSyAzWXQh2DEWfKsMCSMPcNvFfDko28c36_M"  # Replace with your actual key
genai.configure(api_key=GENAI_API_KEY)

# Define the state
class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""

# Function to generate a poem using Gemini
def generate_poem_gemini(sentence_count):
    model = genai.GenerativeModel("gemini-pro")  # Use a valid Gemini model
    prompt = f"Write a {sentence_count}-line poem about nature."
    
    response = model.generate_content(prompt)
    
    if response and hasattr(response, "text"):
        return response.text.strip()
    return "Poem generation failed."

# Define the PoemFlow
class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count...")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem using Gemini...")
        self.state.poem = generate_poem_gemini(self.state.sentence_count)
        print("Poem generated:\n", self.state.poem)

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem...")
        with open("poem.txt", "w") as f:
            f.write(self.state.poem)
        print("Poem saved successfully!")

# Functions to start and plot the flow
def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()

def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()

# Run the script
if __name__ == "__main__":
    kickoff()
