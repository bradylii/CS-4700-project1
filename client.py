import socket, ssl, json

def main():
# Conditional tag logic for TCP 27993 vs TLS 27994
    port = 27993
    buf = bytearray()

    sock = socket.create_connection(("proj1.4700.network", port), None)

    # Wrap socket for cryptographic layer for TLS, SSL runs over TCP connection
    if port == 27994:
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname = "proj1.4700.network")

    # Helper to send to server
    def send_json_line(sock, obj):
        json_string = json.dumps(obj, separators=(",", ":"))
        byte_data = json_string.encode("ascii")
        byte_data += b"\n"
        sock.sendall(byte_data)

    # Helper to seperate messages with buffer for \n
    def recv_line(sock, buf):
        while True:
            new_line_index = buf.find(b"\n")
            # we hit a \n
            if new_line_index != -1:
                line = bytes(buf[:new_line_index]) # capture the full line
                del buf[:new_line_index + 1] # remove line and new line
                return line
            # load next chunk
            chunk = sock.recv(4096)
            if chunk == b"":
                raise ConnectionError("server closed connection")
            # add chunk to buffer
            buf.extend(chunk)


    # Helper to recieve and turn to proper json messages
    def recv_json(sock, buf): 
        byte_line = recv_line(sock, buf)
        str_line = byte_line.decode("ascii")
        return json.loads(str_line)
    
    hello = {
        "type": "hello",
        "northeastern_username" : "li.bra"
    }

    send_json_line(sock, hello)
    msg = recv_json(sock, buf)
    print(msg)



if __name__ == "__main__":
    main()