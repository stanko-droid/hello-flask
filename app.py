from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Välkommen till min Flask-app</h1><p>Gå till <a href="/about">Om mig</a></p>'
    return 'Hej, världen!'

@app.route('/about')
def about():
    return 'Detta är sidan om mig!'

@app.route('/api/profile')
def profile():
    # Detta är en Python "Dictionary" (nyckel-värde-par)
    data = {
        "namn": "Ditt Namn",
        "roll": "DevOps Student",
        "skills": ["Python", "Flask", "Git"],
        "aktiv": True
    }
    # jsonify gör om dictionaryn till JSON-format som webben förstår
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)