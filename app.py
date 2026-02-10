from flask import Flask, render_template, request
from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Initialize OpenAI client securely
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

JUNG_PROMPT = """
You are a Jungian dream analyst.
Interpret dreams using Carl Jung's analytical psychology.
Focus on archetypes, symbols, the collective unconscious,
and the process of individuation.
"""

@app.route("/", methods=["GET", "POST"])
def index():
    interpretation = None
    image_data = None

    if request.method == "POST":
        dream = request.form["prompt"]

        try:
            # ---- TEXT INTERPRETATION ----
            text_response = client.responses.create(
                model="gpt-4.1",
                input=[
                    {"role": "system", "content": JUNG_PROMPT},
                    {"role": "user", "content": dream}
                ],
                temperature=0.8,
                max_output_tokens=250
            )

            interpretation = text_response.output_text

            # ---- IMAGE GENERATION ----
            image_prompt = f"""
            A surreal dream scene inspired by Jungian psychology.
            Symbolic, abstract, and emotionally rich imagery
            representing this dream interpretation:
            {interpretation}
            """

            image_response = client.images.generate(
                model="gpt-image-1",
                prompt=image_prompt,
                size="1024x1024"
            )

            # Convert base64 to displayable image
            image_base64 = image_response.data[0].b64_json
            image_data = f"data:image/png;base64,{image_base64}"

        except Exception as e:
            interpretation = f"Error: {str(e)}"

    return render_template(
        "index.html",
        interpretation=interpretation,
        image_data=image_data
    )

if __name__ == "__main__":
    app.run(debug=True)
