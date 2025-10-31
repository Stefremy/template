#!/usr/bin/env python3
"""
Start a simple HTTP server serving the `nordicus` directory.
Try ports 8000 then 8001 and pick the first available.
"""
import os
import socket
import sys
from http.server import test as http_test, SimpleHTTPRequestHandler

def find_free_port(ports):
    for p in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind(("", p))
                return p
            except OSError:
                continue
    return None

def main():
    ports = [8000, 8001]
    port = find_free_port(ports)
    if port is None:
        print(f"No available ports in {ports}", file=sys.stderr)
        sys.exit(1)

    # Change to the nordicus directory relative to repo root (cwd when npm runs)
    target_dir = os.path.join(os.getcwd(), "nordicus")
    if not os.path.isdir(target_dir):
        print(f"Directory not found: {target_dir}", file=sys.stderr)
        sys.exit(1)

    os.chdir(target_dir)
    print(f"Serving '{target_dir}' on port {port} (http://localhost:{port})")
    # Use http.server.test with SimpleHTTPRequestHandler to run the server (blocks)
    # Explicitly pass the handler to avoid environments where a different default
    # handler might be used and not implement GET.
    http_test(SimpleHTTPRequestHandler, port=port)

if __name__ == "__main__":
    main()
