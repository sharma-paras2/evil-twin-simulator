from rich.console import Console
from rich.panel import Panel
import time

console = Console()

def simulate_evil_twin(target_ssid, target_channel, target_bssid):
    console.print(Panel(f"[bold red]Evil Twin Attack Simulator[/bold red]\n[dim]Educational use only[/dim]"))

    steps = [
        ("Scanning environment", f"Target found: {target_ssid} on CH{target_channel}"),
        ("Enabling monitor mode", "Interface wlan0 → wlan0mon"),
        ("Launching rogue AP", f"Broadcasting SSID: '{target_ssid}' (cloned)"),
        ("Starting deauth attack", f"Sending deauth packets to BSSID: {target_bssid}"),
        ("Victim disconnected", "Client forced off real AP"),
        ("Victim connected to rogue AP", "DHCP lease given: 192.168.1.100"),
        ("Captive portal served", "Victim sees fake login page"),
        ("Credentials captured", "Saved to captured_creds.txt"),
    ]

    for step, detail in steps:
        console.print(f"[bold green][+][/bold green] {step}")
        console.print(f"    [dim]{detail}[/dim]")
        time.sleep(1.2)

    console.print("\n[bold red][!] Attack simulation complete[/bold red]")
