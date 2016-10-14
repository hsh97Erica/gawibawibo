"""
.. module:: gawibawibo
   :platform: Unix, Windows
   :synopsis: A GawoBawoBo module.
.. moduleauthor:: Hwang se hyeon <imscs21@hanyang.ac.kr>
"""
from curses.ascii import isdigit
from collections import __main__
stringdata = ["가위","바위","보"]
import random

# 1. 가위, 2. 바위 , 3. 보
def anjuncoding():
    """This function returns index value as int with safe coding 
        Currently, In this 1.0 version, input gayui,bayui,bo as index int number 

        it will return index value 
        
        Args:
            - None
        Returns:
            return int value. Return code::
            
                0 -- 가위
                1 -- 바위
                2 -- 보
    """
    question = "가위, 바위, 보를 숫자로 입력하시오(순서대로 0,1,2)"
    ipt = input(question)
    while((not ipt.isdecimal()) and int(ipt)>=0 and int(ipt)<3):
        
        print("잘 못 입력하셨습니다.")
        ipt= input(question)
    return int(ipt)
def choose():
    """
        This function peeks index for Computer(AI)
        it will return index value  
        
        Args:
            - None
        Returns:
            return int value. Return code::
            
                0 -- 가위
                1 -- 바위
                2 -- 보
    """
    return int(random.choice('012'))
def check(comp,usr):
    """ This function will check who wins 
        int comp and int usr is parameter as gawibawibo index, and each variable format is int;  
        Args:
            - comp (int): Integer computer response
            - usr (int): Integer user response

        Returns:
            return int value. Return code::
            
                -1 -- Computer Wins
                0 -- Draw Game
                1 -- User Wins
    """
   
    r=0
    r=comp-usr
    if(r==2 or r==-1):
        r=1
    elif(r==1 or r==-2):
        r=-1
    else:
        r=0
   
    return r
def start():
    """This function let python start game
        
        Returns: 
            there is no return value
    """
    isAutoMode = False
    for _ in range(0,10):
        computer = choose()
        user = -1
        if(not isAutoMode):
            user = anjuncoding()
        else: 
            user = choose()
        chk = check(computer,user)

    
        if(chk==-1):
            print("컴퓨터가 승리했습니다.")
        elif(chk==1):
            print("플레이어가 승리했습니다.")
        elif(chk==0):
            print("컴퓨터와 플레이어가 비김")
        else:
            print("알 수 없는 판정",chk)
if("__main__"== __name__):
    start()