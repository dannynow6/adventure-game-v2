from a_game_pkg.characters import GameCharacter
from a_game_pkg.characters import Player
from a_game_pkg.characters import Enemy


def battle_player_turn(x, y):
    # x = monster, y = player
    # display enemy stats
    Enemy.monster_stats_msg(x)
    # Msg displayed to player each turn
    Player.player_turn_msg(y)
    # User selects action to perform
    player_turn = Player.user_turn(y)
    player_roll = GameCharacter.roll(y)
    if player_turn == "1" or player_turn.lower() == "basic":
        # User has selected basic attack:
        Player.basic_attack_msg(y)
        if player_roll > 3 and player_roll < 18:
            # Decrease Monster's HP by player damage_1
            x.hp = GameCharacter.successful_attack(x, y.damage_1)
            Player.player_basic_attack_msg(y, player_roll, x)
        else:
            # User does not land attack
            GameCharacter.failed_attack_msg(y)
    if player_turn == "2" or player_turn.lower() == "strong":
        # User has selected Strong attack:
        Player.strong_attack_msg(y)
        if player_roll >= 5 and player_roll < 10:
            # decrease Monster's HP by player damage_2
            x.hp = GameCharacter.successful_attack(x, y.damage_2)
            Player.player_strong_attack_msg(y, player_roll, x)
        else:
            # User does not land attack
            GameCharacter.failed_attack_msg(y)
    if player_turn == "3" or player_turn.lower() == "potion":
        # User opts to use a health potion:
        if y.potions > 0:
            # user has health potion remaining
            y.potions -= 1
            y.hp += 20
            Player.health_potion_msg(y)
        if y.potions <= 0:
            Player.no_potion_msg(y)


def battle_enemy_turn(x, y):
    # x = monster, y = player
    # If monster HP > 0; Monster attacks player:
    # monster_roll determines whether attack successful:
    monster_roll = GameCharacter.roll(x)

    if x.hp > x.choice:
        # monster's health at greater than 50%; monster uses basic attack:
        if monster_roll >= 4 and monster_roll < 18:
            # Monster lands successful basic attack:
            # User's HP reduced by attack damage:
            y.hp = GameCharacter.successful_attack(y, x.damage_1)
            Enemy.monster_basic_attack_msg(x, y)
        elif monster_roll < 4 or monster_roll >= 18:
            # Monster's attack misses:
            GameCharacter.failed_attack_msg(x)

    if x.hp <= x.choice:
        # Monster's total HP at 50% or less; strong attack possible:
        attack = Enemy.attack_choice(x)
        if attack == "basic":
            if monster_roll >= 4 and monster_roll < 18:
                # Monster lands successful basic attack:
                # User's HP reduced by attack damage:
                y.hp = GameCharacter.successful_attack(y, x.damage_1)
                Enemy.monster_basic_attack_msg(x, y)
            elif monster_roll < 4 or monster_roll >= 18:
                # Monster's attack misses:
                GameCharacter.failed_attack_msg(x)
        if attack == "strong":
            if monster_roll >= 5 and monster_roll < 10:
                # Monster lands successful strong attack:
                y.hp = GameCharacter.successful_attack(y, x.damage_2)
                Enemy.monster_strong_attack_msg(x, y)
            elif monster_roll < 5 or monster_roll >= 10:
                GameCharacter.failed_attack_msg(x)


def monster_defeat(p, m):
    # x = monster, y = player 
    Player.monster_defeated_msg(p, m) 
    # User's character awarded boost to stats
    p.hp = Player.hp_boost(p)
    p.damage_1 = Player.basic_boost(p)
    p.damage_2 = Player.strong_boost(p)
    # Display user's current stats:
    Player.stats_boost_msg(p)
        