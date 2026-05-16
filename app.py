from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # קריאת משתנה סביבה שיגיע מה-Secret של קוברנטיס
    secret_key = os.environ.get('MY_APP_SECRET', 'No secret found')
    return f"Hello from Minikube!The secret is: {secret_key}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)