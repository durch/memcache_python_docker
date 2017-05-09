# coding=utf-8
import json
import os

from hello import MyClient, json_serializer, json_deserializer, MyHashClient

host1 = os.environ.get("MEMCACHED_1_HOST", "192.168.99.100")
port1 = int(os.environ.get("MEMCACHED_1_PORT", 11211))
host2 = os.environ.get("MEMCACHED_2_HOST", "192.168.99.100")
port2 = int(os.environ.get("MEMCACHED_2_PORT", 11212))

client = MyHashClient([
    (host1, port1),
    (host2, port2)], serializer=json_serializer, deserializer=json_deserializer)

# client = MyClient((
#     os.environ.get("MEMCACHED_1_HOST", "192.168.99.100"), 11211),
#     serializer=json_serializer, deserializer=json_deserializer)

print(client.clients)
print("--------------")
print(client.clients[f'{host1}:{port1}'].stats())
print(client.clients[f'{host2}:{port2}'].stats())

client.set('test_str', 'test_value')
client.set('test_str', 'test_value')
assert (client.get('test_str') == 'test_value'.encode())
client.set('test_dict', {"test": "dict"})
client.set('test_list', ["test", "list"])

client.append('test_str', '_sufix')
assert (client.get('test_str') == "test_value_sufix".encode())
client.prepend('test_str', 'prefix_')
assert (client.get('test_str') == "prefix_test_value_sufix".encode())
assert (client.get('test_dict') == {"test": "dict"})
client.append('test_dict', {"suf": "ix"})
try:
    client.get('test_dict')
    assert False
except json.decoder.JSONDecodeError:
    assert True
assert (client.get('test_list') == ["test", "list"])
client.replace('test_list', ['list', 'test'])
assert (client.get('test_list') == ['list', 'test'])

print("--------------")
print("All is well")
