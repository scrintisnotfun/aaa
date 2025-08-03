from flask import Flask, jsonify, render_template_string
from app.bot import get_recent_pets

app = Flask(__name__)

HTML_NEXUS_STYLE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Pet Tracker</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

  body {
    margin: 0;
    height: 100vh;
    background-color: #0a0a0a;
    color: #ddd;
    font-family: 'Poppins', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    flex-direction: column;
    padding: 0 1rem;
  }

  h1 {
    font-weight: 900;
    font-size: 5rem;
    margin: 0;
  }

  .red {
    color: #e63946;
  }

  h1 .white {
    color: white;
  }

  p {
    font-weight: 400;
    font-size: 1.5rem;
    max-width: 700px;
    margin: 1rem auto 3rem auto;
    color: #bbb;
  }

  p .highlight {
    color: #e63946;
    font-weight: 600;
  }

  .btn-container {
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  a.btn {
    text-decoration: none;
    font-weight: 600;
    font-size: 1.125rem;
    padding: 1rem 2.5rem;
    border-radius: 8px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: background-color 0.3s ease, color 0.3s ease;
  }

  a.btn-primary {
    background-color: #e63946;
    color: white;
    border: none;
  }

  a.btn-primary:hover {
    background-color: #b32b33;
  }

  a.btn-outline {
    border: 2.5px solid #e63946;
    color: #e63946;
    background: transparent;
  }

  a.btn-outline:hover {
    background-color: #e63946;
    color: white;
  }

  /* Optional icons (you can replace with your own or font icons) */
  .icon-code::before {
    content: "</>";
    font-weight: 700;
    font-family: monospace;
  }

  .icon-gateway::before {
    content: "\\1F6A7"; /* construction cone emoji */
  }
</style>
</head>
<body>
  <h1>
    <span class="red">PET</span><span class="white">TRACKER</span>
  </h1>
  <p>
    The ultimate platform for <span class="highlight">real-time monitoring</span>, <span class="highlight">server updates</span>, and <span class="highlight">community engagement</span>.
  </p>
  <div class="btn-container">
    <a href="/recent-pets" class="btn btn-primary icon-code">Recent Pets</a>
    <a href="/ping" class="btn btn-outline icon-gateway">Ping Service</a>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_NEXUS_STYLE)

@app.route("/recent-pets")
def recent():
    return jsonify(get_recent_pets())

@app.route("/ping")
def ping():
    return "pong"
