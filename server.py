#!/usr/bin/env python3
"""Orbite leaderboard server — zéro dépendance (stdlib only)."""

import json, sqlite3, os, re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'leaderboard.db')
PORT = int(os.environ.get('PORT', 8081))
CORS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
}

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute('''CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_score ON scores(score DESC)')
    conn.commit()
    conn.close()

def get_leaderboard(limit=10):
    conn = sqlite3.connect(DB)
    rows = conn.execute(
        'SELECT name, score FROM scores ORDER BY score DESC LIMIT ?', (limit,)
    ).fetchall()
    conn.close()
    return [{'name': r[0], 'score': r[1]} for r in rows]

def add_score(name, score):
    name = re.sub(r'[<>&"\']', '', name)[:20] or 'Anonyme'
    score = max(0, min(999999, int(score)))
    conn = sqlite3.connect(DB)
    conn.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (name, score))
    conn.commit()
    conn.close()
    return {'ok': True, 'name': name, 'score': score}

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/leaderboard':
            data = get_leaderboard()
            self._json(200, data)
        else:
            self._json(404, {'error': 'not found'})

    def do_POST(self):
        path = urlparse(self.path).path
        if path == '/score':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                payload = json.loads(body)
                result = add_score(payload.get('name', 'Anonyme'), payload.get('score', 0))
                self._json(200, result)
            except (json.JSONDecodeError, ValueError, TypeError) as e:
                self._json(400, {'error': str(e)})
        else:
            self._json(404, {'error': 'not found'})

    def _json(self, status, data):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        for k, v in CORS_HEADERS.items():
            self.send_header(k, v)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        # Quieter logging
        if args:
            print(f'[leaderboard] {args[0]} {args[1]} {args[2] if len(args) > 2 else ""}')

if __name__ == '__main__':
    init_db()
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f'🌀 Orbite leaderboard API → http://localhost:{PORT}')
    print(f'   GET  /leaderboard  (top 10 scores)')
    print(f'   POST /score        {{"name":"...","score":N}}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nArrêt.')
        server.server_close()
