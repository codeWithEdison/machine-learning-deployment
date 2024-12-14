#!/usr/bin/env bash
set -o errexit

# Upgrade pip and install dependencies in specific order
python -m pip install --upgrade pip
pip install --no-cache-dir numpy==1.24.3
pip install --no-cache-dir -r requirements.txt

# Verify installations
python -c "import numpy; print('NumPy version:', numpy.__version__)"
python -c "import sklearn; print('Scikit-learn version:', sklearn.__version__)"