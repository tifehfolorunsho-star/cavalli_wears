"""
Simple HTTP Server to run and preview the SwiftShop product ordering website.
Run this script using:
    python3 server.py
Then open http://localhost:8000 in your web browser.
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 65)
        print(" 👑 Cavalli Wears Website Server is Running!")
        print(f" 🛍️  Customer Storefront : {url}/index.html")
        print(f" 🔍  Search Page          : {url}/search.html")
        print(f" 🔐  Owner Admin Portal   : {url}/admin.html")
        print("     Default Owner Password: cavalli123")
        print(" Press Ctrl+C to stop the server.")
        print("=" * 65)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    run()

