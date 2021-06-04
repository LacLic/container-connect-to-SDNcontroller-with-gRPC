from __future__ import print_function
import logging
import grpc
import transinfo_pb2
import transinfo_pb2_grpc


def run():
    # connect
    with grpc.insecure_channel('localhost:11451') as channel:
        stub = transinfo_pb2_grpc.TransInfoStub(channel)
        response = stub.GetInfo(transinfo_pb2.InfoSending(info='1'*114514))
    print(f"Package sent successfully (length: {response.reply})")


if __name__ == '__main__':
    logging.basicConfig()
    run()
