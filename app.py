
import os
import socket
import json
import time
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# AWS EC2 server configuration
SERVER_IP = os.environ.get("SERVER_IP", "16.178.83.139")
TCP_PORT = 5000
UDP_PORT = 5001

MAX_FILE_SIZE = 50 * 1024 * 1024


def receive_line(sock):
    data = b""

    while True:
        char = sock.recv(1)

        if not char:
            raise ConnectionError("Server disconnected")

        if char == b"\n":
            break

        data += char

    return json.loads(data.decode("utf-8"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tcp", methods=["POST"])
def tcp_message():
    message = request.form.get("message", "").strip()

    if not message:
        return jsonify({"status": "error", "message": "Please enter a message."}), 400

    payload = {
        "action": "message",
        "message": message
    }

    start = time.perf_counter()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(10)
            client.connect((SERVER_IP, TCP_PORT))
            client.sendall((json.dumps(payload) + "\n").encode())
            response = receive_line(client)

        elapsed = (time.perf_counter() - start) * 1000

        return jsonify({
            "status": response.get("status", "success"),
            "message": response.get("message", ""),
            "rtt": round(elapsed, 3)
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500


@app.route("/udp", methods=["POST"])
def udp_message():
    message = request.form.get("message", "").strip()

    if not message:
        return jsonify({"status": "error", "message": "Please enter a message."}), 400

    payload = {"message": message}

    start = time.perf_counter()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
            client.settimeout(5)
            client.sendto(
                json.dumps(payload).encode(),
                (SERVER_IP, UDP_PORT)
            )
            data, _ = client.recvfrom(4096)

        response = json.loads(data.decode())
        elapsed = (time.perf_counter() - start) * 1000

        return jsonify({
            "status": response.get("status", "success"),
            "message": response.get("message", ""),
            "rtt": round(elapsed, 3)
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"status": "error", "message": "No file selected."}), 400

    uploaded_file = request.files["file"]

    if not uploaded_file.filename:
        return jsonify({"status": "error", "message": "Please select a file."}), 400

    filename = os.path.basename(uploaded_file.filename)
    file_data = uploaded_file.read(MAX_FILE_SIZE + 1)

    if len(file_data) > MAX_FILE_SIZE:
        return jsonify({"status": "error", "message": "Maximum file size is 50 MB."}), 400

    payload = {
        "action": "file",
        "filename": filename,
        "filesize": len(file_data)
    }

    start = time.perf_counter()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(30)
            client.connect((SERVER_IP, TCP_PORT))

            client.sendall((json.dumps(payload) + "\n").encode())
            client.sendall(file_data)

            response = receive_line(client)

        elapsed = (time.perf_counter() - start) * 1000

        return jsonify({
            "status": response.get("status", "success"),
            "message": response.get("message", ""),
            "size": len(file_data),
            "transfer_time": round(elapsed, 3)
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
