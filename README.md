# python-arp-network-scanner
A Python-based ARP network scanner using Scapy to discover active hosts and their MAC addresses on a local subnet.
# Local Network ARP Scanner in Python

An efficient local network discovery tool developed in Python using the **Scapy** library. It identifies active hosts on a local subnet by sending ARP requests and parsing the corresponding unicast responses.

## Why ARP Scan Instead of Ping (ICMP)?
* **Firewall Bypass:** Many modern operating systems block ICMP Echo Requests (Pings) by default. However, devices *must* respond to ARP requests to communicate on a local network.
* **Speed:** ARP scanning operates directly at Layer 2 (Data Link Layer), making it significantly faster than Layer 3 ping sweeps.

## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/python-arp-network-scanner.git](https://github.com/YOUR_USERNAME/python-arp-network-scanner.git)
   cd python-arp-network-scannerInstall dependencies:

Bash
pip install -r requirements.txt
Usage
Run the script with sudo (or Administrator) privileges, passing the target IP range as an argument:

Bash
sudo python3 network_scanner.py -t 192.168.1.1/24
Sample Output
Plaintext
[*] Tarama başlatılıyor: 192.168.1.1/24
[*] ARP paketleri hazırlanıyor...

==================================================
IP                      MAC 
==================================================
192.168.1.1             00:11:22:33:44:55
192.168.1.10            aa:bb:cc:dd:ee:ff
192.168.1.15            12:34:56:78:90:ab
==================================================
Toplam aktif cihaz sayısı: 3
Disclaimer
This tool is intended for educational purposes and authorized internal auditing only.
