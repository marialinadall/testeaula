import os
import argparse
from datetime import datetime

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--canal", help= "canal")
parametros = parser.parse_args()

canal = parametros.canal

os.environ["pubsub_uuid"] = "marialina-pc"

pnconfig = PNConfiguration()

pnconfig.uuid = os.environ["pubsub_uuid"]

os.environ["pubsub_uuid"] = "pub-c-04250ae0-dda0-42b0-98ba-741650176bb7"
os.environ["pubsub_uuid"] = "sub-c-2dff428c-9b94-4da1-9816-66229f3315cd"


pubnub = PubNub(pnconfig)


class RecebeMensagem(SubscribeCallback):
    def presence(self, pubnub, event):
        pass

    def status(self, pubnub, event):
        pass

    def message(self, pubnub, event):
        print("{}: {}\n{}".format(event.message["usr"], event.message["msg"], datetime.now().strftime("%H:%M:%S")))


pubnub.add_listener(RecebeMensagem())
pubnub.subscribe().channels(canal).with_presence().execute()