#!/bin/bash
# Script per configurare l'ambiente virtuale Python su Ubuntu
# Setup script for Python virtual environment on Ubuntu

set -e  # Exit on error

echo "=== Python Exam Preparation - Virtual Environment Setup ==="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 using: sudo apt install python3 python3-venv python3-pip"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "Found: $PYTHON_VERSION"
echo ""

# Check if venv module is available
if ! python3 -m venv --help &> /dev/null; then
    echo "Error: python3-venv module is not installed."
    echo "Please install it using: sudo apt install python3-venv"
    exit 1
fi

# Create virtual environment
VENV_DIR="venv"
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists at ./$VENV_DIR"
    read -p "Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing virtual environment..."
        rm -rf "$VENV_DIR"
    else
        echo "Using existing virtual environment."
    fi
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in ./$VENV_DIR..."
    python3 -m venv "$VENV_DIR"
    echo "✓ Virtual environment created successfully"
fi

echo ""
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    echo ""
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
    echo "✓ Dependencies installed successfully"
else
    echo ""
    echo "Warning: requirements.txt not found. Skipping dependency installation."
fi

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "To activate the virtual environment in the future, run:"
echo "    source venv/bin/activate"
echo ""
echo "To deactivate the virtual environment, run:"
echo "    deactivate"
echo ""
echo "You can now run the examples:"
echo "    python examples/01_variables.py"
echo "    python examples/02_loops.py"
echo "    etc."
echo ""
