def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

# Function to get the number of points per game for a given player name
def num_points_per_game(player_name):
    # Call the game_dict() to access the teams and players
    teams = game_dict()

    # Iterate through both home and away teams
    for team in teams.values():
        # Access the players list for each team
        for player in team["players"]:
            # Check if the current player's name matches the provided name
            if player["name"] == player_name:
                # Return the points per game for the matched player
                return player["points_per_game"]
    
    # Return None if the player is not found
    return None
print(num_points_per_game("Darius Garland")) 


# Function to get the age of a player by their name
def player_age(player_name):
    # Call the game_dict() to access the teams and players
    teams = game_dict()

    # Iterate through both home and away teams
    for team in teams.values():
        # Access the players list for each team
        for player in team["players"]:
            # Check if the current player's name matches the provided name
            if player["name"] == player_name:
                # Return the age for the matched player
                return player["age"]
    
    # Return None if the player is not found
    return None

print(player_age("Bradley Beal"))  

# Function to get the colors of a team by its name
def team_colors(team_name):
    # Call the game_dict() to access the teams
    teams = game_dict()

    # Iterate through both home and away teams
    for team in teams.values():
        # Check if the current team's name matches the provided team name
        if team["team_name"] == team_name:
             # Return the list of colors for the matched team
              return team["colors"]
        
    # Return None if the team is not found
    return None

print(team_colors("Cleveland Cavaliers"))

# Function to get a list of all team names
def team_names():
    # Call the game_dict() to access the teams
    teams = game_dict()

    # Create a list to store team names
    names = []
    # Iterate through both home and away teams
    for team in teams.values():
        # Append the team name to the list
        names.append(team["team_name"])

    # Return the list of team names
    return names

print(team_names())      

# Function to get player jersey numbers for a specific team
def player_numbers(team_name):
    # Call the game_dict() to access the teams
    teams = game_dict()

    # Create a list to store jersey numbers
    numbers = []
    # Iterate through both home and away teams
    for team in teams.values():
        # Check if the current team's name matches the provided team name
        if team["team_name"] == team_name:
            # Iterate through the players list and collect jersey numbers
            for player in team["players"]:
                numbers.append(player["number"])
            # Return the list of jersey numbers for the matched team
            return numbers

    # Return None if the team is not found
    return None

print(player_numbers("Washington Wizards"))


# Function to get all stats for a player by their name
def player_stats(player_name):
    # Call the game_dict() to access the teams and players
    teams = game_dict()

    # Iterate through both home and away teams
    for team in teams.values():
        # Access the players list for each team
        for player in team["players"]:
            # Check if the current player's name matches the provided name
            if player["name"] == player_name:
                return {
                    "name": player["name"],
                    "number": player["number"],
                    "position": player["position"],
                    "points_per_game": player["points_per_game"],
                    "rebounds_per_game": player["rebounds_per_game"],
                    "assists_per_game": player["assists_per_game"],
                    "steals_per_game": player["steals_per_game"],
                    "blocks_per_game": player["blocks_per_game"],
                    "career_points": player["career_points"],
                    "age": player["age"],
                    "height_inches": player["height_inches"],
                    "shoe_brand": player["shoe_brand"],
                }
        
    
    # Return None if the player is not found
    return None

print(player_stats("Jarrett Allen"))

def average_rebounds_by_shoe_brand():
    # Call the game_dict() to access the teams and players
    teams = game_dict()
    
    # Create a dictionary to hold shoe brands and their respective rebounds
    rebounds_by_brand = {}

    # Iterate through both home and away teams
    for team in teams.values():
        # Access the players list for each team
        for player in team["players"]:
            brand = player["shoe_brand"]  # Get the player's shoe brand
            rebounds = player["rebounds_per_game"]  # Get the player's rebounds
            
            # Check if the shoe brand already exists in the dictionary
            if brand not in rebounds_by_brand:
                # If not, create a new entry with an empty list
                rebounds_by_brand[brand] = []
            
            # Append the current player's rebounds to the list for the brand
            rebounds_by_brand[brand].append(rebounds)

    # Calculate and print the average rebounds for each shoe brand
    for brand, rebounds in rebounds_by_brand.items():
        average = sum(rebounds) / len(rebounds)  # Calculate average rebounds
        print(f"{brand}:  {average:.2f}")  # Add an extra space before average

average_rebounds_by_shoe_brand()
