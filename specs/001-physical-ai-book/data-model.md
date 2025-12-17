# Data Model: Book Structure

## Directory Layout

The book will be structured as a Docusaurus-ready project (or standard Markdown collection).

```text
book-content/
├── docs/
│   ├── 01-intro/
│   │   ├── index.md            # Chapter 1 text
│   │   └── assets/             # Diagrams/Images
│   ├── 02-ros2-basics/
│   │   ├── index.md
│   │   └── code/               # Runnable examples
│   ├── 03-simulation/
│   │   ├── index.md
│   │   └── assets/
│   ├── 04-isaac-sim/
│   │   ├── index.md
│   │   └── code/
│   ├── 05-vla-integration/
│   │   ├── index.md
│   │   └── code/
│   └── 06-capstone/
│       ├── index.md
│       └── code/
├── examples/                   # Standalone repo structure for users
│   ├── .devcontainer/          # Environment config
│   ├── src/                    # ROS 2 workspace
│   │   ├── my_robot_control/
│   │   └── my_robot_description/
│   └── README.md
└── navigation.md               # Table of Contents map
```

## Entities

### Chapter
- **Title**: String
- **Slug**: String (folder name)
- **Learning Objectives**: List[String]
- **Prerequisites**: List[String]
- **Content**: Markdown
- **Code Examples**: List[File]

### Code Example
- **Language**: Python (mostly), XML (URDF), YAML (Config)
- **Dependencies**: defined in `setup.py` or `package.xml`
- **Execution Command**: String (e.g., `ros2 run pkg node`)
