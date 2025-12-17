---
id: vla-integration
title: Chapter 5: The Mind (VLA)
sidebar_label: 5. VLA Integration
---

# Chapter 5: The Mind (Vision-Language-Action)

Traditional robots need explicit code: `move_to(x=10)`.
**Physical AI** understands intent: "Clean this room."

To bridge this gap, we use **Vision-Language-Action (VLA)** models. These are Large Multimodal Models (LMMs) trained to understand space and physics.

## The Architecture

1.  **Input**: Image + Text Command.
2.  **Model**: GPT-4o, Gemini 1.5 Pro, or specialized models like RT-2.
3.  **Output**: Structured JSON or Code.

## Prompt Engineering for Robots

You can't just ask "What do you see?". You must force the model to think like a robot controller.

```python
SYSTEM_PROMPT = """
You are a Robot Control AI.
Output Format: JSON
{
    "action": "PICK | PLACE | MOVE_TO",
    "coordinates": [x, y, z]
}
"""
```

## The VLA Client

We write a simple Python wrapper to send the simulation screenshot to the API.

```python
def analyze_scene(image_path, command):
    # 1. Encode Image
    # 2. Send to API with SYSTEM_PROMPT
    # 3. Parse JSON
    return json_plan
```

By receiving a structured JSON, our "Nervous System" (ROS 2) can now execute the "Mind's" decision!
