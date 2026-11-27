# Cloud-Based Network Protocol Implementation and Testing System

A Python-based network communication and testing platform that implements TCP and UDP protocols, supports TCP file transfer, measures communication performance, and provides a browser-based interface deployed on AWS EC2.

**Live Application:** http://16.178.83.139:8000

**GitHub Repository:** https://github.com/vatsa2005rishika/Cloud-Based-Network-Protocol-System

---

## 1. Project Overview

The Cloud-Based Network Protocol Implementation and Testing System is designed to demonstrate and evaluate network communication using two major transport-layer protocols: Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).

The project uses Python socket programming to implement client-server communication. A Flask-based web application provides a simple browser interface through which users can send messages, test protocol responses, and transfer files.

The application is deployed on an Amazon Web Services (AWS) EC2 instance, making the web interface accessible through a public IP address.

## 2. Objectives

- Implement TCP-based client-server communication.
- Implement UDP-based message communication.
- Enable file transfer using TCP.
- Measure Round Trip Time (RTT) for message communication.
- Measure file size and file-transfer duration.
- Develop a browser-based interface using Flask.
- Deploy the application and socket services on AWS EC2.
- Understand the practical differences between TCP and UDP.

## 3. Features

### TCP Communication
- Establishes a connection between client and server.
- Supports text message exchange.
- Displays the server response.
- Measures Round Trip Time (RTT).

### UDP Communication
- Supports connectionless message exchange.
- Receives and responds to UDP datagrams.
- Measures Round Trip Time (RTT).

### TCP File Transfer
- Supports uploading files through the web interface.
- Transfers file data using TCP.
- Saves received files on the server.
- Reports file size and transfer duration.

### Web Interface
- Browser-based interface built using Flask.
- Separate sections for TCP testing, UDP testing and file transfer.
- Displays communication responses and performance measurements.

### Cloud Deployment
- Hosted on AWS EC2.
- Uses Ubuntu Server.
- Uses Gunicorn to serve the Flask application.
- Uses systemd to manage application services.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Socket Programming | TCP and UDP communication |
| TCP | Reliable messaging and file transfer |
| UDP | Connectionless message communication |
| Flask | Web application backend |
| HTML | Web page structure |
| CSS | Interface styling |
| JavaScript | Browser-side interactions |
| Gunicorn | WSGI application server |
| AWS EC2 | Cloud hosting |
| Ubuntu | Server operating system |
| systemd | Service management |
| Git and GitHub | Version control and source-code hosting |

## 5. System Architecture

The system consists of a browser interface, a Flask application and two Python socket services.

```text
              User Browser
                   |
                   |
             HTTP - Port 8000
                   |
                   v
             Gunicorn Server
                   |
                   v
               Flask App
                   |
            ----------------
            |              |
            v              v
        TCP Service    UDP Service
        Port 5000      Port 5001
            |              |
            v              v
      TCP Messaging    UDP Messaging
      TCP File Transfer
                   |
                   v
                AWS EC2
              Ubuntu Server
```

The Flask application communicates with the socket services running on the same EC2 instance through the local loopback address.

## 6. Network Port Configuration

| Port | Protocol | Purpose |
|---|---|---|
| 8000 | HTTP | Flask web application served by Gunicorn |
| 5000 | TCP | TCP messaging and file transfer |
| 5001 | UDP | UDP messaging |

## 7. Project Structure

```text
Cloud-Based-Network-Protocol-System/
│
├── server.py
├── client.py
├── app.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── README.md
└── .gitignore
```

**File descriptions:**

- `server.py` – Implements the TCP and UDP socket services.
- `client.py` – Provides the client-side interface for network testing.
- `app.py` – Implements the Flask web application and connects browser requests to the socket services.
- `templates/index.html` – Contains the web interface.
- `requirements.txt` – Lists the Python dependencies.
- `.gitignore` – Excludes virtual environments, generated files and sensitive credentials from Git tracking.

## 8. Installation and Local Execution

### Prerequisites

- Python installed.
- Git installed.
- A terminal or command prompt.
- Required Python packages.

### Step 1: Clone the repository

```bash
git clone https://github.com/vatsa2005rishika/Cloud-Based-Network-Protocol-System.git
```

```bash
cd Cloud-Based-Network-Protocol-System
```

### Step 2: Create a virtual environment

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

**Ubuntu/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Start the socket server

Open a terminal in the project directory and run:

```bash
python server.py
```

On Ubuntu/Linux, use:

```bash
python3 server.py
```

Keep this terminal running.

### Step 5: Start the Flask application

Open a second terminal in the project directory.

**Windows PowerShell:**

```powershell
$env:SERVER_IP="127.0.0.1"
$env:PORT="8000"
python app.py
```

**Ubuntu/Linux:**

```bash
export SERVER_IP=127.0.0.1
export PORT=8000
python3 app.py
```

