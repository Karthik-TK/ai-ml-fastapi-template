# AI/ML - FastAPI Template

This repository provides a comprehensive starter template for building AI/ML applications using FastAPI, designed to take you from PoC to production-ready seamlessly. It includes essential features like logging, configuration management, and best practices to help you quickly develop, test, and deploy AI/ML models with confidence.

Whether you're prototyping a new model or building a scalable production API, this template has you covered. It provides a robust foundation with built-in tools for logging, environment management, and more, to ensure smooth transitions through every stage of development.

## Features

- **FastAPI:** High-performance web framework for building APIs.
- **Logging:** Integrated logging setup to track application activity and errors.
- **Configuration Management:** Supports flexible configuration using environment variables or .env files.
- **Pre-commit hooks:** Ensures code quality with pre-configured hooks.
- **Uvicorn:** ASGI server for serving FastAPI apps, supporting hot-reload during development.
- **Poetry:** Dependency management and virtual environment setup.
- **Pyenv:** Python version management to ensure consistent development environments.
- **AI/ML Model Integration:** Template for integrating AI/ML models with FastAPI endpoints.

## Project structure

```bash
.
├── app/
│   ├── __init__.py
│   ├── api/               # API routes
│   ├── models/            # ML model loading and inference
│   ├── utils/             # Helper functions (logging, config, etc.)
│   └── main.py            # FastAPI app initialization
├── .env                   # Environment variables for local development
├── pyproject.toml         # Poetry configuration
├── README.md              # Project documentation
├── setup_and_run.bat      # Windows Shell script to set up the project
└── setup_and_run.sh       # Linux/MacOS Shell script to set up the project
```

## Getting Started

### Run Locally

#### 1. Setup and Run Script Linux/macOS:

```bash
chmod +x setup_and_run.sh
```

```bash
./setup_and_run.sh
```

#### 2. Setup and Run Script Windows:

```bash
setup_and_run.bat
```

### Docker Deployment

To deploy the project using Docker, follow these steps:

1. Build the Docker image:

```bash
  docker build -t app .
```

2. Run the Docker container:

```bash
  docker run -t -i -p 80:80 --restart=always app &
```

## Contributing

I welcome contributions from everyone! If you have ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT. See the [LICENSE](#LICENSE) file for details.
