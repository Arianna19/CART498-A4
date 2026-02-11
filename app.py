from flask import Flask, render_template, request
from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

JUNG_PROMPT = """
You are a Jungian dream analyst.
Analyze dreams using Carl Jung's analytical psychology.
Focus on archetypes, symbolism, the collective unconscious,
and individuation. Write clearly and reflectively.
"""

@app.route("/", methods=["GET", "POST"])
def index():
    interpretation = None
    image_url = None

    if request.method == "POST":
        dream = request.form["prompt"]

        try:
            # ---- TEXT ANALYSIS ----
            text_response = client.responses.create(
                model="gpt-4.1",
                input=[
                    {"role": "system", "content": JUNG_PROMPT},
                    {"role": "user", "content": dream}
                ],
                max_output_tokens=150,
                temperature=0.7
            )

            interpretation = text_response.output_text

            # ---- IMAGE GENERATION ----
            image_prompt = f"""
            Surreal dream imagery inspired by Jungian psychology.
            Symbolic, emotional, painterly style.
            Dream description:
            {dream}
            """

            image_response = client.images.generate(
                model="gpt-image-1",
                prompt=image_prompt,
                size="auto"
            )

            image_base64 = image_response.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            # Save image safely to static folder
            image_path = "static/dream.png"
            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_url = "/" + image_path

        except Exception as e:
            interpretation = f"Error: {str(e)}"

    return render_template(
        "index.html",
        interpretation=interpretation,
        image_url=image_url
    )

if __name__ == "__main__":
    app.run(debug=True)
