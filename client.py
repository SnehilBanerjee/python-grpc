import grpc

from proto import user_pb2
from proto import user_pb2_grpc

channel = grpc.insecure_channel('localhost:4001')

stub = user_pb2_grpc.HelloStub(channel)

# create a valid request message
user_name = user_pb2.User(first_name='Snehil',last_name='Banerjee')

response = stub.hello_user(user_name)

# et voilà
print(response.resp)