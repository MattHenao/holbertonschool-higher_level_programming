#!/usr/bin/python3
def multiple_returns(sentence):
    longer = len(sentence)
    if longer == 0:
        return(longer, None)
    return(longer, sentence[0])
