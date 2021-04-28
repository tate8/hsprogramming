from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from Wall import Wall
from HealthBar import HealthBar
from BloodSplatter import BloodSplatter
import time

# ------Create Objects for classes-------
player_1 = Player()
hbar = HealthBar()
blood = None



# enemy list and storage
enemies = []
walls = []
enemy_skins = []
bloods = []
blood_effects = []


def setup():
    size(1000, 600)
    imageMode(CENTER)
    global p, map_1, font, blood_1, show_blood, start_screen, play
    show_blood = False
    play = False
    p = loadImage('survivor.png')
    map_1 = loadImage('map.png')
    font = loadFont('Dialog-40.vlw')
    # zombies
    enemy_1 = loadImage('enemy_1.png')
    enemy_skins.append(enemy_1)
    enemy_2 = loadImage('enemy_2.png')
    enemy_skins.append(enemy_2)
    enemy_3 = loadImage('enemy_3.png')
    enemy_skins.append(enemy_3)
    enemy_4 = loadImage('enemy_4.png')
    enemy_skins.append(enemy_4)
    enemy_5 = loadImage('enemy_5.png')
    enemy_skins.append(enemy_5)
    # bloods
    blood_1 = loadImage('blood_1.png')
    blood_effects.append(blood_1)
    blood_2 = loadImage('blood_2.png')
    blood_effects.append(blood_2)
    blood_3 = loadImage('blood_3.png')
    blood_effects.append(blood_3)
    blood_4 = loadImage('blood_4.png')
    blood_effects.append(blood_4)
    blood_5 = loadImage('blood_5.png')
    blood_effects.append(blood_5)
    # start screen
    start_screen = loadImage('start_screen.png')

    
    
# def time_decorator(func):
#     def wrapper():
#         old_time = time.time()
#         func()
#         new_time = time.time()
#         time = old_time-new_time
#         print(time)
#         return func
#     return wrapper

