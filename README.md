# jsonrpc-client
Another python json-rpc client

#Install

```
sudo pip install jsonrpc-client
```

#Usage

jsonrpc-client uses requests to make request, you can pass any parameters for requests.post to jsoncliet.Client

```
>> from jsonclient import Client
>> headers = {"token":"xxxooo"}
>> rpc_client = Client("http://server_url", headers=headers)
>> print rpc_client.add(1,2)
>> 3
```