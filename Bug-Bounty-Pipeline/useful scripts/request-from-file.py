import socket
import ssl

def send_raw_request(host, port, request_file, times=1):
    # Read request from file
    with open(request_file, "rb") as f:  # rb = preserve exact bytes
        raw_request = f.read()

    # Create TCP connection
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"[*] Connected securely to {host}:{port}")

            for i in range(times):
                print(f"\n[*] Sending request #{i+1}...")
                ssock.sendall(raw_request)

                # Receive response (loop until no more data or connection closed)
                response = b""
                while True:
                    chunk = ssock.recv(8192)
                    if not chunk:
                        break
                    response += chunk
                    if len(chunk) < 8192:  # heuristic stop
                        break

                print(f"[*] Got response #{i+1}:")
                try:
                    print(response.decode(errors="replace"))
                except:
                    print(response)

if __name__ == "__main__":
    # ✅ Port 443 is usually correct for HTTPS unless explicitly different
    send_raw_request("c3-ux.dv.exaba.io", 443, "request.txt", times=50)
