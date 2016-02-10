import zmq
import sys
import time
from multiprocessing import Process

def server(port="5556"):
	context = zmq.Context()
	socket = context.socket(zmq.REP)
	socket.bind("tcp://*:%s" % port)
	print "Started server on port: ", port

	while True:
		message = socket.recv()
		print "Got request  %s" % message
		socket.send("We got your request!")

def client(ports=["5556"]):
	context = zmq.Context()
	print "Connecting to server on ports %s" % ports
	socket = context.socket(zmq.REQ)
	for port in ports:
		socket.connect("tcp://localhost:%s" %port)
	for request in range(50):
		print "Sending client request", request, "..."
		socket.send("Hello")
		message = socket.recv()
		print "Got a reply", request, "[", message,"]", port
		time.sleep(0.5)

if __name__ == "__main__":
	server_ports = range(5540,5558, 1)
	for server_port in server_ports:
		Process(target=server, args=(server_port,)).start()

	Process(target=client, args=(server_ports,)).start()