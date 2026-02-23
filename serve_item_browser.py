# -*- coding: utf-8 -*-
"""Simple HTTP server for item_browser.html, serves ItemInfo.txt with proper encoding."""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=DIR, **k)

    def do_GET(self):
        if self.path in ("/", ""):
            self.path = "/item_browser.html"
        if self.path.split("?")[0] == "/ItemInfo.txt":
            path = os.path.join(DIR, "ItemInfo.txt")
            try:
                for enc in ("gbk", "gb18030", "gb2312", "utf-8"):
                    try:
                        with open(path, "r", encoding=enc) as f:
                            content = f.read()
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    self.send_error(500, "Cannot decode ItemInfo.txt")
                    return
            except FileNotFoundError:
                self.send_error(404, "ItemInfo.txt not found")
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
            return
        return super().do_GET()


def main():
    port = 8765
    print(f"Item Browser server: http://localhost:{port}/item_browser.html")
    print("Press Ctrl+C to stop")
    HTTPServer(("", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
