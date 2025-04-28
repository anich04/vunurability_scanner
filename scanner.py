import socket

def scan_target(target, ports):
    print(f"\n🔍 Scanning Target: {target}\n")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            print(f"[+] Port {port} is OPEN --> Banner: {banner}")
            sock.close()
        except:
            print(f"[-] Port {port} is closed")

if __name__ == "__main__":
    print("=== Simple Vulnerability Scanner ===\n")
    target = input("Enter the target IP address or domain: ").strip()
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389]
    scan_target(target, ports)
