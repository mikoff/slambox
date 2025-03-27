#!/usr/bin/env python3
 
import json5
import os
import re
 
# Path to conanrun.sh and VS Code settings.json
conanrun_path = "build/generators/conanrunenv-release-x86_64.sh"
settings_path = ".vscode/settings.json"
 
# Extract PYTHONPATH from conanrun.sh
def extract_pythonpath(conanrun_file):
    with open(conanrun_file, "r") as file:
        content = file.read()
    match = re.search(r'export PYTHONPATH="([^"]+)"', content)
    if match:
        paths = match.group(1).split(":")
        return [p for p in paths if p and p != "$PYTHONPATH"]
    return []
 
# Update python.analysis.extraPaths in VS Code settings
def update_vscode_settings(python_paths, settings_file):
    if not os.path.exists(settings_file):
        os.makedirs(os.path.dirname(settings_file), exist_ok=True)
        settings = {}
    else:
        with open(settings_file, "r") as file:
            settings = json5.load(file)
 
    extra_paths = settings.get("python.analysis.extraPaths", [])
    for path in python_paths:
        if path not in extra_paths:
            extra_paths.append(path)
 
    settings["python.analysis.extraPaths"] = extra_paths
 
    with open(settings_file, "w") as file:
        json5.dump(settings, file, indent=4)
 
# Run extraction and update
python_paths = extract_pythonpath(conanrun_path)
if python_paths:
    update_vscode_settings(python_paths, settings_path)
    print("Updated python.analysis.extraPaths with:", python_paths)
else:
    print("No PYTHONPATH found in conanrun.sh.")
