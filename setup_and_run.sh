#!/bin/bash

# Function to handle errors
handle_error() {
    echo "Error occurred in step: $1"
    exit 1
}

# Step 1: Ensure pyenv is installed
echo "Checking if pyenv is installed..."
if ! command -v pyenv &>/dev/null; then
    echo "pyenv not found, installing..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Install pyenv on Linux
        curl https://pyenv.run | bash
        export PATH="$HOME/.pyenv/bin:$PATH"
        eval "$(pyenv init --path)"
        eval "$(pyenv init -)"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Install pyenv on macOS
        brew install pyenv
    else
        handle_error "Unsupported OS for pyenv installation"
    fi
else
    echo "pyenv is already installed."
fi

# Step 2: Install Python 3.12 using pyenv
echo "Installing Python 3.12 with pyenv..."
pyenv install 3.12 || handle_error "pyenv install 3.12"
pyenv shell 3.12 || handle_error "pyenv shell 3.12"

# Step 3: Ensure Poetry is installed
echo "Checking if Poetry is installed..."
if ! command -v poetry &>/dev/null; then
    echo "Poetry not found, installing..."
    curl -sSL https://install.python-poetry.org | python3 - || handle_error "Poetry installation"
else
    echo "Poetry is already installed."
fi

# Step 4: Configure Poetry for in-project virtualenv
echo "Configuring Poetry to create virtualenvs in the project directory..."
poetry config virtualenvs.in-project true || handle_error "Configuring Poetry"

# Step 5: Install project dependencies
echo "Installing project dependencies with Poetry..."
poetry install || handle_error "Poetry install"

# Step 6: Install pre-commit hooks
echo "Installing pre-commit hooks..."
poetry run pre-commit install || handle_error "Pre-commit install"

# Step 7: Activate the Poetry shell
echo "Activating Poetry shell..."
poetry shell || handle_error "Poetry shell"

# Step 8: Start the server using uvicorn
echo "Starting the server..."
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8081 --reload || handle_error "Starting the server"
