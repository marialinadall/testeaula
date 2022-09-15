import os
import argparse

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--canal", help= "canal")
parametros = parser.parse_args()

canal = parametros.canal

os.environ["pubsub_uuid"] = "marialina-pc"

pnconfig = PNConfiguration()

pnconfig.uuid = os.environ["pubsub_uuid"]
os.environ["pubsub_pub"] = "pub-c-04250ae0-dda0-42b0-98ba-741650176bb7"
os.environ["pubsub_sub"] = "sub-c-2dff428c-9b94-4da1-9816-66229f3315cd"

pnconfig.publish_key = os.getenv("pubsub_pub")
pnconfig.subscribe_key = os.getenv("pubsub_sub")

usr = input("Seu nome: ")
print("-"*50)

pubnub = PubNub(pnconfig)

while True:
    msg = input("Fala ae: ")
    envelope = pubnub.publish().channel(canal).message({"msg": msg, "usr": usr}).sync()

    if envelope.status.is_error():
        print("->>>>> DEU PAU")