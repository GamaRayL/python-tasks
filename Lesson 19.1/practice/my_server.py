from http.server import BaseHTTPRequestHandler
from os import path

index_file = path.join(path.dirname(path.abspath(__file__)), "index.html")


class MyServer(BaseHTTPRequestHandler):

    @staticmethod
    def __get_index():
        with open(index_file) as index:
            return index.read()

    def do_GET(self):
        page_content = self.__get_index()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))
