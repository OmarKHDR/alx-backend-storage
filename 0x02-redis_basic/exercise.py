#!/usr/bin/env python3
"""For some reason it may work like this
"""
import uuid
import redis
from typing import ByteString


class Cache():
	def __init__(self) -> None:
		self._redis = redis.Redis()
		self._redis.flushdb()

	def store(self, data: str | ByteString | float | int) -> str:
		id = str(uuid.uuid4())
		self._redis.set(id, data)
		return id
