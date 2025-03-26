#!/usr/bin/env python3
import json5
import json
import sys

SETTINGS_FILE = "/workspace/.vscode/settings.json"  # update path
SYMFORCE_FILE = "/home/developer/symforce.env"

# Load the new path
with open(SYMFORCE_FILE, "r") as f:
    new_path = f.read().strip()

# Load the settings.json (supports trailing commas/comments)
with open(SETTINGS_FILE, "r") as f:
    data = json5.load(f)

# Ensure the key exists and update it if needed
extra_paths = data.get("python.analysis.extraPaths", [])
if new_path not in extra_paths:
    extra_paths.append(new_path)
    data["python.analysis.extraPaths"] = extra_paths
    # Write back standard JSON (comments/trailing commas will be removed)
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Appended '{new_path}' to python.analysis.extraPaths.")
else:
    print(f"Path '{new_path}' already exists.")