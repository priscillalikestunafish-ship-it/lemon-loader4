from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/")
def index():
    # This is the web browser interface
    return render_template_string("""
        <!doctype html>
        <html>
        <head>
            <title>Lemon Loader</title>
            <style>
                body { margin: 0; background: #1ac0ff; color: white; font-family: system-ui; }
                iframe { width: 100%; height: 90vh; border: none; }
                #bar { background: #7b2ff7; padding: 10px; display: flex; gap: 10px; }
                input { flex: 1; padding: 8px; border-radius: 8px; border: none; }
                button { padding: 8px 12px; border: none; border-radius: 8px; background: white; color: #7b2ff7; font-weight: bold; }
            </style>
        </head>
        <body>
            <div id="bar">
                <input id="url" placeholder="Enter a website (ex: https://example.com)">
                <button onclick="go()">Go</button>
            </div>
            <iframe id="view" src=""></iframe>

            <script>
                function go() {
                    let url = document.getElementById('url').value.trim();
                    if (!url.startsWith('http')) {
                        url = 'https://' + url;
                    }
                    document.getElementById('view').src = url;
                }
            </script>
        </body>
        </html>
    """)

# --- Allow embedding ---
@app.after_request
def allow_iframe(resp):
    resp.headers["X-Frame-Options"] = "ALLOWALL"
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