# @time_decorator
def draw():
    global map_1, start_screen
    if play == False:
        background(start_screen)
    else:
        background(map_1)
        #display blood first so other stuff is on top
        display_blood(blood)
    
        # spawn enemy
        # LEVEL LOGIC
        if player_1.kill_count % 5 == 0:
            player_1.level += 1
            player_1.kill_count += 1
        if len(enemies) < player_1.level:
            t_or_b = random(0, 2)
            if t_or_b < 1:
                x = random(400, 1000)
                y = -30
                index = random(5)
                random_skin = enemy_skins[int(index)]
                enemy = Enemy(x, y, random_skin, int(index))
                enemies.append(enemy)
            if t_or_b > 1:
                x = random(0, 1000)
                y = 630
                index = random(5)
                random_skin = enemy_skins[int(index)]
                enemy = Enemy(x, y, random_skin, int(index))
                enemies.append(enemy)
        if player_1.kill_count %5 == 0 and player_1.can_increase_level == True:
            player_1.level += 1
            player_1.can_increase_level = False
    
        
        
        # -------------PLAYER vs. WALLS--------------
        # 1st
        w1 = Wall(0, 0, 390, 190, player_1.x, player_1.y, player_1.x_speed, player_1.y_speed)
        walls.append(w1)
        w1.display()
        if w1.collision_detection_y():
            player_1.y += 3
        if w1.collision_detection_x():
            player_1.x += 3
        
        # 2nd (below car)
        w2 = Wall(690, 240, 310, 5, player_1.x, player_1.y, player_1.x_speed, player_1.y_speed)
        walls.append(w2)
        w2.display()
        if w2.collision_detection_y() and player_1.key_up == True:
            player_1.y += 3
        elif w2.collision_detection_y() and player_1.key_down == True:
            player_1.y -= 3
        elif w2.collision_detection_y():
            player_1.y_speed *= -1
        if w2.collision_detection_x():
            player_1.x -= 3
            
        # 3rd (above road(most right)
        w3 = Wall(690, 473, 310, 5, player_1.x, player_1.y, player_1.x_speed, player_1.y_speed)
        walls.append(w3)
        w3.display()
        if w3.collision_detection_y() and player_1.key_up == True:
            player_1.y += 3
        elif w3.collision_detection_y() and player_1.key_down == True:
            player_1.y -= 3
        elif w3.collision_detection_y():
            player_1.y_speed *= -1
        if w3.collision_detection_x():
            player_1.x -= 3
        
            # 4th (vertical)
        w4 = Wall(522, 250, 5, 230, player_1.x, player_1.y, player_1.x_speed, player_1.y_speed)
        walls.append(w4)
        w4.display()
        if w4.collision_detection_y() and player_1.key_up == True:
            player_1.y += 3
        elif w4.collision_detection_y() and player_1.key_down == True:
            player_1.y -= 3
        elif w4.collision_detection_y():
            player_1.y_speed *= -1
        if w4.collision_detection_x() and player_1.key_left == True:
            player_1.x += 3
        elif w4.collision_detection_x() and player_1.key_right == True:
            player_1.x -= 3
        elif  w4.collision_detection_x():
            player_1.x_speed *= -1
            
        # 5th (below blue bench)
        w5 = Wall(530, 240, 100, 5, player_1.x, player_1.y, player_1.x_speed, player_1.y_speed)
        walls.append(w5)
        w5.display()
        if w5.collision_detection_y() and player_1.key_up == True:
            player_1.y += 3
        elif w5.collision_detection_y() and player_1.key_down == True:
            player_1.y -= 3
        elif w5.collision_detection_y():
            player_1.y_speed *= -1
        if w5.collision_detection_x():
            player_1.x -= 3
            
        # 6th (below 5)
        w6 = Wall(520, 473, 120, 5, player_1.x, player_1.y, player_1.x_speed, player_1.y_speed)
        walls.append(w6)
        w6.display()
        if w6.collision_detection_y() and player_1.key_up == True:
            player_1.y += 3
        elif w6.collision_detection_y() and player_1.key_down == True:
            player_1.y -= 3
        elif w6.collision_detection_y():
            player_1.y_speed *= -1
        if w6.collision_detection_x():
            player_1.x -= 3
            
        # -------------BULLET vs. WALLS--------------
        for wall in walls:
            for bullet in player_1.bullets:
                pass
    
        
        # ------------PLAYER STUFF -------------
        # movement
        #display with image: p
        player_1.display(p)
        player_1.count_speed()
        player_1.change_pos()
        # some drag so u don't fall of screen
        player_1.x_speed *= 0.9
        player_1.y_speed *= 0.9
        
        # if reload button pressed: give cooldown
        if player_1.pressed_r:
            player_1.cool_down()
        
    
    
            
        # ------------COLISION DETECTION -------------
        # player vs. edge 
        # x
        if player_1.x < 20:
            player_1.x_speed += 3
        if player_1.x > 970:
            player_1.x_speed -= 3
        # y
        if player_1.y < 20:
            player_1.y_speed += 3
        if player_1.y > 570:
            player_1.y_speed -= 3
        
        
        # player vs. enemy
        for enemy in enemies:
            if dist(player_1.x, player_1.y, enemy.x, enemy.y) < 30:
                if player_1.health < 0:
                    noLoop()
                    print('gg')
                else:
                    player_1.health -= enemy.damage
                    player_1.score -= 10
                    # TODO: get thrown in random direction
                    print('you got thrown')
                    enemies.remove(enemy)
    
            
            
        
        #bullet vs enemy
        for enemy in enemies:
            for bullet in player_1.bullets:
                if enemy.bullet_intersection(bullet):
                    player_1.bullets.remove(bullet)
                    enemy.health -= 20
                    if enemy.health <= 0:
                        
                        # show blood
                        global blood_1, show_blood, blood
                        show_blood = True
                        # make blood splatter at enemy pos and angle
                        index = random(4)
                        selected_blood_effect = blood_effects[int(index)]
                        blood = BloodSplatter(selected_blood_effect, enemy.x, enemy.y, enemy.angle)
                        #add blood to list so u can have multiple
                        bloods.append(blood)
                        enemies.remove(enemy)
    
                        
                        player_1.score += 50
                        player_1.kill_count += 1
                        print('enemy defeated')
                # bullet vs edge of screen      
                if bullet.reached_an_edge():
                    player_1.bullets.remove(bullet)
        info_panel()
                
    
    # ------------ENEMY STUFF -------------
    for enemy in enemies:
        enemy.display(player_1.x, player_1.y)
        

    if mousePressed and player_1.can_shoot == True:
        if player_1.bullets_left > 0:
            if frameCount % 4 == 1:
                player_1.shoot()
                player_1.bullets_left -= 1
    if player_1.bullets_left >= 0:
        player_1.can_shoot == False
        player_1.count_down()

            
            
def display_blood(blood):
    for blood in bloods:
        if blood == None:
            pass
        global show_blood
        if show_blood:
            blood.display()

    
def info_panel():
    global font, hbar
    hbar.display(10,10, 370, 15, player_1.health)
    textFont(font)
    fill(0)
    textSize(20)
    text('Score: %s' %player_1.score , 10, 55)
    text('Enemies defeated: %i' %int(player_1.kill_count-player_1.level) , 10, 80)
    text('Level: %s' %player_1.level , 10, 105)
    text('Bullets: %s/60' %player_1.bullets_left , 10, 130)








#mouse clicked to start game
def mouseClicked():
    global play
    play = True

# keys
def keyPressed():
    if key == 'w':
        player_1.key_up = True
    
    if key == 's':
        player_1.key_down = True
    
    if key == 'a':
        player_1.key_left = True
      
    if key == 'd':
        player_1.key_right = True
    
    if key == 'r':
        if player_1.pressed_r == True:
            pass
        player_1.key_r = True
        player_1.pressed_r = True
        

def keyReleased():
    if key == 'w':
        player_1.key_up = False
    
    if key == 's':
        player_1.key_down = False
    
    if key == 'a':
        player_1.key_left = False
    
    if key == 'd':
        player_1.key_right = False
        
    if key == 'r':
        player_1.key_r = False
