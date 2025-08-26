import socket
import random
import string
import re

def random_string(length=100, start_with_letter=False):
    chars = string.ascii_letters + string.digits
    if start_with_letter:
        return random.choice(string.ascii_letters) + ''.join(random.choice(chars) for _ in range(length - 1))
    else:
        return ''.join(random.choice(chars) for _ in range(length))

def send_raw_request(host, port, request_file):
    with open(request_file, "rb") as f:
        raw_request_template = f.read()

    # Try splitting headers/body with both Windows and Linux line endings
    if b"\r\n\r\n" in raw_request_template:
        header_bytes, body_bytes = raw_request_template.split(b"\r\n\r\n", 1)
        sep = b"\r\n\r\n"
    elif b"\n\n" in raw_request_template:
        header_bytes, body_bytes = raw_request_template.split(b"\n\n", 1)
        sep = b"\n\n"
    else:
        print("[-] Could not find header/body separator (\\r\\n\\r\\n or \\n\\n)")
        return

    header_str = header_bytes.decode(errors="replace")

    for i in range(2):
        # Generate random values
        name_val = random_string(100000, start_with_letter=True)
        url_val = "http://" + random_string(100000)

        # Replace "name" and "url" in body
        body_str = body_bytes.decode(errors="replace")
        body_str = re.sub(r'"name"\s*:\s*".*?"', f'"name":"{name_val}"', body_str)
        body_str = re.sub(r'"url"\s*:\s*".*?"', f'"url":"{url_val}"', body_str)

        new_body_bytes = body_str.encode()

        # Fix Content-Length in headers
        new_header_str = re.sub(
            r"Content-Length:\s*\d+",
            f"Content-Length: {len(new_body_bytes)}",
            header_str
        )

        # Rebuild request with the same separator used in file
        modified_request = (new_header_str.encode() + sep + new_body_bytes)

        # Connect and send
        with socket.create_connection((host, port)) as sock:
            print(f"\n[*] Request {i+1} -> Connected to {host}:{port}")
            sock.sendall(modified_request)
            print(f"[*] Sent request {i+1} with name={name_val[:12]}..., url={url_val[:30]}...")

            response = sock.recv(8192)
            print(f"[*] Got response {i+1}:")
            print(response.decode(errors="replace"))

if __name__ == "__main__":
    send_raw_request("localhost", 9006, "request.txt")