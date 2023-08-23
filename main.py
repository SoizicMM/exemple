from flask import Flask

app = Flask(__name__)

# Page Accueil
@app.route('/')
def index():
  return "changement collaborateur :D !"   

app.run(host='0.0.0.0', port=81)