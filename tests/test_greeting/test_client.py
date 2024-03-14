import pytest
from src.greeting.service_pb2 import AddRequest, GreetingRequest, Language
from src.greeting.client import GreetingClient, LanguageEnum


def test_greeting() -> None:
    request1 = GreetingRequest(name="Name", language=Language.ENGLISH)
    request2 = GreetingRequest(name="Another", language=Language.ENGLISH)
    request3 = GreetingRequest(name="Danila", language=Language.ENGLISH)

    response1 = GreetingClient.greet(name="Name", language=LanguageEnum.ENGLISH)
    response2 = GreetingClient.greet(name="Another", language=LanguageEnum.ENGLISH)
    with pytest.raises(ValueError):
        GreetingClient.greet(name="Danila", language=LanguageEnum.ENGLISH)


    assert response1 == "Hello Name!"
    assert response2 == "Hello Another!"


def test_add() -> None:
    response1 = GreetingClient.add(a=1, b=2)
    response2 = GreetingClient.add(a=1, b=10)
    response3 = GreetingClient.add(a=1000, b=-1)

    assert response1 == 3
    assert response2 == 11
    assert response3 == 999