### Step 6: Open the application

Visit:

```text
http://127.0.0.1:8000
```

The browser interface can now be used to test TCP messaging, UDP messaging and TCP file transfer.

**Note:** Run the socket server and Flask application in separate terminals. The local configuration uses port 8000 for the web application to avoid conflicting with the TCP service on port 5000.

## 9. AWS EC2 Deployment

The application was deployed on an AWS EC2 instance with Ubuntu Server 24.04 LTS.

### Deployment configuration

| Component | Configuration |
|---|---|
| Cloud platform | Amazon Web Services |
| Service | EC2 |
| Instance type | t3.micro |
| Operating system | Ubuntu Server 24.04 LTS |
| Web application port | 8000 |
| TCP service port | 5000 |
| UDP service port | 5001 |
| Web server | Gunicorn |
| Service management | systemd |

### Deployment steps

1. Launch an Ubuntu EC2 instance.
2. Configure the required inbound security group rules.
3. Connect to the instance using SSH or EC2 Instance Connect.
4. Clone the GitHub repository.
5. Create and activate a Python virtual environment.
6. Install the required dependencies.
7. Configure the socket server and Flask application.
8. Configure Gunicorn to serve the Flask application.
9. Configure systemd services for automatic startup and restart.
10. Verify that the services are running and the website is accessible.

### Clone the project on EC2

```bash
git clone https://github.com/vatsa2005rishika/Cloud-Based-Network-Protocol-System.git
```

```bash
cd Cloud-Based-Network-Protocol-System
```

### Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Start the application services

The deployed environment uses two systemd services:

- `network-server.service` – Runs the Python TCP/UDP server.
- `network-web.service` – Runs the Flask application through Gunicorn.

Check their status:

```bash
sudo systemctl status network-server.service --no-pager
```

```bash
sudo systemctl status network-web.service --no-pager
```

Check the listening ports:

```bash
sudo ss -tulnp | grep -E ':5000|:5001|:8000'
```

The deployed Flask application uses:

```text
SERVER_IP=127.0.0.1
```

This allows the Flask application to communicate with the socket services on the same EC2 machine.

## 10. Testing and Results

The system was tested through local virtual machines and the deployed web application.

### Functional tests

| Test | Expected behaviour |
|---|---|
| TCP message testing | Server receives the message and returns a response |
| UDP message testing | Server receives the datagram and returns a response |
| TCP file transfer | File is received and saved on the server |
| RTT measurement | Communication response time is measured |
| File-transfer measurement | File size and transfer duration are reported |
| Web interface | Browser displays the testing interface |
| AWS deployment | Application is accessible through the public URL |

### Recorded local testing results

| Test | Recorded result |
|---|---|
| Client-server connectivity | 4 packets received out of 4 |
| TCP message | Successful response to "Hello server" |
| TCP message RTT | 13.567 ms |
| TCP file transfer | `sample.txt` received successfully |
| File size | 48 bytes |
| File-transfer time | 18.546 ms |

### Website response-time optimization

During deployment, the website initially showed a very high response time.

The Gunicorn configuration was subsequently changed to use a gthread worker with four threads.

Recorded measurements:

| Metric | Before optimization | After optimization |
|---|---:|---:|
| First byte | Approximately 87.08 s | 0.773943 s |
| Total loading time | Approximately 87.08 s | 0.774157 s |

The recorded total response time decreased substantially after the configuration change.

These are website response-time measurements, not TCP/UDP throughput measurements.

## 11. Limitations

- The application currently runs on a single EC2 instance.
- HTTPS is not configured.
- User authentication is not implemented.
- Large-scale concurrent-client testing has not been established.
- Performance measurements may vary with network conditions.
- Persistent message-history functionality is not implemented as a documented feature.

## 12. Future Enhancements

- Implement HTTPS using a domain name and SSL/TLS certificate.
- Add user authentication and access control.
- Improve logging and monitoring.
- Add more detailed network performance analytics.
- Perform scalability and concurrent-client testing.
- Conduct repeated performance tests under controlled conditions.
- Improve the interface and reporting features.

## 13. References

- Python Socket Documentation: https://docs.python.org/3/library/socket.html
- Flask Documentation: https://flask.palletsprojects.com/
- Gunicorn Documentation: https://docs.gunicorn.org/
- AWS EC2 Documentation: https://docs.aws.amazon.com/ec2/
- Ubuntu Documentation: https://ubuntu.com/server/docs
- Git Documentation: https://git-scm.com/doc

---

## 14. Project Links

**GitHub Repository:**  
https://github.com/vatsa2005rishika/Cloud-Based-Network-Protocol-System

**Deployed Web Application:**  
http://16.178.83.139:8000

---

**Project:** Cloud-Based Network Protocol Implementation and Testing System

**Department:** Computer Science and Engineering

**Academic Year:** 2026–27