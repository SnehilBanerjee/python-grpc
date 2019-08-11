import grpc
from concurrent import futures
import time
from proto import user_pb2
from proto import user_pb2_grpc

import hello

class HelloServicer(user_pb2_grpc.HelloServicer):

    def hello_user(self, request, context):
        response = user_pb2.Respose()
        response.resp = hello.hello_user(request.first_name,request.last_name)
        return response

server = grpc.server(futures.ThreadPoolExecutor())

user_pb2_grpc.add_HelloServicer_to_server(
        HelloServicer(), server)

print('Starting server. Listening on port 4001.')
server.add_insecure_port('[::]:4001')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)