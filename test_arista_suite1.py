
import requests
from requests.auth import HTTPBasicAuth

def get_data():
    xx = requests.post('http://192.168.56.101/command-api',auth=HTTPBasicAuth('python','python'),
                  json={"method": "runCmds", "jsonrpc": "2.0", "id": "moo",  "params": {"cmds": ['show interfaces'], "version": 1,}})
    resp = xx.json()

    for interf in resp['result'][0]['interfaces']:
        print(interf)
    return resp['result'][0]['interfaces'] or None

def test_all_interfaces():
    assert 'Management1' in get_data()