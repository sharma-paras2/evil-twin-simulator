# Evil Twin Attack Simulator

An educational cybersecurity project that simulates an Evil Twin Wi-Fi attack built in Python on Kali Linux.

## About
This project demonstrates how Evil Twin attacks work — where an attacker creates a rogue access point cloning a legitimate network to trick victims into connecting and capturing their credentials through a fake login portal.

Built as a learning project to understand wireless network security concepts.

## Features
- Network scanner using Scapy
- Evil Twin attack flow simulation
- Fake captive portal using Flask
- Credential logger
- Terminal dashboard using Rich

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask rich scapy
python3 main.py
```

## Project Structure