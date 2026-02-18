#!/bin/bash

# Check if conda is available
#!/bin/bash

# Check if conda is available
if command -v conda &> /dev/null; then
    echo "Conda found. Initializing conda..."
    conda init bash
    echo "Setting up conda environment..."
    conda create --prefix ./.conda/ -y
    conda activate ./.conda/
    echo "Conda environment created and activated at ./.conda/"
    echo "Installing packages with conda..."
    conda install -c conda-forge -y ipykernel Ipython sqlalchemy psycopg2-binary pandas matplotlib pylatex
    echo ""
    echo "Virtual environment setup complete!"
    echo "Use the kernel located at ./.conda/bin/python"
else
    echo "Conda not found. Setting up Python venv instead..."
    python -m venv ./.venv
    source ./.venv/bin/activate
    echo "Python virtual environment created and activated at ./.venv/"
    echo "Installing packages with pip..."
    python -m pip install ipykernel Ipython sqlalchemy psycopg2-binary pandas matplotlib pylatex
    echo ""
    echo "Virtual environment setup complete!"
    echo "Use the kernel located at ./.venv/bin/python"
fi

echo "Virtual environment setup complete!"