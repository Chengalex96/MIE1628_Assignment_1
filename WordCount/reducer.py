#!/usr/bin/env python  
  
from operator import itemgetter  
import sys  

def main(): 
    sum = 0
    # input comes from STDIN  
    for line in sys.stdin:  
        sum = sum + 1
    print("%s" %sum)

if __name__ == "__main__":
    main()