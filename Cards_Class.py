# SINCE I DON'T HAVE TO INHERIT ANYTING I AM NOT USING BRACKETS
class Cards:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank + ' of ' + self.suit 
      
