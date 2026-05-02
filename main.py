from rich.console import Console
from rich.panel import Panel
import os

console = Console()

def main():
    console.print(Panel("[bold red]Evil Twin Attack Simulator[/bold red]\n[dim]For educational purposes only[/dim]", width=50))
    console.print("\n[bold]Choose mode:[/bold]")
    console.print("  [cyan]1[/cyan] → Scan local network")
    console.print("  [cyan]2[/cyan] → Simulate Evil Twin attack")
    console.print("  [cyan]3[/cyan] → Start captive portal")
    console.print("  [cyan]4[/cyan] → View captured credentials")
    console.print("  [cyan]5[/cyan] → Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        from scanner import scan_network
        scan_network()
    elif choice == "2":
        ssid = input("Enter target SSID: ")
        channel = input("Enter channel (default 6): ") or "6"
        bssid = input("Enter BSSID (or press Enter for default): ") or "AA:BB:CC:DD:EE:FF"
        from simulator import simulate_evil_twin
        simulate_evil_twin(ssid, channel, bssid)
    elif choice == "3":
        console.print("[green]Starting captive portal on http://localhost:8080[/green]")
        os.system("python3 server.py")
    elif choice == "4":
        try:
            with open("captured_creds.txt") as f:
                content = f.read()
                console.print(content if content else "[dim]No credentials captured yet.[/dim]")
        except FileNotFoundError:
            console.print("[dim]No credentials captured yet.[/dim]")
    elif choice == "5":
        exit()
    else:
        console.print("[red]Invalid choice[/red]")

main()
