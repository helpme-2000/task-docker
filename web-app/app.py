import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    chars = "qwertyuiopasdfghjklzxcvbnm!@#$%^&*()?"
    password = "".join(random.choice(chars) for _ in range(12))
    return f"""
        <h1>{password}</h1>
	<button onclick="window.location.reload();">start</button>
    	"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6666)
