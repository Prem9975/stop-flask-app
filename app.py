from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess
import getpass

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Your Full Name"  # Replace with your real name
    user = getpass.getuser()
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata'))
    server_time = ist_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Run top command (first few lines)
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -30", shell=True, text=True)
    except Exception as e:
        top_output = f"Error running top: {str(e)}"
    
    return f"""
    <pre>
    Name: {name}
    User: {user}
    Server Time (IST): {server_time}
    TOP output:
    {top_output}
    </pre>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
