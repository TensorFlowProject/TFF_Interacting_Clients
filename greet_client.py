import greet_pb2_grpc
import greet_pb2
import time
import grpc
import New_Thing

def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            # Populate HelloRequest message with name, greeting, weights, and biases
            weights, biases = New_Thing.train()
            hello_request = greet_pb2.HelloRequest(
                greeting="Bonjour",
                name="YouTube",
                weights=weights,
                biases=biases
            )
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)




if __name__ == "__main__":
    run()