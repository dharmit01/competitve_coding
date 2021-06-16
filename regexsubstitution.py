# One can solve this challenge by using the re.sub() tool along with (?<= ) which is a positive lookbehind that makes sure that the pattern is preceded by a space. Also, by using (?= ) which is a positive lookahead that makes sure that the pattern is followed by a space.


import re

for line in range(int(input())):
    string = ''
    string = re.sub(r'(?<= )&&(?= )','and',input())
    string = re.sub(r'(?<= )\|\|(?= )','or',string)
    print(string)