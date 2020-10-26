"""
test grpc transmit speed.

Created On 26th Oct, 2020
Author: bohang.li@shopee.com
"""

import grpc
import test_pb2
import test_pb2_grpc
from concurrent import futures
import argparse


class SpeedTest(test_pb2_grpc.SpeedTestServicer):
    def work(self, request, context):
        ret = test_pb2.Reply()
        ret.ret = "received"
        return ret


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    test_pb2_grpc.add_SpeedTestServicer_to_server(
        SpeedTest(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()
    print("business server running on port " + str(port) + " ...")
    server.wait_for_termination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", default=50051, type=int, help="port number.")
    args = parser.parse_args()
    serve(port=args.port)
