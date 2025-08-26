import socket

def send_raw_request(host, port, request_file):
    # Read request from file
    with open(request_file, "rb") as f:  # rb to preserve exact bytes
        raw_request = f.read()

    # Connect to the server
    with socket.create_connection((host, port)) as sock:
        print(f"[*] Connected to {host}:{port}")
        
        # Send the raw request exactly as in request.txt
        sock.sendall(raw_request)
        print("[*] Sent request:")
        print(raw_request.decode(errors="replace"))

        # Receive the response
        response = sock.recv(8192)
        print("[*] Got response:")
        print(response.decode(errors="replace"))


if __name__ == "__main__":
    # Change host/port depending on your Burp request target
    send_raw_request("localhost", 9006, "request.txt")
