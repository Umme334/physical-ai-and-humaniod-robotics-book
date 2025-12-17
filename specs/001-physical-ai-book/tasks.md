# Task List: Physical AI & Humanoid Robotics Book

**Feature Branch**: `001-physical-ai-book`
**Status**: In Progress

## Phase 1: Setup & Foundational Structure

*Goal: Initialize the book project structure and development environment.*

- [x] T001 Create book directory structure (docs/, examples/) in `book-content/`
- [x] T002 Initialize Docusaurus skeleton (or Markdown structure) in `book-content/`
- [x] T003 Create ROS 2 workspace structure in `book-content/examples/src`
- [x] T004 Implement .devcontainer for ROS 2 Humble in `book-content/examples/.devcontainer/devcontainer.json`
- [x] T005 Create Chapter 1 (Intro) conceptual content in `book-content/docs/01-intro/index.md`

## Phase 2: User Story 1 - Foundations & Nervous System

*Goal: Reader can install ROS 2 and run their first nodes.*

- [x] T006 [US1] Create ROS 2 "Hello World" package (my_robot_control) in `book-content/examples/src/my_robot_control`
- [x] T007 [US1] Implement simple Talker/Listener Python nodes in `book-content/examples/src/my_robot_control`
- [x] T008 [US1] Write Chapter 2 content explaining Nodes/Topics in `book-content/docs/02-ros2-basics/index.md`
- [x] T009 [US1] Add verify_install.py script to check environment in `book-content/examples/src/verify_install.py`

## Phase 3: User Story 2 - The Digital Body

*Goal: Reader can spawn a humanoid robot in Gazebo.*

- [x] T010 [US2] Create URDF description package (my_robot_description) in `book-content/examples/src/my_robot_description`
- [x] T011 [US2] Add basic humanoid URDF/XACRO file in `book-content/examples/src/my_robot_description/urdf/robot.urdf`
- [x] T012 [US2] Create Gazebo launch file to spawn robot in `book-content/examples/src/my_robot_description/launch/spawn_robot.launch.py`
- [x] T013 [US2] Write Chapter 3 content on URDF and Simulation in `book-content/docs/03-simulation/index.md`

## Phase 4: User Story 3 - The AI Brain

*Goal: Connect Isaac Sim to ROS 2 for movement control.*

- [x] T014 [US3] Create Isaac Sim python script for robot loading in `book-content/docs/04-isaac-sim/code/load_robot.py`
- [x] T015 [US3] Implement ROS 2 Bridge configuration in Isaac script in `book-content/docs/04-isaac-sim/code/ros2_bridge.py`
- [x] T016 [US3] Write Chapter 4 content on Isaac Sim and Bridges in `book-content/docs/04-isaac-sim/index.md`

## Phase 5: User Story 4 - Vision-Language-Action

*Goal: Use an API (VLA) to interpret a scene.*

- [x] T017 [US4] Create VLA client script using OpenAI/Gemini API in `book-content/docs/05-vla-integration/code/vla_client.py`
- [x] T018 [US4] Implement prompt engineering for robotic action output in `book-content/docs/05-vla-integration/code/prompts.py`
- [x] T019 [US4] Write Chapter 5 content on VLA concepts and API usage in `book-content/docs/05-vla-integration/index.md`

## Phase 6: User Story 5 - Capstone Integration

*Goal: Full pipeline: See -> Plan -> Move.*

- [x] T020 [US5] Create integration script linking VLA output to ROS 2 command in `book-content/docs/06-capstone/code/main_agent.py`
- [x] T021 [US5] Write Chapter 6 Capstone walkthrough in `book-content/docs/06-capstone/index.md`
- [x] T022 [US5] Create system architecture diagram in `book-content/docs/06-capstone/assets/architecture_diagram.png`

## Phase 7: Polish & Review

- [x] T023 Generate navigation/TOC map in `book-content/navigation.md`
- [x] T024 Review all code snippets against linting standards
- [x] T025 Verify all file paths in docs match the examples directory structure

## Dependencies

- US1 (ROS Basics) blocks all subsequent chapters.
- US2 (Body) blocks US3 (Brain) and US5 (Capstone).
- US3 (Brain) and US4 (VLA) can be developed in parallel, but both block US5.

## Parallel Execution Opportunities

- **Content vs Code**: One agent can write the Markdown content (T008, T013, T016...) while another implements the Python examples (T006, T010, T014...).
- **US3 & US4**: The Isaac Sim integration (US3) and VLA API logic (US4) are largely independent until the Capstone (US5).

## Implementation Strategy

1.  **Skeleton First**: Establish the directory structure and devcontainer (Phase 1).
2.  **Code-First Authoring**: For each chapter, write the *code* first to verify it works, then wrap the *text* around it.
3.  **Validation**: Use the `verify_install.py` style checks to ensure readers can follow along.
