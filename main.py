import os 

def clear_screen():
    os.system("cls")

class players:
    def __init__(self) :
        self.__name=""
        self.__symbol=""


    def choice_name(self):
        while True:
            self.name=input("enter your name [letters only]:\n")

            if self.name.isalpha():
                    break
            else:
                    print("Invalid name. Please use letters only.\n")



    def choice_symbol(self):
      while True:
        symbol=input(f"welcome {self.name} enter your symbol: ")
        symbol=symbol.upper()
        if symbol=="X" or symbol== "O" :
         self.symbol=symbol
         break
        else:
         print("please choice x or o only")

class Menu:
    def display_main_menu(self):
        print("Welcome to my X-0 game!")
        print("1. Start Game")
        print("2. Quit Game")
        choice = input("Enter your choice (1 or 2): ")
        return choice
    def display_endgame_menu(self):
        menu_text ="""
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2): """
        choice = input(menu_text)
        return choice
        
class board:
    def __init__(self):
        self.board=[str(i) for i in range (1,10)] 
    
    def display_board(self):
        for i in range(0,9,3):
            print(" | ".join(self.board[i:i+3]))
            if i<6:
                print("-"*9)
    
    def update_board(self,symbol):
        
        while True:
            num_choice=input("choose a number:  ")
            if  num_choice.isdigit():
                  num_choice=int(num_choice)
                  if num_choice > 0 and num_choice < 10 and self.board[num_choice-1].isdigit() :
                    self.board[num_choice-1]=symbol
                    break
            else:
                  
                  print("please choose a right number")
                  


    def reset_board(self):
        self.board=[str(i) for i in range (1,10)]

class game_logic():
    def __init__(self) :
        self.board=board()
        self.players=[players(),players()]
        self.menu=Menu()
        self.current_player_index=0
    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice=="1":
            self.setup_players()
            self.play_game()

        else:
            self.quit_game()

    def setup_players(self):
        for number,player in enumerate (self.players,start=1):
            print("="*20)
            print(f"player{number}")
            player.choice_name()
            player.choice_symbol()
        if self.players[0].symbol== self.players[1].symbol:
            print("please choice different symbol")
            self.setup_players()
            
    def play_game(self):
        clear_screen()
        self.board.display_board()
              
        while True:
            if self.check_win() or self.check_draw():
                end=self.menu.display_endgame_menu()
                if end=="1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            
            self.play_turn()
            symbol=self.the_player.symbol
            self.board.update_board(symbol)
            self.board.display_board()
            print(self.board.board)

    def play_turn(self):
        self.the_player=self.players[self.current_player_index]
        if self.current_player_index==0:
            self.current_player_index = self.current_player_index +1
        else :
            self.current_player_index=0
        print(f"{self.the_player.name} your symble is {self.the_player.symbol}")
        

    def check_win(self):
        win_condition=[
            [0,1,2],[3,4,5],[6,7,8],     #horizontal 
            [0,3,6],[1,4,7],[2,5,8],     #vertical   
            [0,4,8],[2,4,6]              #diagonal 
            ]             
        for com in win_condition:
            if self.board.board[ com [0]]==self.board.board[ com [1]]==self.board.board[ com[2]]:
                print(f"{self.the_player.name} is win")
                return(True)

         
    def check_draw(self):
        
        for co in range(0,9) :
            if self.board.board[co].isdigit():
                return(False)
        print("="*25)
        print("you are draw")    
        return(True)

    def restart_game(self):
        self.board.reset_board()
        self.play_game()

    def quit_game(self):
        print("-" * 9)
        print("Thank you for playing ")
        print("-" * 9 )
        print("\n")
            
    



game=game_logic()
game.start_game()
