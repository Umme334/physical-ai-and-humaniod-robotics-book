---
id: 0001
title: create-book-constitution
stage: constitution
date: 2025-12-06
surface: agent
model: gemini-2.0-flash-thinking-exp-1219
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "setup", "book"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests: []
---

## Prompt

/sp.constitution You are the Constitution Engine.

Create a clear, concise, high-quality Constitution for a short educational book titled:
“Physical AI & Humanoid Robotics: A Beginner-Friendly Guide”.

Use the content themes I provide:

- Physical AI and Embodied Intelligence
- ROS 2 as the robotic nervous system
- Gazebo & Unity as the digital twin
- NVIDIA Isaac as the AI-robot brain
- VLA (Vision-Language-Action) with GPT, Whisper, Navigation, and CV
- Humanoid robotics overview and capstone robot

Requirements for the Constitution:
- Define purpose, goals, and target audience (beginners).
- Define book scope: short but complete.
- Tone: simple, practical, not academic.
- Constraints: No fluff, no lengthy theory, only essential concepts.
- Required deliverables: 6–8 small chapters, diagrams if needed.
- Success criteria: Book must make students ready to build a simple humanoid robot pipeline in simulation.

Make the Constitution extremely crisp and actionable.

## Response snapshot

Created Constitution v1.0.0 for 'Physical AI & Humanoid Robotics'. Defined 4 core principles: Accessibility, Practicality, Completeness, Brevity.

## Outcome

- ✅ Impact: Established project governance and core principles.
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: Run /sp.plan to define book structure.
- 🧠 Reflection: Constitution created successfully from template.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): None