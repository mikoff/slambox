#!/bin/bash

# Check if the "development" virtual environment is active
if [[ "$VIRTUAL_ENV" != "$HOME/venv/development" ]]; then
  source "$HOME/venv/development/bin/activate"
fi

# Append the contents of /home/developer/symforce.env to PYTHONPATH
if [ -r /home/developer/symforce.env ]; then
  # For a single path:
  export PYTHONPATH="${PYTHONPATH}:$(< /home/developer/symforce.env)"
fi