import os
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Callable

import grpc
from grpc._channel import _InactiveRpcError
from grpc_interceptor import ClientInterceptor

from src.greeting.service_pb2 import AddRequest, GreetingRequest, Language
from src.greeting.service_pb2_grpc import GreetingsStub


class ErrorLogger(ClientInterceptor):
    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        try:
            return method(request_or_iterator, call_details)
        except Exception:
            print(
                f"""
time: {datetime.now(timezone.utc)}
payload: {str(request_or_iterator).rstrip("\n")}
call_details: {call_details}"""
            )


class LanguageEnum(Enum):
    RUSSIAN = "RUSSIAN"
    ENGLISH = "ENGLISH"


def generate_default_client() -> GreetingsStub:
    interceptors = [ErrorLogger()]
    recommendations_host = os.getenv("SERVICE_HOST", "localhost")
    channel = grpc.insecure_channel(f"{recommendations_host}:51744")
    channel = grpc.intercept_channel(channel, *interceptors)
    client = GreetingsStub(
        channel,
    )
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
            raise ValueError(
                "INVALID_ARGUMENT, you are not allowed to use name equal to Danila"
            ) from exc

    @staticmethod
    def add(a: int, b: int, client: GreetingsStub = generate_default_client()) -> int:
        request = AddRequest(a=a, b=b)
        return client.Add(request).answer


def main() -> None:
    print(GreetingClient.add(a=5, b=3))
    print(GreetingClient.greet(name="User", language=LanguageEnum.ENGLISH))
    print(GreetingClient.greet(name="Пользователь", language=LanguageEnum.RUSSIAN))


if __name__ == "__main__":
    main()
