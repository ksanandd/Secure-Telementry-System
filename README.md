# Secure-Telementry-System
Secure Telementry System using socket programming with SSL and multi-client support

# Secure Telemetry Collection System

## Description

This project implements a secure telemetry system using socket programming. Multiple clients send temperature data to a server, which processes and displays real-time statistics.

The system supports multi-client communication and ensures secure data transfer using SSL/TLS.

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

Clients → SSL/TCP → Multi-threaded Server → Processing → Dashboard

---

## Security

SSL/TLS encryption ensures secure communication between client and server.

---

## Conclusion

This project demonstrates secure and scalable telemetry data collection using socket programming.
