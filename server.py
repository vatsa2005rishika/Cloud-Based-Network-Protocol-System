
import socket
import threading
import json
import os
import time

SERVER_IP = "0.0.0.0"
TCP_PORT = 5000
UDP_PORT = 5001

BUFFER_SIZE = 4096
SAVE_DIR = "received_files"

os.makedirs(SAVE_DIR, exist_ok=True)


def receive_line(conn):
    data = b""

    while True:
        char = conn.recv(1)

        if not char:
            raise ConnectionError("Client disconnected")

        if char == b"\n":
            break

        data += char

    return data.decode("utf-8")


# TCP SERVER
def handle_tcp_client(conn, address):
    print(f"\n[TCP] Client connected: {address}")

    try:
        request = json.loads(receive_line(conn))

        if request["action"] == "message":
            message = request["message"]

            print(f"[TCP] Received message: {message}")

            response = {
                "status": "success",
                "message": "Message received successfully by TCP server"
            }

            conn.sendall((json.dumps(response) + "\n").encode())

        elif request["action"] == "file":
            filename = os.path.basename(request["filename"])
            filesize = int(request["filesize"])

            if filesize < 0 or filesize > 50 * 1024 * 1024:
                raise ValueError("File size exceeds the 50 MB limit")

            filepath = os.path.join(SAVE_DIR, filename)

            remaining = filesize

            with open(filepath, "wb") as file:
                while remaining > 0:
                    chunk = conn.recv(min(BUFFER_SIZE, remaining))

                    if not chunk:
                        raise ConnectionError("File transfer interrupted")

                    file.write(chunk)
                    remaining -= len(chunk)

            print(f"[TCP] File received: {filename}")

            response = {
                "status": "success",
                "message": f"File {filename} received successfully",
                "size": filesize
            }

            conn.sendall((json.dumps(response) + "\n").encode())

    except Exception as error:
        print(f"[TCP ERROR] {error}")

        try:
            response = {
                "status": "error",
                "message": str(error)
            }
            conn.sendall((json.dumps(response) + "\n").encode())
        except OSError:
            pass

    finally:
        conn.close()


def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((SERVER_IP, TCP_PORT))
    server.listen(5)

    print(f"[TCP] Server listening on port {TCP_PORT}")

    while True:
        conn, address = server.accept()

        thread = threading.Thread(
            target=handle_tcp_client,
            args=(conn, address)
        )

        thread.start()


# UDP SERVER
def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((SERVER_IP, UDP_PORT))

    print(f"[UDP] Server listening on port {UDP_PORT}")

    while True:
        data, address = server.recvfrom(4096)

        try:
            request = json.loads(data.decode())

            message = request["message"]

            print(f"[UDP] Received from {address}: {message}")

            response = {
                "status": "success",
                "message": "Message received successfully by UDP server"
            }

            server.sendto(
                json.dumps(response).encode(),
                address
            )

        except Exception as error:
            print(f"[UDP ERROR] {error}")


if __name__ == "__main__":

    print("===================================")
    print(" CLOUD NETWORK PROTOCOL SERVER")
    print("===================================")

    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=udp_server, daemon=True).start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nServer stopped.")
