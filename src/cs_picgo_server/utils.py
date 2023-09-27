import socket


def test_bind_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.bind(('', port))
        except:
            return False
        else:
            return True
