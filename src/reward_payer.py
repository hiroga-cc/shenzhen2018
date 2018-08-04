# coding: utf-8
import time
from garbage_sensor import GarbageSensor
from addr import AddrHandler
from addr_validator import *
from wallet import Wallet
from director import Director

PAY_AMOUNT = "0.000039" # Thank you!

class RewardPayer():
    def __init__(self):
        self.sensor = GarbageSensor()
        self.addr_handler = AddrHandler()
        self.wallet = Wallet()
        self.director = Director()

    def reception_open(self):
        while True:
	    time.sleep(0.5)
            if self.sensor.was_trash_thrown() == True:
                self.director.play_bell()
                decorated_addr = self.addr_handler.cut_addr()
                if decorated_addr == "":
                    print("QRコードリーダーから何も読み取っていません.")
                    continue
                addr = trim_addr(decorated_addr)
                # 本当はここでアドレスのValidationを実施
                if addr == None:
                    print("アドレスの形式が不正です.")
                    continue
                self.wallet.payment(addr, PAY_AMOUNT)
                print("Payment Complete! Pay to:" + addr + " Amount: " + PAY_AMOUNT)
                self.director.play_thanks()
