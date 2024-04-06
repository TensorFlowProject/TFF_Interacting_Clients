from concurrent import futures
import time

import grpc
import greet_pb2
import greet_pb2_grpc
import greet_client
#import New_Thing_Server
global_weights = None
global_biases = None
class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    # Global variables to store weights and biases
    def SayHello(request, context):
        global global_weights, global_biases
        
        print("SayHello Request Made:")
        hello_reply = greet_pb2.HelloReply()
        # Access weights and biases arrays
        weights = request.weights
        biases = request.biases
        print("Weights array:", weights)
        print("Biases array:", biases)
        
        # Assign weights and biases to global variables
        global_weights = weights
        global_biases = biases
        return hello_reply
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
print("Hello")    