from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime
import webbrowser
import threading

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>MarketingFXTrade</title>
  <style>
    body { background: black; color: white; font-family: sans-serif; }
    .text-center { text-align: center; }
    .p-6 { padding: 1.5rem; }
    .card { background: #333; padding: 1rem; margin: 1rem; border-radius: 8px; }
    .tabs button { margin: 0.5rem; }
    .tab-content { display: none; }
    .tab-content.active { display: block; }
    input, button { margin: 0.5rem 0; padding: 0.5rem; width: 100%; max-width: 300px; }
    form { display: flex; flex-direction: column; align-items: center; }
  </style>
</head>
<body>
  <header class=\"text-center p-6\">
    <h1 class=\"text-4xl font-bold\">MarketingFXTrade</h1>
    <p class=\"text-lg\">Trade Forex, Crypto & CFDs with Confidence</p>
    <a href=\"/register\">Get Started</a>
  </header>

  <section class=\"features text-center\">
    <div class=\"card\">
      <h3>Low Spreads</h3>
      <p>Trade with spreads from 0.0 pips on major pairs.</p>
    </div>
    <div class=\"card\">
      <h3>Fast Execution</h3>
      <p>Lightning-fast trade execution with STP/DMA tech.</p>
    </div>
    <div class=\"card\">
      <h3>Secure Trading</h3>
      <p>Regulated environment with full data encryption.</p>
    </div>
  </section>

  <section class=\"accounts text-center\">
    <h2>Account Types</h2>
    <div class=\"tabs\">
      <button onclick=\"showTab('standard')\">Standard</button>
      <button onclick=\"showTab('vip')\">VIP</button>
      <button onclick=\"showTab('pro')\">Pro</button>
    </div>
    <div id=\"standard\" class=\"tab-content active\">
      <ul>
        <li>1:200 Leverage</li>
        <li>Spreads from 1.5 pips</li>
        <li>$100 Min Deposit</li>
      </ul>
    </div>
    <div id=\"vip\" class=\"tab-content\">
      <ul>
        <li>1:400 Leverage</li>
        <li>Spreads from 0.8 pips</li>
        <li>$1,000 Min Deposit</li>
      </ul>
    </div>
    <div id=\"pro\" class=\"tab-content\">
      <ul>
        <li>1:500 Leverage</li>
        <li>Spreads from 0.1 pips</li>
        <li>$5,000 Min Deposit</li>
      </ul>
    </div>
  </section>

  <section class=\"register text-center\">
    <h2>Sign Up Now</h2>
    <form action=\"/register\" method=\"POST\">
      <input name=\"name\" placeholder=\"Full Name\" required>
      <input name=\"email\" type=\"email\" placeholder=\"Email Address\" required>
      <input name=\"password\" type=\"password\" placeholder=\"Password\" required>
      <button type=\"submit\">Register</button>
    </form>
  </section>

  <footer class=\"text-center\">
    &copy; {{ year }} MarketingFXTrade. All rights reserved. |
    <a href=\"/\">Return Home</a> |
    <a href=\"http://127.0.0.1:5000\">Click here to open your broker site</a>
  </footer>

  <script>
    function showTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, year=datetime.now().year)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(f"Registered: {name}, {email}")
        return redirect(url_for('home'))
    return render_template_string(HTML_TEMPLATE, year=datetime.now().year)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.25, open_browser).start()
    app.run(debug=True)
