from flask import Flask
import psutil
import platform

app = Flask(__name__)

@app.route("/")
def info():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "platform": platform.platform()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0")
