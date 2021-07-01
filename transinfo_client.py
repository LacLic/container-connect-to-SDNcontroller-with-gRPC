from __future__ import print_function
import logging
import grpc
import json
import transinfo_pb2
import transinfo_pb2_grpc
import xdpcontrol


def run(info, prev_time):
    # connect
    with grpc.insecure_channel('30.0.1.102:11451') as channel:
        stub = transinfo_pb2_grpc.TransInfoStub(channel)
        response = stub.GetInfo(transinfo_pb2.InfoSending(
            type=info['type'],
            protocol=info['protocol'],
            saddr=info['data']['saddr'],
            sport=int(info['data']['sport']),
            send_byte=info['data']['send_byte'],
            daddr=info['data']['daddr'],
            dport=int(info['data']['dport']),
            recv_byte=info['data']['recv_byte'],
            time=int(info['data']['time']),
            pid=info['data']['pid'],
            com=info['data']['com'],
            host=info['host'],
            prev_time=prev_time))
    print(info)
    print("Package sent successfully with return code " +
          str(response.reply_code) + ".")
    return response.reply_code, response.reply


"""
string type = 1;
string protocol = 2;
string saddr = 3;
int32 sport = 4;
int32 send_byte = 5;
string daddr = 6;
int32 dport = 7;
int32 recv_byte = 8;
int32 time = 9;
int32 pid = 10;
string com = 11;
string host = 12;
int32 prev_time = 13;
"""


def transinfo(msg=None, prev_time=0):
    logging.basicConfig()
    print(msg)
    reply_code, reply = run(msg, prev_time)
    print(reply)
    if reply_code == 2:
        xdpcontrol.xdpcontrol(list(reply))


def get_time():
    import time
    return time.time()


if __name__ == '__main__':
    transinfo({'type': 'ip4', 'host': '30.0.1.227', 'data': {'daddr': '10.168.16.15', 'send_byte': 773, 'sport': '5901', 'recv_byte': 10,
                                                             'time': get_time(), 'dport': '47420', 'com': 'Xtightvnc', 'saddr': '30.0.1.227', 'pid': 1243}, 'protocol': 'tcp'},
              prev_time=0)
