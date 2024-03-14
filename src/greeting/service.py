from concurrent import futures

from grpc_interceptor import ExceptionToStatusInterceptor, ServerInterceptor
import grpc
import service_pb2_grpc
from service_pb2 import (AddRequest, AddResponse, GreetingRequest,
                         GreetingResponse, Language)
from datetime import datetime, timezone

class ErrorLogger(ServerInterceptor):
    def intercept(self, method, request, context, method_name):
        try:
            return method(request, context)
        except Exception as e:
            self.log_error(e, request, context)
            raise

    def log_error(self, e: Exception, request, context) -> None:

        print(f"""
time: {datetime.now(timezone.utc)}
payload: {str(request).rstrip("\n")}
status: {context.code()}""")


class GreetingsServicer(service_pb2_grpc.GreetingsServicer):
    def Greet(self, request: GreetingRequest, context) -> GreetingResponse:
        if request.name == "Danila":
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "I am not allowed to say hello to Danila")
        if request.language == Language.RUSSIAN:
            return GreetingResponse(greeting=f"Привет {request.name}!")
        if request.language == Language.ENGLISH:
            return GreetingResponse(greeting=f"Hello {request.name}!")

    def Add(self, request: AddRequest, context) -> AddResponse:
        return AddResponse(answer=request.a + request.b)


def serve() -> None:
    interceptors = [ExceptionToStatusInterceptor(), ErrorLogger()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors)
    service_pb2_grpc.add_GreetingsServicer_to_server(GreetingsServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
