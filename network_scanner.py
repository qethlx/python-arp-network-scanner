#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import sys

def get_arguments():
    """Kullanıcıdan taranacak IP aralığını parametre olarak alır."""
    parser = argparse.ArgumentParser(description="Python ARP Network Scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, 
                        help="Taranacak hedef IP adresi veya IP aralığı (Örn: 192.168.1.1/24)")
    options = parser.parse_args()
    return options

def scan(ip):
    """Belirtilen IP aralığına ARP istekleri gönderir ve yanıtları toplar."""
    arp_request = scapy.ARP(pdst=ip)

    ether_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_packet = ether_broadcast/arp_request

    answered_list = scapy.srp(arp_request_packet, timeout=2, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        
    return clients_list

def print_result(results_list):
    """Tarama sonuçlarını şık bir tablo formatında ekrana yazdırır."""
    if not results_list:
        print("\n[!] Ağda aktif hiçbir cihaz bulunamadı veya yetki hatası oluştu.")
        return
        
    print("\n" + "=" * 50)
    print("IP Adresi\t\tMAC Adresi")
    print("=" * 50)
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")
    print("=" * 50)
    print(f"Toplam aktif cihaz sayısı: {len(results_list)}\n")

def main():
    options = get_arguments()
    
    print(f"\n[*] Tarama başlatılıyor: {options.target}")
    print("[*] ARP paketleri hazırlanıyor...")
    
    try:
        scan_result = scan(options.target)
        print_result(scan_result)
    except PermissionError:
        print("\n[!] HATA: Ağ paketleri göndermek için yönetici (root/administrator) yetkilerine sahip olmalısınız.")
        print("[*] Lütfen Linux'ta 'sudo python3 network_scanner.py ...' şeklinde çalıştırın.")
        sys.exit()
    except KeyboardInterrupt:
        print("\n[!] Tarama kullanıcı tarafından sonlandırıldı.")
        sys.exit()

if __name__ == "__main__":
    main()
