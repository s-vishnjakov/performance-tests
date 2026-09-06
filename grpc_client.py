import grpc

import greeting_pb2
import greeting_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")

    stub = greeting_pb2_grpc.GreeterStub(channel)

    request = greeting_pb2.HelloRequest(name="Wolrd")
    response = stub.SayHello(request)
    print("Server answer:", response)


if __name__ == '__main__':
    run()