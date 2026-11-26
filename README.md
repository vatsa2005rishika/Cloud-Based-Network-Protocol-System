# Cloud-Based Network Protocol Implementation and Testing System

## 1. Project Overview

This project demonstrates network communication using TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) through Python socket programming.

It implements client-server communication between Ubuntu Virtual Machines configured using Oracle VirtualBox. The application supports message exchange using TCP and UDP, along with file transfer using TCP.

The project also measures Round Trip Time (RTT) to compare the communication behaviour of both protocols. The server is deployed on AWS EC2 to demonstrate cloud-based remote communication.

## 2. Objectives

- Implement TCP client-server communication.
- Implement UDP client-server communication.
- Transfer files using TCP.
- Measure and compare TCP and UDP response times.
- Understand reliable and connectionless communication.
- Deploy the server on AWS EC2.
- Demonstrate cloud-based networking.

## 3. Technologies Used

- Python 3
- Socket Programming
- TCP and UDP
- Ubuntu Linux
- Oracle VirtualBox
- AWS EC2
- Git and GitHub
- Visual Studio Code

## 4. Project Architecture

### Local Network Configuration

| Component | Configuration |
|---|---|
| Server VM | Ubuntu |
| Server IP | 192.168.50.4 |
| Client VM | Ubuntu |
| Client IP | 192.168.50.3 |
| TCP Port | 5000 |
| UDP Port | 5001 |

### Cloud Architecture

The server application is hosted on an AWS EC2 Ubuntu instance. A remote client connects to the EC2 public IP address to exchange messages and transfer files.

| Component | Configuration |
|---|---|
| Cloud Provider | AWS |
| Service | Amazon EC2 |
| Operating System | Ubuntu Server 24.04 LTS |
| Instance Type | t3.micro |
| Server Application | Python Socket Server |
| TCP Port | 5000 |
| UDP Port | 5001 |

The EC2 server listens on `0.0.0.0` to accept remote client connections through the configured network ports.

## 5. Features

### TCP Communication
Provides reliable, connection-oriented message exchange between the client and server.

### UDP Communication
Demonstrates connectionless message exchange using UDP datagrams.

### File Transfer
Transfers files from the client to the server using TCP.

### Response Time Measurement
Measures Round Trip Time (RTT) for TCP and UDP communication.

### Cloud Deployment
Deploys the server application on AWS EC2 for remote communication.

## 6. Project Structure

```text
Cloud-Based-Network-Protocol-System/
├── client.py
├── server.py
├── README.md
├── requirements.txt
├── .gitignore
└── received_files/
```

## 7. Execution Instructions

### Start the Server

```bash
python3 server.py
```

### Start the Client

```bash
python3 client.py
```

### Client Menu

1. Send Message using TCP
2. Send Message using UDP
3. Transfer File using TCP
4. Exit

### AWS EC2 Deployment

1. Launch an Ubuntu EC2 instance.
2. Clone the GitHub repository onto the EC2 instance.
3. Configure the required inbound security group rules:
   - TCP port 5000
   - UDP port 5001
   - SSH port 22 for remote administration
4. Start the Python server on the EC2 instance.
5. Configure the client to connect to the EC2 public IP address.
6. Run the client and test TCP messaging, UDP messaging and TCP file transfer.

## 8. TCP vs UDP Comparison

| Parameter | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Best effort |
| Delivery | Acknowledged | Not guaranteed |
| Ordering | Maintained | Not guaranteed |
| Overhead | Higher | Lower |
| File transfer | Implemented | Not implemented |

## 9. Testing and Results

The application was tested using a remote Ubuntu client and an AWS EC2 Ubuntu server.

### Test 1: TCP Message Transmission

- Feature: TCP messaging
- Result: Successful
- Server response: `Message received successfully by TCP server`
- Measured RTT: 849.317 ms

### Test 2: UDP Message Transmission

- Feature: UDP messaging
- Result: Successful
- Server response: `Message received successfully by UDP server`
- Measured RTT: 594.117 ms

### Test 3: TCP File Transfer

- Feature: TCP file transfer
- File name: `sample.txt`
- File size: 48 bytes
- Server response: `File sample.txt received successfully`
- Transfer time: 900.530 ms
- Result: Successful

The received file was verified on the AWS EC2 instance inside the `received_files/` directory.

### Test Summary

| Test Case | Result |
|---|---|
| TCP message transmission | Passed |
| UDP message transmission | Passed |
| TCP file transfer | Passed |
| File receipt on AWS EC2 | Verified |

**Note:** The measured response and transfer times are observations from individual test runs and may vary with network conditions.

## 10. Future Scope

- Implement reliable UDP file transfer.
- Develop a graphical user interface.
- Add detailed network performance analysis.
- Support multiple simultaneous clients.
- Implement authentication and encrypted communication.

## 11. Conclusion

The project demonstrates the practical implementation of TCP and UDP protocols using Python socket programming. It provides an understanding of reliable and connectionless communication, file transfer, performance measurement and cloud networking through AWS EC2 deployment.

The successful remote testing of TCP messaging, UDP messaging and TCP file transfer validates the functionality of the application in a cloud environment.

## 12. GitHub Repository

Source code and project documentation:

https://github.com/vatsa2005rishika/Cloud-Based-Network-Protocol-System
