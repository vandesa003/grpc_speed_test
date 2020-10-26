"""
test grpc transmit speed.

Created On 26th Oct, 2020
Author: bohang.li@shopee.com
"""

import os
import grpc
import test_pb2
import test_pb2_grpc
import glob
import argparse
import time
import pandas as pd
from tqdm import tqdm


def test(ip, img):
    with grpc.insecure_channel(ip) as channel:
        req = test_pb2.Request(
            image=img
        )
        stub = test_pb2_grpc.SpeedTestStub(channel)
        ret = stub.work(req)
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", "-ip", default="127.0.0.1:30111", help="ip:port")
    parser.add_argument("--folder", "-f", default="./data/", help="image folder.")
    args = parser.parse_args()
    print("calling: {}".format(args.ip))
    print("folder: {}".format(args.folder))
    input_list = [x for x in glob.glob(os.path.join(args.folder, "*")) if x.lower().endswith((".jpg", ".png", ".jpeg"))]
    sizes = [0 for _ in range(len(input_list))]
    time_cost = [0 for _ in range(len(input_list))]
    flags = [0 for _ in range(len(input_list))]
    for i in tqdm(range(len(input_list))):
        sizes[i] = "{:.2f}".format(os.path.getsize(input_list[i]) / 1e3)
        start = time.time()
        with open(input_list[i], "rb") as img:
            ret = test(args.ip, img.read())
        end = time.time()
        time_cost[i] = "{:.4f}".format(end - start)
        flags[i] = ret.ret
    res = pd.DataFrame(columns=["filename", "size(kb)", "time_cost(s)", "flag"])
    res["filename"] = input_list
    res["size(kb)"] = sizes
    res["time_cost(s)"] = time_cost
    res["flag"] = flags
    res.to_csv("test_result.csv", index=False)
