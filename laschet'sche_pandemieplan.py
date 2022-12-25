#inspiriert durch https://www.reddit.com/r/de/comments/mkt3a8/w%C3%BCrfeln_mit_armin_erstelle_deinen_eigenen/ # 

from random import randint
from satzbausteine import *

def sentence_generator():
    sent = Satzbausteine[0][0]
    sent += Satzbausteine[1][randint(0, 5)]
    sent += Satzbausteine[2][randint(0, 5)]
    sent += Satzbausteine[3][randint(0, 5)]
    sent += Satzbausteine[4][randint(0, 5)]
    sent += Satzbausteine[5][randint(0, 5)]
    sent += Satzbausteine[6][0]
    sent += Satzbausteine[7][randint(0, 5)]
    sent += Satzbausteine[8][0]
    sent += Satzbausteine[9][randint(0, 5)]
    sent += Satzbausteine[10][randint(0, 5)] 
    sent += Satzbausteine[11][0]
    sent += Satzbausteine[12][randint(0, 5)]
    return sent

if __name__ == '__main__':
    print(sentence_generator())