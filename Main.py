#-*- coding:utf-8 -*-
# ====================================================== #
# Yonsei University - Seamless Transportation Laboratory #
# Ho Suk, Jae-Young Moon                                 #
# sukho93@yonsei.ac.kr                                   #
# ====================================================== #

from NMEAInterpreter import*

import time

def main():
    try:
        MyNMEAInterpreter = NMEAInterpreter()
            
        while True:
            MyNMEAInterpreter.convertDataUnit4PX2()
            time.sleep(0.01)
    finally:
        MyNMEAInterpreter.MySerialCommunicator.ser.close()
    
if __name__ == "__main__":
    main()