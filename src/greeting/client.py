from enum import Enum

import grpc
from service_pb2 import AddRequest, GreetingRequest, Language
from service_pb2_grpc import GreetingsStub


class LanguageEnum(Enum):
    RUSSIAN = "RUSSIAN"
    ENGLISH = "ENGLISH"


def generate_default_client() -> GreetingsStub:
    channel = grpc.insecure_channel("localhost:50051")
    client = GreetingsStub(channel)
    return client


class GreetingClient:
    @staticmethod
    def greet(
        name: str,
        language: LanguageEnum,
        client: GreetingsStub = generate_default_client(),
    ) -> str:
        request = GreetingRequest(name=name, language=language.value)
        return client.Greet(request).greeting

    @staticmethod
    def add(a: int, b: int, client: GreetingsStub = generate_default_client()) -> int:
        request = AddRequest(a=a, b=b)
        return client.Add(request).answer


def main() -> None:
    print(GreetingClient.greet(name="Danila", language=LanguageEnum.ENGLISH))

    print(GreetingClient.add(a=5, b=3))


if __name__ == "__main__":
    main()
