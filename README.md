# Cloud-Based Network Protocol Implementation and Testing System

## 1. Project Overview

This project demonstrates network communication using TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) through Python socket programming.

It implements client-server communication between two Ubuntu Virtual Machines configured using Oracle VirtualBox. The application supports message exchange using TCP and UDP, along with file transfer using TCP.

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
Cloud_computing_project/
├── client.py
├── server.py
├── README.md
├── requirements.txt
├── .gitignore
├── screenshots/
└── sample_files/
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

## 8. TCP vs UDP Comparison

| Parameter | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Best effort |
| Delivery | Acknowledged | Not guaranteed |
| Ordering | Maintained | Not guaranteed |
| Overhead | Higher | Lower |
| File transfer | Implemented | Not implemented |

## 9. Testing

The following experiments are performed:

- TCP message transmission.
- UDP message transmission.
- TCP file transfer.
- Response time measurement.
- Local communication between Ubuntu VMs.
- Remote communication using AWS EC2.

## 10. Future Scope

- Implement reliable UDP file transfer.
- Develop a graphical user interface.
- Add detailed network performance analysis.
- Support multiple simultaneous clients.
- Implement authentication and encrypted communication.

## 11. Conclusion

The project demonstrates the practical implementation of TCP and UDP protocols using Python socket programming. It provides an understanding of reliable and connectionless communication, file transfer, performance measurement and cloud networking through AWS EC2 deployment.
