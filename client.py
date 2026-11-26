
import socket
import json
import time
import os

SERVER_IP = "192.168.50.4"

TCP_PORT = 5000
UDP_PORT = 5001

BUFFER_SIZE = 4096


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


# TCP MESSAGE
def tcp_message():

    message = input("Enter message: ")

    request = {
        "action": "message",
        "message": message
    }

    start = time.perf_counter()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        client.settimeout(10)

        client.connect((SERVER_IP, TCP_PORT))

        client.sendall(
            (json.dumps(request) + "\n").encode()
        )

        response = receive_line(client)

    end = time.perf_counter()

    print("\nTCP Response:", response["message"])
    print(f"Round Trip Time: {(end-start)*1000:.3f} ms")


# UDP MESSAGE
def udp_message():

    message = input("Enter message: ")

    request = {
        "message": message
    }

    start = time.perf_counter()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:

        client.settimeout(5)

        client.sendto(
            json.dumps(request).encode(),
            (SERVER_IP, UDP_PORT)
        )

        data, address = client.recvfrom(4096)

    end = time.perf_counter()

    response = json.loads(data.decode())

    print("\nUDP Response:", response["message"])
    print(f"Round Trip Time: {(end-start)*1000:.3f} ms")


# TCP FILE TRANSFER
def send_file():

    filepath = input("Enter file path: ").strip()

    if not os.path.isfile(filepath):
        print("Error: File not found!")
        return

    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    if filesize > 50 * 1024 * 1024:
        print("Error: Maximum file size is 50 MB.")
        return

    request = {
        "action": "file",
        "filename": filename,
        "filesize": filesize
    }

    start = time.perf_counter()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        client.settimeout(30)

        client.connect((SERVER_IP, TCP_PORT))

        client.sendall(
            (json.dumps(request) + "\n").encode()
        )

        with open(filepath, "rb") as file:

            while True:
                chunk = file.read(BUFFER_SIZE)

                if not chunk:
                    break

                client.sendall(chunk)

        response = receive_line(client)

    end = time.perf_counter()

    print("\nServer Response:", response["message"])
    print(f"File Size: {filesize} bytes")
    print(f"Transfer Time: {(end-start)*1000:.3f} ms")


# MAIN MENU
def main():

    while True:

        print("\n================================")
        print(" CLOUD NETWORK PROTOCOL CLIENT")
        print("================================")
        print("1. Send Message using TCP")
        print("2. Send Message using UDP")
        print("3. Transfer File using TCP")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":
                tcp_message()

            elif choice == "2":
                udp_message()

            elif choice == "3":
                send_file()

            elif choice == "4":
                print("Client application closed.")
                break

            else:
                print("Invalid choice. Try again.")

        except socket.timeout:
            print("Error: Server response timed out.")

        except ConnectionRefusedError:
            print("Error: Server is not running or port is blocked.")

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
