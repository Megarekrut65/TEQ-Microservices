# TEQ-Microservices
Microservices for TEQ project

This project provides a microservices architecture for executing and testing code in Python, C++, and Java. It also includes services for analyzing similarity between scripts and natural language descriptions. All services are containerized using Docker, communicate via a shared internal network, and are accessed through a unified gateway.

## Microservices Overview

- **Gateway** – Central access point for all services (`localhost:8800`)
- **PL Similarity** – Script similarity analysis for program languages (`localhost:8801`)
- **NL Similarity** – Script similarity analysis for natural languages (`localhost:8802`)
- **Python Runner** – Executes Python code (`localhost:8803`)
- **C++ Runner** – Executes C++ code (`localhost:8804`)
- **Java Runner** – Executes Java code (`localhost:8805`)
- **Python Tester** – Runs Python unit tests - unittest lib (`localhost:8806`)
- **C++ Tester** – Runs C++ unit tests - gtest lib (`localhost:8807`)
- **Java Tester** – Runs Java unit tests - JUnit lib (`localhost:8808`)



## Setup
1. Configure `.env` files for gateway and microservices
2. **Pull external images**:
   ```bash
   docker pull python:3.12-slim
   docker pull megarekrut65/java-junit
   docker pull kost13/cpp-gtest

3. **Build & start services**:
   ```bash
   docker-compose up --build
