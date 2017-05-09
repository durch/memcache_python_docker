# coding=utf-8
from pymemcache.client.base import Client
from pymemcache.client.hash import HashClient
import json


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value
    if flags == 2:
        return json.loads(value)
    raise Exception("Unknown serialization format")


class MyHashClient(HashClient):
    def is_set(self, key):
        return self.get(key) is not None


class MyClient(Client):
    def is_set(self, key):
        return self.get(key) is not None
