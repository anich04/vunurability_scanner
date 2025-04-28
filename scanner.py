import socket
import argparse

def scan_target(target, start_port, end_port):
    print(f"\n🔍 Scanning Target: {target}")
    print(f"🎯 Ports: {start_port} to {end_port}\n")
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            print(f"[+] Port {port:5d} is OPEN --> Banner: {banner}")
            sock.close()
        except:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Vulnerability Scanner")
    parser.add_argument("--target", required=True, help="Target IP address or domain")
    parser.add_argument("--start-port", type=int, default=20, help="Starting port number (default=20)")
    parser.add_argument("--end-port", type=int, default=1024, help="Ending port number (default=1024)")
    args = parser.parse_args()

    scan_target(args.target, args.start_port, args.end_port)
