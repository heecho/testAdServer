import socket

HOST, PORT = '', 8888

def run_server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)

    print 'Serving HTTP on port %s ...' % PORT
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(4096)
        request_line = request.split('\r\n')
        print request_line
        request_first_part = request_line[0].split(' ')
        request_verb = request_first_part[0]
        request_page = request_first_part[1]
        print request_verb, request_page

        http_response = """HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"""
      
        http_response += ad_page()

        client_connection.sendall(http_response)
        client_connection.close()

def read_page(page):
	page_file = page
	with open(page_file, 'r') as f:
		return f.read()

def ad_page():
	print "serving ad"
	return read_page('testAd.html')

run_server()