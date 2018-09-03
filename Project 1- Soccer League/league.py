import csv
import os

#Method for adding  players list into teams dictionaries
def append_items(players, x, y):
    items = []
    for i in range(x, y):
        items.append(players[i])
    return items

# Main function will run as native file
if __name__  == '__main__':

    # If file exists from previous run delete it
    if os.path.exists("teams.txt"):
        os.remove("teams.txt")
    # Getting data freom csv file into experienced and non experienced students lists
    input_file = csv.DictReader(open("soccer_players.csv"))
    soccer_player_list_exp = []
    soccer_player_list_inexp = []
    for row in input_file:
        exp = row["Soccer Experience"]
        if exp == "YES":
            soccer_player_list_exp.append(row)
        else:
            soccer_player_list_inexp.append(row)
    teams = {}
    exp_players = []
    inexp_players = []

    # Assigning experienced players into teams
    teams["dragons"] = append_items(soccer_player_list_exp, 0, 3)
    teams["sharks"] = append_items(soccer_player_list_exp, 3, 6)
    teams["raptors"] = append_items(soccer_player_list_exp, 6, 9)

    # Assigning non-experienced players into teams
    for item in teams.items():
        if item[0] == "dragons":
            item[1].extend(append_items(soccer_player_list_inexp, 0, 3))
        if item[0] == "sharks":
            item[1].extend(append_items(soccer_player_list_inexp, 3, 6))
        if item[0] == "raptors":
            item[1].extend(append_items(soccer_player_list_inexp, 6, 9))
    
    # Printing teams.txt file
    def print_teams():
        player_data = ""
        for item in teams.items():
            title = "{}".format(item[0].title()) + "\n" + "========="
            with open("teams.txt", "a") as file:
                file.write(title + "\n")
            for player in item[1]:
                player_data = player["Name"] + ", " +  player["Soccer Experience"] + ", " + player["Guardian Name(s)"]
                with open("teams.txt", "a") as file:
                    file.write(player_data + "\n")
            with open("teams.txt", "a") as file:
                    file.write("\n")

    # Creating file
    print_teams()
                



    
