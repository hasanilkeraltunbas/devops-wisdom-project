# frontend/app.py
import os
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

# Backend service discovery via environment variables (12-factor app principle)
# Defaults to localhost for local development, overwritten in Kubernetes
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8080")

@app.route("/")
def index():
    quote = "Backend'e ulaşılamadı..."
    author = "Bilinmiyor"
    
    try:
        # Inter-service communication within the cluster
        response = requests.get(f"{BACKEND_URL}/quote", timeout=2)
        if response.status_code == 200:
            data = response.json()
            quote = data.get("text")
            author = data.get("author")
    except Exception as e:
        print(f"Hata: {e}")

    # Simple UI Template for demonstration
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Wisdom</title>
        <style>
            body {{ font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f0f2f5; }}
            .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: inline-block; max-width: 600px; }}
            h1 {{ color: #333; }}
            p {{ font-size: 1.2em; color: #555; }}
            .author {{ font-style: italic; color: #888; margin-top: 10px; display: block; }}
            button {{ background-color: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin-top: 20px; }}
            button:hover {{ background-color: #0056b3; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>💡 Günün Sözü</h1>
            <p>"{quote}"</p>
            <span class="author">- {author}</span>
            <br>
            <button onclick="window.location.reload();">Yeni Söz Getir</button>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)