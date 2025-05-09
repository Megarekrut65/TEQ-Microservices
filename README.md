# TEQ-Microservices
Microservices for TEQ project

This project provides a microservices architecture for executing and testing code in Python, C++, and Java. It also includes services for analyzing similarity between scripts and natural language descriptions. All services are containerized using Docker, communicate via a shared internal network, and are accessed through a unified gateway.

## Microservices Overview

- **Python Runner** – Executes Python code (`localhost:8006`)
- **C++ Runner** – Executes C++ code (`localhost:8007`)
- **Java Runner** – Executes Java code (`localhost:8008`)
- **Python Tester** – Runs Python unit tests - unittest lib (`localhost:8016`)
- **C++ Tester** – Runs C++ unit tests - gtest lib (`localhost:8017`)
- **Java Tester** – Runs Java unit tests - JUpiter lib (`localhost:8018`)
- **PL Similarity** – Script similarity analysis for program languages (`localhost:8004`)
- **NL Similarity** – Script similarity analysis for natural languages (`localhost:8005`)
- **Gateway** – Central access point for all services (`localhost:8080`)

## Setup

1. **Build & start services**:
   ```bash
   docker-compose up --build
