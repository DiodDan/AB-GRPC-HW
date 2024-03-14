import os

import grpc
import pytest
from grpc._channel import _InactiveRpcError

from src.greeting.service_pb2 import AddRequest, GreetingRequest, Language
from src.greeting.service_pb2_grpc import GreetingsStub


@pytest.fixture
def client() -> GreetingsStub:
    recommendations_host = os.getenv("SERVICE_HOST", "localhost")
    channel = grpc.insecure_channel(f"{recommendations_host}:5000")
    client = GreetingsStub(
        channel,
    )
    return client


def test_greeting(client: client) -> None:
    request1 = GreetingRequest(name="Name", language=Language.ENGLISH)
    request2 = GreetingRequest(name="Another", language=Language.ENGLISH)
    request3 = GreetingRequest(name="Danila", language=Language.ENGLISH)

    response1 = client.Greet(request1)
    response2 = client.Greet(request2)
    with pytest.raises(_InactiveRpcError):
        client.Greet(request3)

    assert response1.greeting == "Hello Name!"
    assert response2.greeting == "Hello Another!"


def test_add(client: client) -> None:
    request1 = AddRequest(a=1, b=2)
    request2 = AddRequest(a=1000, b=-1)
    with pytest.raises(TypeError):
        request3 = AddRequest(a="123", b=123)

    response1 = client.Add(request1)
    response2 = client.Add(request2)

    assert response1.answer == 3
    assert response2.answer == 999
