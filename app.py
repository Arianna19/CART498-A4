from flask import Flask, render_template, request, send_file
from openai import OpenAI
from dotenv import load_dotenv
import base64
import os
import io

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# In-memory image storage (simple + safe)
generated_image_bytes = None

JUNG_PROMPT = """
You are a Jungian dream analyst.
Interpret dreams using Carl Jung's analytical psychology.
Focus on symbols, archetypes, the unconscious, and individuation.
Write clearly and thoughtfully.
Ask a question depending on the analysis given about how the user is doing. 
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global generated_image_bytes

    dream_text = None
    interpretation = None
    image_ready = False

    if request.method == "POST":
        dream_text = request.form["prompt"]

        try:
            # ---- TEXT INTERPRETATION ----
            text_response = client.responses.create(
                model="gpt-4.1",
                input=[
                    {"role": "system", "content": JUNG_PROMPT},
                    {"role": "user", "content": dream_text}
                ],
                max_output_tokens=180,
                temperature=0.7
            )

            interpretation = text_response.output_text

            # ---- IMAGE GENERATION ----
            image_response = client.images.generate(
                model="gpt-image-1",
                prompt=f"Surreal dream imagery inspired by this dream infused with kawaii style: {dream_text}",
                size="auto"
            )

            image_base64 = image_response.data[0].b64_json
            generated_image_bytes = base64.b64decode(image_base64)
            image_ready = True

        except Exception:
            interpretation = "An error occurred while analyzing the dream."

    return render_template(
        "index.html",
        dream_text=dream_text,
        interpretation=interpretation,
        image_ready=image_ready
    )

@app.route("/image")
def image():
    global generated_image_bytes

    if generated_image_bytes is None:
        return "No image available", 404

    return send_file(
        io.BytesIO(generated_image_bytes),
        mimetype="image/png"
    )

if __name__ == "__main__":
    app.run(debug=True)
