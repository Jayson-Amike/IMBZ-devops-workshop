import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    profiles = []
    # This ensures it always looks inside the same folder where app.py lives
    current_dir = os.path.dirname(os.path.abspath(__file__))
    profiles_dir = os.path.join(current_dir, "profiles")
    
    if os.path.exists(profiles_dir):
        for filename in os.listdir(profiles_dir):
            if filename.endswith(".json"):
                file_path = os.path.join(profiles_dir, filename)
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)
                        profiles.append(data)
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
                    
    return render_template("index.html", profiles=profiles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)