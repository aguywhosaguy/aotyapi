from aotyapi import client

client = client.AOTYClient()


def test_aoty():
    # Tests if client can access AOTY 
    assert client.request("get", "").status_code == 200
