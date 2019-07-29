class Player:
    def __init__(self,name,score,symbol):
        self.name = name
        self.score = score
        self.symbol = symbol
p1=Player('Neil',20,'X')
p2=Player("David",20,'o')
active_player=p1
count =0
while(True):

    if (active_player==p1):
        active_player=p2
    else:
        active_player=p1
    print(active_player.name)
    break


#create the borad
#ask size of board
#b=Board(width,length)
#Create players
p1 = Player(self.)
p2 = Player()
active_player = p1

while (True):
    if  b.isFull():
        break
#end of game
    #   else :
        active_player.play(b)
        if(b.is_there_a_winner()):
            print('End of Game')
            break

        if active_player==p1:
            active_player==p2


