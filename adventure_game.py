from a_game_pkg.characters import GameCharacter
from a_game_pkg.characters import Player
from a_game_pkg.characters import Enemy
from a_game_pkg.a_game_mod import check_list
from a_game_pkg.characters import player
from a_game_pkg.characters import goblin
from a_game_pkg.characters import ogre
from a_game_pkg.characters import orc
from a_game_pkg.characters import dragon
from a_game_pkg.battle import battle_player_turn
from a_game_pkg.battle import battle_enemy_turn
from a_game_pkg.battle import monster_defeat

def adventure_game():
    
    while True:
        """
        Main Game Loop:
        - first display title and initial prompt which allows user to quit program or play game;
        - If play game, user then selects a character from playable character options;
        - playable character selected determines user's stats for game session;
        - User then selects first enemy/monster to battle (gives user ability to experience game in different ways during different game sessions);
        - if enemy/monster already has been defeated during current game session, message displayed and user prompted to select a different enemy/monster to battle;
        - User plays until user's character defeated (hp reduced to 0 or below) or until all enemies/monsters defeated (each enemy's hp reduced to 0 or below);
        - when game ends for either above reason - User prompted to play again or quit program.
        """
        main_prompt = input(
            "\n--------------------------------\n ---- DEFEAT ALL MONSTERS! ---- \n--------------------------------\n\nTo quit game type 'quit' or 'q'\nTo Play Game type any key: "
        )
        if main_prompt.lower() == "q" or main_prompt.lower() == "quit":
            break
        else:
            # User has chosen to play game
            while True:
                # Loop for user to select a playable character from available options
                """
                Options for character traits user can select from
                """
                playable = {
                    "mage": {
                        "name": "Mage",
                        "hp": 175,
                        "damage_1": 25,
                        "damage_2": 80,
                        "potions": 2,
                    },
                    "warrior": {
                        "name": "Warrior",
                        "hp": 225,
                        "damage_1": 40,
                        "damage_2": 125,
                        "potions": 1,
                    },
                    "thief": {
                        "name": "Thief",
                        "hp": 180,
                        "damage_1": 25,
                        "damage_2": 85,
                        "potions": 2,
                    },
                }

                """ 
                Empty list where name of monster stored after user defeats it
                list checked each loop to prevent player from fighting same monster twice
                """
                completed_quests = []
                """
                User selects character and info displayed after selection: 
                """
                user = Player.user_select(player)
                if user == "1" or user.lower() == "mage":
                    player.name = playable["mage"]["name"]
                    player.hp += playable["mage"]["hp"]
                    player.damage_1 += playable["mage"]["damage_1"]
                    player.damage_2 += playable["mage"]["damage_2"]
                    player.potions += playable["mage"]["potions"]
                    break
                if user == "2" or user.lower() == "warrior":
                    player.name = playable["warrior"]["name"]
                    player.hp += playable["warrior"]["hp"]
                    player.damage_1 += playable["warrior"]["damage_1"]
                    player.damage_2 += playable["warrior"]["damage_2"]
                    player.potions += playable["warrior"]["potions"]
                    break
                if user == "3" or user.lower() == "thief":
                    player.name = playable["thief"]["name"]
                    player.hp += playable["thief"]["hp"]
                    player.damage_1 += playable["thief"]["damage_1"]
                    player.damage_2 += playable["thief"]["damage_2"]
                    player.potions += playable["thief"]["potions"]
                    break
                # Simple message printed if no character selected:
                print("\nUnknown/Invalid Character Selection...")
                # A print message displays the character info/stats for user's character after selection:
            Player.player_select_msg(player)

        while True:
            """
            User now selects an enemy/Monster to fight;
            - User and monster engage in turn-based battle;
            - battle ends when either user/monster HP reduced to 0 or below;
            - If user defeated: message displayed and user can quit game or play again;
            - If monster defeated: user character awarded stats boost and user prompted to select the next monster they want to battle;
            -- monster name added to 'completed_quests' list;
            -- completed_quests is checked each time to determine whether user battled given enemy in current game-session;
            -- user Wins when completed_quests contains the names of all monsters...
            - If user defeats all monsters in current game-session - Game is Won! - message displayed that user won and prompted to quit game or play again...
            """
            # Check to see if enemy in 'completed_quests'
            game_fin = check_list(completed_quests)
            if game_fin == True:
                Player.game_won_msg(player)
                break
            elif player.hp <= 0:
                Player.game_over_msg(player)
                break
            else:
                select_quest = Player.quest_select(player)
                if select_quest == "1" or select_quest.lower() == "goblin":
                    check = Enemy.check_if_defeated(goblin, completed_quests)
                    if check == True:
                        Player.already_defeated_msg(player, goblin)
                        continue
                    elif check == False:
                        completed_quests.append("goblin")
                        """ 
                        User Battles the Goblin: 
                        """
                        while True:
                            # player takes turn
                            battle_player_turn(goblin, player)
                            """ 
                            Check monster's HP before moving to Monster's turn; 
                            -- if monster HP <=0, user wins and is awarded stats boost;
                            -- else, monster's turn. 
                            """
                            if goblin.hp <= 0:
                                monster_defeat(player, goblin)
                                break
                            # If monster HP > 0; Monster attacks player:
                            battle_enemy_turn(goblin, player)

                            # Check to see if User's HP <= 0:
                            if player.hp <= 0:
                                Player.player_defeated_msg(player, goblin)
                                break

                if select_quest == "2" or select_quest.lower() == "ogre":
                    check = Enemy.check_if_defeated(ogre, completed_quests)
                    if check == True:
                        Player.already_defeated_msg(player, ogre)
                        continue
                    elif check == False:
                        completed_quests.append("ogre")
                        """ 
                        User Battles the Ogre 
                        """
                        while True:
                            # player takes turn
                            battle_player_turn(ogre, player)
                            """ 
                            Check monster's HP before moving to Monster's turn; 
                            -- if monster HP <=0, user wins and is awarded stats boost;
                            -- else, monster's turn. 
                            """
                            if ogre.hp <= 0:
                                monster_defeat(player, ogre)
                                break
                            # If monster HP > 0; Monster attacks player:
                            battle_enemy_turn(ogre, player)

                            # Check to see if User's HP <= 0:
                            if player.hp <= 0:
                                Player.player_defeated_msg(player, ogre)
                                break

                if select_quest == "3" or select_quest.lower() == "orc":
                    check = Enemy.check_if_defeated(orc, completed_quests)
                    if check == True:
                        Player.already_defeated_msg(player, orc)
                        continue
                    elif check == False:
                        completed_quests.append("orc")
                        """ 
                        User Battles the Orc
                        """
                        while True:
                            # player takes turn
                            battle_player_turn(orc, player)
                            """ 
                            Check monster's HP before moving to Monster's turn; 
                            -- if monster HP <=0, user wins and is awarded stats boost;
                            -- else, monster's turn. 
                            """
                            if orc.hp <= 0:
                                monster_defeat(player, orc)
                                break
                            # If monster HP > 0; Monster attacks player:
                            # monster_roll determines whether attack successful:
                            battle_enemy_turn(orc, player)

                            # Check to see if User's HP <= 0:
                            if player.hp <= 0:
                                Player.player_defeated_msg(player, orc)
                                break

                if select_quest == "4" or select_quest.lower() == "dragon":
                    check = Enemy.check_if_defeated(dragon, completed_quests)
                    if check == True:
                        Player.already_defeated_msg(player, dragon)
                        continue
                    elif check == False:
                        completed_quests.append("dragon")
                        """ 
                        User Battles the Dragon
                        """
                        while True:
                            # player takes turn
                            battle_player_turn(dragon, player)
                            """ 
                            Check monster's HP before moving to Monster's turn; 
                            -- if monster HP <=0, user wins and is awarded stats boost;
                            -- else, monster's turn. 
                            """
                            if dragon.hp <= 0:
                                monster_defeat(player, dragon)
                                break
                            # If monster HP > 0; Monster attacks player:
                            battle_enemy_turn(dragon, player)
                            # Check to see if User's HP <= 0:
                            if player.hp <= 0:
                                Player.player_defeated_msg(player, dragon)
                                break

if __name__ == "__main__":
    adventure_game()