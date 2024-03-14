from concurrent import futures
import random

import grpc

from service_pb2 import (
    GreetingRequest,
    Language,
    GreetingResponse,
)
import service_pb2_grpc


class GreetingsServicer(
    service_pb2_grpc.GreetingsServicer
):
    def Greet(self, request, context):
        if request.language == Language.RUSSIAN:
            return GreetingResponse(greeting=f"Привет {request.name}!")
        if request.language == Language.ENGLISH:
            return GreetingResponse(greeting=f"Hello {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreetingsServicer_to_server(
        GreetingsServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
