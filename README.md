![](https://img.shields.io/badge/python-3.5%2B-green.svg)
![](https://img.shields.io/badge/Accumulo-1.8.1-green.svg)
![](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

# Introduction

**WIP**

This is a [thrift](https://thrift.apache.org/) generated Python 3 client library for [Apache Accumulo](https://accumulo.apache.org/).


Thrift code is generated with `thrift -r --gen py proxy.thrift` of Accumulo 1.8.1.


## Examples

These examples are in Python 3.6.

### Connection
    transport_socket: TSocket.TSocket = TSocket.TSocket('server', 42424)
    transport: TTransport.TFramedTransport = TTransport.TFramedTransport(transport_socket)
    protocol: TCompactProtocol.TCompactProtocol = TCompactProtocol.TCompactProtocol(transport)
    transport.open()
    
    client: AccumuloProxy.Client = AccumuloProxy.Client(protocol)
    login: bytes = client.login("root", {"password": "q123456"})


#### Table Operations
    table: str = "mytable"
    if not client.tableExists(login, table):
        client.createTable(login, table, True, TimeType.MILLIS)

    print(client.listTables(login))


#### Scan Table

    scanner: str = client.createScanner(login, table, ScanOptions())
    results: ScanResult = client.nextK(scanner, 200)
    for keyvalue in results.results:
        print(keyvalue)
    client.closeScanner(scanner)



#### Notes
pyaccumulo doesn't support Python 3 and I'm not sure if it's still maintained so I've created a new one.

