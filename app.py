from flask import Flask, request, render_template
import os
import yaml
from dotenv import load_dotenv
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

app = Flask("FitAI Trainer")

# GitHub Models API setup
endpoint = "https://models.github.ai/inference"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Load prompt configuration from .prompt.yml
with open(".prompt.yml", "r") as file:
    prompt_config = yaml.safe_load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    workout_plan = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            # Prepare messages from the prompt configuration
            messages = [
                {"role": msg["role"], "content": msg["content"].replace("{{input}}", user_input)}
                for msg in prompt_config["messages"]
            ]
            response = client.complete(
                messages=messages,
                temperature=prompt_config["modelParameters"]["temperature"],
                model=prompt_config["model"]
            )
            workout_plan = response.choices[0].message.content
    return render_template("index.html", workout_plan=workout_plan)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True) 