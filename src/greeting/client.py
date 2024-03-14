from service_pb2 import GreetingRequest, Language
import grpc
from service_pb2_grpc import GreetingsStub


def main() -> None:
    channel = grpc.insecure_channel("localhost:50051")
    client = GreetingsStub(channel)
    request = GreetingRequest(name="Danila", language="RUSSIAN")

    print(client.Greet(request))


if __name__ == "__main__":
    main()
