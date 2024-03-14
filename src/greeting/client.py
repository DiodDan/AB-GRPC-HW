from enum import Enum

import grpc
from service_pb2 import AddRequest, GreetingRequest, Language
from service_pb2_grpc import GreetingsStub
from grpc._channel import _InactiveRpcError


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
        try:
            return client.Greet(request).greeting
        except _InactiveRpcError as exc:
            raise ValueError("INVALID_ARGUMENT, you are not allowed to use name equal to Danila") from exc

    @staticmethod
    def add(a: int, b: int, client: GreetingsStub = generate_default_client()) -> int:
        request = AddRequest(a=a, b=b)
        return client.Add(request).answer


def main() -> None:
    print(GreetingClient.add(a=5, b=3))
    print(GreetingClient.greet(name="Danila", language=LanguageEnum.ENGLISH))
    print(GreetingClient.greet(name="Semen", language=LanguageEnum.ENGLISH))



if __name__ == "__main__":
    main()
