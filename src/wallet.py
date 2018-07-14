# coding: utf-8
import os
import requests


class Wallet:
    def __init__(self):
        self.guid = os.environ["GUID"]
        self.password  = os.environ["WALLET_PASSWORD"]
        self.api_code = os.environ["WALLET_API_CODE"]
        self.base_url = "http://localhost:3000"

    def payment(self, to, amount):
        payment_url = self.base_url + "/merchant/" + self.guid + "/payment?to=" + to + "&amount=" + amount + "&password=" + self.password + "&api_code=" + self.api_code
        print(payment_url)

        try:
            r = requests.post(payment_url)
            print(r)
        except requests.exceptions.ConnectionError:
            print("ConnectionError. サーバーの立ち上げ忘れがないか調べてみてください")

    def balance(self):
        balance_url = self.base_url+ '/merchant/' + self.guid + '/balance?password=' + self.password + "&api_code=" + self.api_code
        print(balance_url)

        try:
            r = requests.post(balance_url)
            print(r.text)
        except requests.exceptions.ConnectionError:
            print("ConnectionError. サーバーの立ち上げ忘れがないか調べてみてください")


if __name__ == "__main__":
    wallet = Wallet()
    wallet.balance()