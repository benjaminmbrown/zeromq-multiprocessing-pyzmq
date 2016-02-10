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

if __name__ == "__main__":
	server_ports = range(5540,5558, 4)
	for server_port in server_ports:
		Process(target=server, args=(server_port,)).start()