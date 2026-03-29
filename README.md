# Secure Telemetry Collection System
Secure Telemetry System using socket programming with SSL and multi-client support

## Description

This project implements a secure telemetry data collection system using low-level socket programming. Multiple clients send temperature data to a centralized server, which processes and displays real-time statistics such as minimum, maximum, average, and count.

The system supports concurrent multi-client communication and ensures secure data transmission using SSL/TLS encryption.

---

## Technologies Used

* Python
* Socket Programming (TCP)
* SSL/TLS
* Multithreading

---

## Features

* Multi-client support
* Secure communication using SSL
* Real-time temperature dashboard
* Data processing (min, max, avg, count)
* Thread-based concurrent client handling

---

## How to Run

### 1. Generate Certificate

```
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
```

### 2. Run Server

```
python server_ssl.py
```

### 3. Run Clients

```
python client_ssl.py
```

---

## Architecture

Multiple Clients → SSL/TCP Layer → Multi-threaded Server → Data Processing → Real-time Dashboard2

---

## Security

SSL/TLS encryption ensures secure communication between client and server.

---

## Conclusion

The system effectively demonstrates real-world concepts of secure communication, concurrency, and network programming.

## Future Scope

* Integration with web-based dashboards
* Database storage for historical analysis
* Implementation of DTLS for secure UDP communication

## Input with multiple clients

<img width="723" height="382" alt="Input1" src="https://github.com/user-attachments/assets/1e9844aa-afc5-4e14-9c07-a7202ff6cdb2" />
<img width="772" height="377" alt="Input 2" src="https://github.com/user-attachments/assets/336f5ff6-b301-4b0d-9ba9-4f4875738e57" />
<img width="762" height="383" alt="Input 3" src="https://github.com/user-attachments/assets/08af373a-7702-4bb1-8559-2ccb453485cf" />

## Output of these inputs

<img width="658" height="247" alt="output" src="https://github.com/user-attachments/assets/5fd954f0-d86f-42fc-9e61-d247fd35c834" />

