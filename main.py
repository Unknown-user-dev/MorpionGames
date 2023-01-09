import colorama
from colorama import Fore, Back, Style
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


colorama.init()

banner = Fore.CYAN + """

  __  __                  _                _____                             _ 
 |  \/  |                (_)              / ____|                           | |
 | \  / | ___  _ __ _ __  _  ___  _ __   | |  __  __ _ _ __ ___   ___  ___  | |
 | |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \  | | |_ |/ _` | '_ ` _ \ / _ \/ __| | |
 | |  | | (_) | |  | |_) | | (_) | | | | | |__| | (_| | | | | | |  __/\__ \ |_|
 |_|  |_|\___/|_|  | .__/|_|\___/|_| |_|  \_____|\__,_|_| |_| |_|\___||___/ (_)
                   | |                                                         
                   |_|                                                         
                        Created By Unknown User
"""

def menu(): 
    print(banner)
    print(Fore.RED + "1. Jouer")
    print(Fore.RED +"2. Règles")
    print(Fore.RED + "3. Quitter")
    choice = input(Fore.GREEN + "Choix : ")
    if choice == "1":
        play_game()
    elif choice == "2":
        rules()
    elif choice == "3":
        exit()
    else:
        print("Erreur : Veuillez choisir une option valide")
        menu()

def rules():
    print("Règles du jeu :")
    print("Le but du jeu est d'aligner 3 symboles identiques (X ou O) sur une grille de 3x3 cases.")
    print("Chaque joueur joue à tour de rôle, en plaçant son symbole dans une case vide de la grille.")
    print("Le premier joueur à aligner 3 symboles identiques a gagné.")
    print("Si la grille est remplie et qu'aucun joueur n'a aligné 3 symboles identiques, alors la partie est nulle.")
    print("Appuyez sur Entrée pour revenir au menu")
    input()
    menu()


board = [[' ' for _ in range(3)] for _ in range(3)]

players = [Fore.RED + "X" + Style.RESET_ALL, Fore.BLUE + "O" + Style.RESET_ALL]

game_grid = [[' ' for _ in range(3)] for _ in range(3)]

def display_grid():
    print(Fore.WHITE + '   ' + ' | '.join([str(i) for i in range(1, 4)]))
    print(Fore.WHITE + ' ' + '-' * 11)
    for i, row in enumerate(game_grid):
        print(Fore.WHITE + f'{i+1} ' + ' | '.join([Fore.RED + cell + Fore.WHITE if cell == 'X' else Fore.YELLOW + cell + Fore.WHITE if cell == 'O' else cell for cell in row]))

def update_grid(x, y, symbol): 
    game_grid[x][y] = symbol

def check_win(symbol):
    for row in game_grid:
        if row == [symbol, symbol, symbol]:
            return True
    for col in range(3):
        if game_grid[0][col] == symbol and game_grid[1][col] == symbol and game_grid[2][col] == symbol:
            return True
    if game_grid[0][0] == symbol and game_grid[1][1] == symbol and game_grid[2][2] == symbol:
        return True
    if game_grid[0][2] == symbol and game_grid[1][1] == symbol and game_grid[2][0] == symbol:
        return True
    return False

def check_full():
    for row in game_grid: 
        if ' ' in row: 
            return False
    return True

def get_move(symbol):
    while True:
        try:
            x = int(input(f"{symbol}: Où souhaitez-vous jouer votre coup ? (ligne) ")) - 1
            y = int(input(f"{symbol}: Où souhaitez-vous jouer votre coup ? (colonne) ")) - 1
            if x in range(3) and y in range(3) and game_grid[x][y] == ' ':
                update_grid(x, y, symbol)
                break
            else:
                print(Fore.RED + "Erreur : Ce coup n'est pas valide. Veuillez recommencez")
        except ValueError:
            print(Fore.RED + "Erreur : Ce coup n'est pas valide. Veuillez recommencez")

def play_game():
    turn = 0
    while True:
        cls()
        display_grid()
        get_move(players[turn])
        if check_win(players[turn]):
            display_grid()
            print(Fore.GREEN + f"{players[turn]} a gagné !")
            break
        elif check_full():
            display_grid()
            print(Fore.GREEN + "Match nul !")
            break
        turn = 1 - turn

if __name__ == '__main__':
    menu()

