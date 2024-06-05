from flask import Flask, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current date and time
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the IP address of the server
    server_ip = request.host.split(':')[0]

    return render_template('index.html', current_date=current_date, server_ip=server_ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
