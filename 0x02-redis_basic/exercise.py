#!/usr/bin/env python3
"""For some reason it may work like this
"""
import uuid
import redis
from typing import Union, Optional
from functools import wraps


def count_calls(method: callable) -> callable:
    """DocDoc Doc Doc
    """
    @wraps(method)
    def wrapped(self, *args, **kwargs) -> callable:
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapped

def call_history(method):
    """DocDoc Doc Doc
    """
    @wraps(method)
    def wrapper(self, *argv, **kwargs):
        retValue = method(self, *argv, **kwargs)
        inputL = f"{method.__qualname__}:inputs"
        outputL = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputL, str(argv))
        self._redis.rpush(outputL, retValue)
        return retValue
    return wrapper

class Cache():
    def __init__(self) -> None:
        """Forget about it you wouldnt get it
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ THis is a docDocDoc
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, id: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """This sisissisis
        """
        data = self._redis.get(id)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, id: str) -> Union[str, bytes, int, float]:
        """THis DocDocDOc dic
        """
        return self.get(id, lambda x: x.decode('utf-8'))

    def get_int(self, id: str) -> Union[str, bytes, int, float]:
        """THis DocDocDOc dic
        """
        return self.get(id, lambda x: int(x))
