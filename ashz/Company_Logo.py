#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    _collection = {}
    for i in list(s):
        if i not in _collection.keys():
            _collection.update({i: 1})
        else:
            _collection.update({i: _collection[i]+1})
    
    for _ in range(3):
        big = 0
        _char = None
        for i in _collection.keys():
            if _collection[i] > big:
                big = _collection[i]
                _char = i
            elif _collection[i] == big:
                if ord(i) < ord(_char):
                    big = _collection[i]
                    _char = i
        
        _collection.pop(_char)
        print(_char + ' ' + str(big))
