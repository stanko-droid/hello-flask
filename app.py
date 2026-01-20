from flask import Flask, jsonify
import os  # <--- NYTT: Vi importerar 'os' för att kunna hitta filer

app = Flask(__name__)

@app.route('/')
def hello():
    # Här försöker vi läsa innehållet i din footer-fil
    try:
        with open('content/_footer.md', 'r', encoding='utf-8') as f:
            footer_content = f.read()
    except FileNotFoundError:
        footer_content = "Kunde inte hitta sidfoten..."

    # Vi bygger ihop HTML-koden + footer-texten
    # <hr> betyder "Horizontal Rule" (ett streck)
    # <pre> gör att texten behåller sina radbrytningar
    html_code = f"""
    <h1>Välkommen till min Flask-app</h1>
    <p>Gå till <a href="/about">Om mig</a></p>
    <br>
    <hr>
    <footer>
        <pre>{footer_content}</pre>
    </footer>
    """
    return html_code

@app.route('/about')
def about():
    return 'Detta är sidan om mig!'

@app.route('/api/profile')
def profile():
    data = {
        "namn": "Ditt Namn",
        "roll": "DevOps Student",
        "skills": ["Python", "Flask", "Git"],
        "aktiv": True
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)