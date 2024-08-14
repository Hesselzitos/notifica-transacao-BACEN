from __future__ import print_function

import logging

import grpc
import transactionConsumer_pb2
import transactionConsumer_pb2_grpc


def run():
    consumerName = "Consumer"

    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = transactionConsumer_pb2_grpc.ConsumerStub(channel)
        listQuees = stub.ListQuees(transactionConsumer_pb2.AskForQuees(ask="Hey, whats quees do you have?"))
        quee=listQuees.listQuees[0]
        response = stub.Subscribe(transactionConsumer_pb2.AskForSubscribe(channel=quee, consumerName=consumerName))
    print(response.ack)
    print(listQuees.listQuees)


if __name__ == "__main__":
    logging.basicConfig()
    run()