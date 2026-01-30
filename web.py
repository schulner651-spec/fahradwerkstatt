from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚲 Fahrradwerkstatt</h1>
    <p>Willkommen! Wir melden uns per E-Mail. TEST SEITE!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
