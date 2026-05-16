#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import argparse
import pathlib

parser = argparse.ArgumentParser(description='Run 3D baseball game locally')
parser.add_argument('--port', type=int, default=8000)
parser.add_argument('--no-open', action='store_true', help='Do not auto-open browser')
args = parser.parse_args()

root = pathlib.Path(__file__).resolve().parent
url = f'http://127.0.0.1:{args.port}/index.html'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(root), **kw)

with socketserver.TCPServer(("", args.port), Handler) as httpd:
    print('\n✅ 3D 야구게임 서버 실행됨')
    print(f'👉 브라우저 주소: {url}')
    print('종료하려면 Ctrl+C\n')
    if not args.no_open:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    httpd.serve_forever()
