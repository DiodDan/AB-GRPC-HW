import random
from concurrent import futures

import grpc
import service_pb2_grpc
from service_pb2 import (AddRequest, AddResponse, GreetingRequest,
                         GreetingResponse, Language)


class GreetingsServicer(service_pb2_grpc.GreetingsServicer):
    def Greet(self, request: GreetingRequest, context) -> GreetingResponse:
        if request.language == Language.RUSSIAN:
            return GreetingResponse(greeting=f"Привет {request.name}!")
        if request.language == Language.ENGLISH:
            return GreetingResponse(greeting=f"Hello {request.name}!")

    def Add(self, request: AddRequest, context) -> AddResponse:
        return AddResponse(answer=request.a + request.b)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreetingsServicer_to_server(GreetingsServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
