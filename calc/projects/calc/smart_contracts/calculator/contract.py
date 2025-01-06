from algopy import ARC4Contract, UInt64
from algopy.arc4 import abimethod


class Calculator(ARC4Contract):
    @abimethod()
    def add(self, a: UInt64,b: UInt64)->UInt64:
        return a+b
    
    @abimethod()
    def sub(self, a: UInt64,b: UInt64)->UInt64:
        return a-b
    
    @abimethod()
    def mul(self, a: UInt64,b: UInt64)->UInt64:
        return a*b
    
    @abimethod()
    def div(self, a: UInt64,b: UInt64)->UInt64:
        return a//b
