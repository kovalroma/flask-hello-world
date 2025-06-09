from flask import Flask, request, render_template
from datetime import datetime
import socket, subprocess, os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current date and time
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the IP address of the server
    server_hostname = request.host.split(':')[0]
    server_ip = subprocess.check_output(["hostname", "-I"], text=True)
    
    # Get background color from environment variable, default to white if not set
    background_color = os.environ.get('color', 'white')

    return render_template('index.html', 
                           current_date=current_date, 
                           server_hostname=server_hostname, 
                           server_ip=server_ip,
                           background_color=background_color)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
