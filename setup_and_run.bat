@echo off
setlocal EnableDelayedExpansion

:: Function to handle errors
call :handle_error "Starting"

:: Step 1: Ensure pyenv is installed
echo Checking if pyenv is installed...
where pyenv >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo pyenv not found, installing...
    echo Installing pyenv...
    powershell -Command "Invoke-WebRequest https://pyenv.run | Invoke-Expression" || call :handle_error "pyenv installation"
) else (
    echo pyenv is already installed.
)

:: Step 2: Install Python 3.12 using pyenv
echo Installing Python 3.12 with pyenv...
pyenv install 3.12 || call :handle_error "pyenv install 3.12"
pyenv shell 3.12 || call :handle_error "pyenv shell 3.12"

:: Step 3: Ensure Poetry is installed
echo Checking if Poetry is installed...
where poetry >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Poetry not found, installing...
    powershell -Command "Invoke-WebRequest https://install.python-poetry.org | Invoke-Expression" || call :handle_error "Poetry installation"
) else (
    echo Poetry is already installed.
)

:: Step 4: Configure Poetry for in-project virtualenv
echo Configuring Poetry to create virtualenvs in the project directory...
poetry config virtualenvs.in-project true || call :handle_error "Configuring Poetry"

:: Step 5: Install project dependencies
echo Installing project dependencies with Poetry...
poetry install || call :handle_error "Poetry install"

:: Step 6: Install pre-commit hooks
echo Installing pre-commit hooks...
poetry run pre-commit install || call :handle_error "Pre-commit install"

:: Step 7: Activate the Poetry shell
echo Activating Poetry shell...
poetry shell || call :handle_error "Poetry shell"

:: Step 8: Start the server using uvicorn
echo Starting the server...
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8081 --reload || call :handle_error "Starting the server"

goto :eof

:: Error handling subroutine
:handle_error
echo Error occurred in step: %1
exit /b 1
