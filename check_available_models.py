import os
from groq import Groq

# Set your API key if it's not already set in your environment variables
# os.environ["GROQ_API_KEY"] = "your_groq_api_key_here"

client = Groq()

try:
    # Fetch all models accessible by your account/tier
    models = client.models.list()

    print(f"{'MODEL ID':<40} | {'CREATED BY':<15} | {'ACTIVE'}")
    print("-" * 70)

    for model in models.data:
        # Filter for active models
        if getattr(model, "active", True):
            print(f"{model.id:<40} | {model.owned_by:<15} | {model.active}")

except Exception as e:
    print(f"Error listing models: {e}")