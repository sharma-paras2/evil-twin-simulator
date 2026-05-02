🔐 Evil Twin Attack Simulator

A mini cybersecurity project that simulates an Evil Twin Wi-Fi attack for educational purposes.

Features
Network scanning (Scapy)
Simulates rogue access point attack flow
Fake captive portal (login page)
Credential logging with timestamps
Clean terminal output (Rich)

How it works
Scans local network devices
Clones a target SSID
Simulates victim connection
Serves a fake login page
Captures entered credentials

How to run
Install dependencies: pip install flask scapy rich

Run main program: python main.py

Open captive portal (if hosted): http://127.0.0.1:8080