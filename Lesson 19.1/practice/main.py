from http.server import HTTPServer
from my_server import MyServer

hostname = "localhost"
port = 8080

if __name__ == "__main__":
    webServer = HTTPServer((hostname, port), MyServer)
    print(f"Server started http://{hostname}:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print("Server stopped.")
    
