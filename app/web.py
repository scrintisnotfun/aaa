from flask import Flask, jsonify, render_template_string
from app.bot import get_recent_pets

app = Flask(__name__)

HTML_DARK_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Pet Tracker</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron&display=swap');
  body {
    margin: 0; 
    background: #121212; 
    color: #e63946; 
    font-family: 'Orbitron', monospace, sans-serif; 
    display: flex; 
    flex-direction: column; 
    min-height: 100vh; 
    align-items: center; 
    justify-content: center;
    overflow-x: hidden;
  }
  h1 {
    font-size: 4rem;
    background: linear-gradient(90deg, #e63946, #fca311, #e63946);
    background-size: 200% 200%;
    animation: gradientMove 3s ease infinite;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow:
      0 0 5px #e63946,
      0 0 10px #fca311;
    margin-bottom: 0.5rem;
  }
  @keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
  }
  p {
    font-size: 1.25rem;
    text-align: center;
    max-width: 600px;
    color: #aaa;
    text-shadow: 0 0 5px #660000;
  }
  footer {
    margin-top: auto;
    padding: 1rem;
    font-size: 0.9rem;
    color: #770000;
    text-align: center;
  }
  /* subtle animated background effect */
  body::before {
    content: "";
    position: fixed;
    top: -20%;
    left: -20%;
    width: 140vw;
    height: 140vh;
    background: radial-gradient(circle at center, #3a0e0e, transparent 60%);
    opacity: 0.15;
    animation: pulse 5s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: -1;
  }
  @keyframes pulse {
    0% {opacity: 0.1;}
    100% {opacity: 0.25;}
  }
</style>
</head>
<body>
  <h1>Pet Tracker</h1>
  <p>Tracking your pets in real-time with a sleek dark and red theme.</p>
  <footer>© 2025 Your Bot</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_DARK_PAGE)

@app.route("/recent-pets")
def recent():
    return jsonify(get_recent_pets())

@app.route("/ping")
def ping():
    return "pong"
