#import sys
#import os
import requests

alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None

if __name__=='__main__':
    #url_1= "https://github.com/sora1441/4663-Cryptography/blob/master/Assignments/A03/ciphertext_1.txt"
    url_2= "https://github.com/sora1441/4663-Cryptography/blob/master/Assignments/A03/ciphertext_2.txt"
    f_1 = requests.get(url_1)
    f_2 = requests.get(url_2)
    text_1 = f_1.text
    text_2 = f_2.text
    F = Frequency()

    #F.count(text_1)
    F.count(text_2)
    F.print()
    print()
    print(F.getNth(2))