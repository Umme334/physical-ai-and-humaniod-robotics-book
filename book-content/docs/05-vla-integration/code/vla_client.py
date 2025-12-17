# vla_client.py
import os
import json
# import openai  # Uncomment when using real API
from prompts import SYSTEM_PROMPT

class VLAClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
    
    def analyze_scene(self, image_path, user_command):
        """
        Sends image and command to VLA model (e.g. GPT-4o).
        Returns structured JSON plan.
        """
        print(f"👀 Analyzing {image_path} with command: '{user_command}'...")
        
        # --- MOCK RESPONSE FOR TUTORIAL ---
        # In a real app, you would encode the image to base64 and hit the API.
        # response = client.chat.completions.create(...)
        
        mock_response = {
            "thought": "I see a blue cube on the floor.",
            "target_object": "blue_cube",
            "action": "MOVE_TO",
            "coordinates": [1.0, 0.5, 0.0]
        }
        
        print("🤖 VLA Output:", json.dumps(mock_response, indent=2))
        return mock_response

if __name__ == "__main__":
    client = VLAClient()
    client.analyze_scene("test_scene.jpg", "Go to the blue cube")
