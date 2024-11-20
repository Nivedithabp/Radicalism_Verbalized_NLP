import requests
import gradio as gr
import json
from langdetect import detect

LLAMA_API_URL = "http://localhost:11434/api/generate"

# Function to classify cognitive bias
def classify_cognitive_bias(user_input):
    try:
        # Detect language
        detected_language = detect(user_input)
        language_instruction = "Respond in French." if detected_language == "fr" else "Respond in English."
        
        # Define the prompt
        prompt = f"""
        Analyze the following statement:
        '{user_input}'
        
        Identify the most likely cognitive bias from the following list:
        - Confirmation Bias, Groupthink, Ingroup Bias, Outgroup Homogeneity Bias, Authority Bias, Bandwagon Effect, Availability Heuristic, Anchoring Bias, Black-and-White Thinking (False Dichotomy), Framing Effect, Moral Licensing, Negativity Bias, Overconfidence Effect, Projection Bias, Halo Effect, Self-Serving Bias, Hindsight Bias, Stereotyping, Hostile Attribution Bias, Fear-Based Bias, Recency Bias, Polarization Effect, Cognitive Dissonance, Appeal to Emotion Bias, Hyperbolic Discounting, Sunk Cost Fallacy, Dehumanization Bias, Anchoring on Identity, Belief Perseverance, Tribalism Bias
        
        Provide a response with the bias name and a brief explanation.

        {language_instruction}
        """
        
        print(f"[DEBUG] Prompt sent to LLaMA API: {prompt}")

        # Make POST request to LLaMA API
        response = requests.post(
            LLAMA_API_URL,
            json={"model": "llama3.2", "prompt": prompt},
            stream=True
        )

        # Ensure the request was successful
        response.raise_for_status()

        # Decode and assemble the response
        assembled_response = ""
        for chunk in response.iter_lines():
            if chunk:
                try:
                    chunk_data = json.loads(chunk.decode('utf-8'))
                    assembled_response += chunk_data.get("response", "")
                except (json.JSONDecodeError, AttributeError) as e:
                    print(f"[WARNING] Failed to parse chunk: {chunk}. Error: {e}")

        print(f"[DEBUG] Assembled Response: {assembled_response}")
        return assembled_response.strip()

    except Exception as e:
        print(f"[ERROR] Failed to process request: {e}")
        return "Sorry, an error occurred while processing your request."

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## Cognitive Bias Classifier")
    gr.Markdown("Provide a statement, and the app will classify the cognitive bias based on the list in 'bias_list.txt'.")
    
    chatbot = gr.Chatbot()
    text_input = gr.Textbox(placeholder="Enter your statement here...")
    send_button = gr.Button("Send")

    def interact(user_input, chat_history):
        response = classify_cognitive_bias(user_input)
        chat_history.append((user_input, response))
        return chat_history, ""

    send_button.click(interact, [text_input, chatbot], [chatbot, text_input])

# Launch
demo.launch()
