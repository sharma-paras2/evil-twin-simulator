from scapy.all import ARP, Ether, srp
from rich.console import Console
from rich.table import Table

console = Console()

def scan_network(target_ip="192.168.1.1/24"):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    console.print("[bold cyan]Scanning network...[/bold cyan]")
    result = srp(packet, timeout=3, verbose=0)[0]

    table = Table(title="Discovered Devices")
    table.add_column("IP Address", style="cyan")
    table.add_column("MAC Address", style="magenta")

    for sent, received in result:
        table.add_row(received.psrc, received.hwsrc)

    console.print(table)
