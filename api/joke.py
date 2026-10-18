from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import urllib.error


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        joke = None
        try:
            req = urllib.request.Request(
                "https://icanhazdadjoke.com/",
                headers={
                    "Accept": "application/json",
                    "User-Agent": "WLZBI Dad Joke API (vercel)"
                },
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                joke = data.get("joke")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        payload = {
            "joke": joke,
            "credit": {
                "by": "WLZBI",
                "author": "@rejerks",
                "display": "@rejerks | WLZBI"
            }
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))
