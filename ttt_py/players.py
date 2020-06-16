import json

class Players:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    #get_win and get_lose return integer!
    def get_win(self):
        
        dic = read_scoreboard()
        
        return dic.get(self.name)[0]
    
    def get_lose(self):
        
        dic = read_scoreboard()

        return dic.get(self.name)[1]

    def first_init(self):
        
        dic = read_scoreboard()
        
        with open("scoreboard.json", 'w') as scoreboard:
            
            dic[self.name] = [0, 0]
            json.dump(dic, scoreboard)
        
        return

    def update_scoreboard(self, win_or_lose):
        
        dic = read_scoreboard()
        
        win = self.get_win()
        lose = self.get_lose()
        
        if win_or_lose == "win":
           
            with open("scoreboard.json", 'w') as scoreboard:
                dic[self.name] = [win + 1, lose]
                json.dump(dic, scoreboard)
        
        else:
        
            with open("scoreboard.json", 'w') as scoreboard:
                dic[self.name] = [win, lose + 1]
                json.dump(dic, scoreboard)
    
    def turn(self):
        turn = input(f"\n\n{self.name} where on the grid will you want to put your {self.mark}:\n")
        return turn

    
def read_scoreboard():
    
    with open("scoreboard.json", 'r') as scoreboard_:
        dic = json.load(scoreboard_)
        
        return dic

def display_scoreboard():

    dic = read_scoreboard()
    
    print("   Tic-Tac-Toe")
    
    for name, score in dic.items():
        print(f"{name} | {score[0]} wins, {score[1]} loses")
    
    return

