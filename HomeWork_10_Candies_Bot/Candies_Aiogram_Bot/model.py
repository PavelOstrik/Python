# Здесь храним все перменные и методы для их чтения и установки (а-ля работа с классами)
import random
from aiogram import types

candies = 150
take = None


def getFirstMove():
    global first_move
    return first_move

def setFirstMove():
    global first_move
    first_move = random.randint(0,1)
    
def getCandies():
    global candies
    return candies

def setCandies(count: int):
    global candies
    candies = count
    
    
def getTake():
    global take
    return take

def setTake(new_take: int):
    global take
    take = new_take

def checkWin():
    if getCandies() <= 28:
        return True
    
# def getCount():
#     global total_count
#     return total_count
    
# def setCount(count: int):
#     global total_count
#     total_count = count
    
# def getUserCount():
#     global user_count
#     return user_count

# def setUserCount(count: int):
#     global user_count
#     user_count = count
    
# def checkWin():
#     if getCount() <= 0:
#         return True