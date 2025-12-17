# Research & Technical Validation: Physical AI Book

## Technology Stack Decisions

### 1. ROS 2 Distribution: Humble Hawksbill (LTS)
**Decision**: Use ROS 2 Humble Hawksbill.
**Rationale**: 
- Runs on Ubuntu 22.04, which is the current standard for many robotics tools.
- Widespread package support.
- Best compatibility with current NVIDIA Isaac Sim versions.
**Alternatives**: Jazzy Jalisco (too new, potential compatibility issues with Isaac), Foxy (EOL).

### 2. Simulation Strategy: Hybrid (Gazebo -> Isaac Sim)
**Decision**: 
- **Chapter 3 (Basics)**: Use **Gazebo Harmonic** (or Classic if Humble dictates) for the first "spawn a robot" tutorial. It's lightweight and installs with ROS.
- **Chapter 4+ (AI/Advanced)**: Use **NVIDIA Isaac Sim** for the AI/VLA chapters.
**Rationale**: 
- Accessibility: Gazebo works on almost any laptop. Isaac Sim requires an NVIDIA RTX GPU. This allows readers without high-end hardware to complete at least the first half of the book.
- Power: Isaac Sim is required for the "Brain" and VLA integration.

### 3. VLA Model: API-Based (OpenAI/Gemini)
**Decision**: Use Vision-Language APIs (e.g., GPT-4o, Gemini 1.5 Pro) for the VLA component.
**Rationale**: 
- **Hardware Constraints**: Running a true VLA (like OpenVLA) locally requires significant VRAM (24GB+).
- **Simplicity**: APIs are easier to integrate via Python `requests` or SDKs than setting up local inference servers.
- **Performance**: APIs offer SOTA reasoning capabilities.

### 4. Containerization: Devcontainer
**Decision**: Provide a `.devcontainer` configuration.
**Rationale**: 
- Solves "It works on my machine" issues.
- Standardizes the ROS 2 environment (Ubuntu 22.04 + Humble) regardless of the user's host OS (Windows/Mac).

## Chapter Outline validation

| Chapter | Key Tech | Outcome |
| :--- | :--- | :--- |
| 1. Concepts | Markdown | Theory understood. |
| 2. Nervous System | ROS 2 Humble, Python | "Hello World" nodes communicating. |
| 3. Digital Body | Gazebo, URDF | Robot visible in 3D space. |
| 4. AI Brain | NVIDIA Isaac Sim, ROS 2 Bridge | Robot moves via external command. |
| 5. VLA | OpenAI/Gemini API, Python | Script describes scene/plans action. |
| 6. Capstone | All above | "See cup -> Plan -> Move -> Grasp" (Simulated). |

## Unknowns Resolved
- **Hardware reqs**: Explicitly state "NVIDIA RTX GPU required for Chapters 4-6". Provide "Reading Mode" alternatives (videos) for those without.
- **OS**: Focus on Windows (WSL2) and Linux. Mac is "best effort" via Docker (no Isaac Sim support on Mac usually).
