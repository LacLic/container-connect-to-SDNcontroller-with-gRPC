from concurrent import futures
import time
import grpc
import logging
import transinfo_pb2
import transinfo_pb2_grpc


class TransInfo:

    def GetInfo(self, request, context):
        return transinfo_pb2.SuccessReply(reply=len(request.info))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transinfo_pb2_grpc.add_TransInfoServicer_to_server(TransInfo(), server)
    server.add_insecure_port('[::]:11451')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
