@echo off
REM Check if conda is available
where conda >nul 2>nul
if %errorlevel% equ 0 (
    echo Conda found. Initializing conda...
    call conda init cmd.exe
    echo Setting up conda environment...
    call conda create --prefix .\.conda\ -y
    call conda activate .\.conda\
    echo Conda environment created and activated at .\conda\
    echo Installing packages with conda...
    call conda install -c conda-forge -y ipykernel Ipython sqlalchemy psycopg2-binary pandas matplotlib pylatex
    echo.
    echo Virtual environment setup complete!
    echo Use the kernel located at .\.conda\bin\python.exe
) else (
    echo Conda not found. Setting up Python venv instead...
    python -m venv .\.venv
    call .\.venv\Scripts\activate.bat
    echo Python virtual environment created and activated at .\venv\
    echo Installing packages with pip...
    python -m pip install ipykernel Ipython sqlalchemy psycopg2-binary pandas matplotlib pylatex
    echo.
    echo Virtual environment setup complete!
    echo Use the kernel located at .\.venv\bin\python.exe
)
echo Virtual environment setup complete!
pause