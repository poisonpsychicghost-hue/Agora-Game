#----Definitions-----

#----Startup Window-----
import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Theseus Kinda Sux Doesn't He?")

#----Bool Trackers------
running = True
z_pressed = False
x_pressed = False
menu_trig = False
menu_secret = False
have_clue_check = False

#------Int Trackers------
theseus_secret = 0
click_tracker = 0

#-----Fonts-------
choice_font = pygame.font.SysFont("Arial", 30)
screen_font = pygame.font.SysFont("Arial", 50)

#----Labels-------
z_button_label = "Z: Yes: Accept"
x_button_label = "X: No: Reject"
menu_main_label = "Menu: "
menu_sub_label = "made ya look ;)"
theseus_secret_label = "Hi! You Found Me!"

#------Sprites-------
theseus_sprite = pygame.image.load("Assets:Sprites/Theseus PlaceHolder-1.png.png")
theseus_sprite_big = pygame.transform.scale(theseus_sprite, (99, 99))

#----Static Backgrounds---
ai_placeholder_image = pygame.image.load("Assets:Sprites/Gemini_Generated_Image_uo4kdvuo4kdvuo4k.png")
ai_placeholder_image_fitted = pygame.transform.scale(ai_placeholder_image, (1020, 420))
##TODO: label and stretch all background scenes with appropriate names
back_intro_bard_scene = pygame.image.load("Assets:Sprites/Intro_Bard_Scene.png")
back_intro_bard_scene_fitted = pygame.transform.scale(back_intro_bard_scene, (1020, 420))
back_athens_assembly_1 = pygame.image.load("Assets:Sprites/Athens_Assembly_1.png")
back_athens_assembly_1_fitted = pygame.transform.scale(back_athens_assembly_1, (1020, 420))
back_athens_assembly_2 = pygame.image.load("Assets:Sprites/Athens_Assembly_2.png")
back_athens_assembly_2_fitted = pygame.transform.scale(back_athens_assembly_2, (1020, 420))
back_athens_docks = pygame.image.load("Assets:Sprites/Athens_Docks.png")
back_athens_docks_fitted = pygame.transform.scale(back_athens_docks, (1020, 420))
back_crete_docks_1 = pygame.image.load("Assets:Sprites/Crete_Docks_1.png")
back_crete_docks_fitted = pygame.transform.scale(back_crete_docks_1, (1020, 420))
back_crete_docks_2 = pygame.image.load("Assets:Sprites/Crete_Docks_2.png")
back_crete_docks_2_fitted = pygame.transform.scale(back_crete_docks_2, (1020, 420))

back_labyrinth_good_1 = pygame.image.load("Assets:Sprites/Labyrinth_Good_1.png")
back_labyrinth_good_1_fitted = pygame.transform.scale(back_labyrinth_good_1, (1020, 420))
back_labyrinth_good_2 = pygame.image.load("Assets:Sprites/Labyrinth_Good_2.png")
back_labyrinth_good_2_fitted = pygame.transform.scale(back_labyrinth_good_2, (1020, 420))
back_labyrinth_good_3 = pygame.image.load("Assets:Sprites/Labyrinth_Good_3.png")
back_labyrinth_good_3_fitted = pygame.transform.scale(back_labyrinth_good_3, (1020, 420))
back_labyrinth_good_ariadne = pygame.image.load("Assets:Sprites/Labyrinth_Good_Ariadne.png")
back_labyrinth_good_ariadne_fitted = pygame.transform.scale(back_labyrinth_good_ariadne, (1020, 420))
back_athens_blk_sail_1 = pygame.image.load("Assets:Sprites/Athens_Black_Sails_1.png")
back_athens_blk_sail_1_fitted = pygame.transform.scale(back_athens_blk_sail_1, (1020, 420))
back_athens_blk_sail_2 = pygame.image.load("Assets:Sprites/Athens_Black_Sails_2.png")
back_athens_blk_sail_2_fitted = pygame.transform.scale(back_athens_blk_sail_2, (1020, 420))
back_athens_blk_sail_3 = pygame.image.load( "Assets:Sprites/Athens_Black_Sails_3.png")
back_athens_blk_sail_3_fitted = pygame.transform.scale(back_athens_blk_sail_3, (1020, 420))

back_labyrinth_bad_1 = pygame.image.load("Assets:Sprites/Labyrinth_Bad_1.png")
back_labyrinth_bad_1_fitted = pygame.transform.scale(back_labyrinth_bad_1, (1020, 420))
back_labyrinth_bad_2 = pygame.image.load("Assets:Sprites/Labyrinth_Bad_2.png")
back_labyrinth_bad_2_fitted = pygame.transform.scale(back_labyrinth_bad_2, (1020, 420))
back_labyrinth_bad_3 = pygame.image.load("Assets:Sprites/Labyrinth_Bad_3.png")
back_labyrinth_bad_3_fitted = pygame.transform.scale(back_labyrinth_bad_3, (1020, 420))
back_labyrinth_bad_minotaur = pygame.image.load("Assets:Sprites/Labyrinth_Bad_Minotaur.png")
back_labyrinth_bad_minotaur_fitted = pygame.transform.scale(back_labyrinth_bad_minotaur, (1020, 420))
back_death_screen = pygame.image.load("Assets:Sprites/Death_Screen.png")
back_death_screen_fitted = pygame.transform.scale(back_death_screen, (1020, 420))


#----Text Box Frames----
##TODO: Generate some retro ancient greek text boxes as jpgs 1 generic, 1 per main npc
##TODO: label and stretch to fit all text needs. Leave ToDo here until all text tested

#--------Scene Texts---------

#--------Scenes-------------
Intro_Bard_Scene = 0
Athens_Assembly_1 = 1
Athens_Assembly_2 = 2
Athens_Docks = 3
Crete_Docks_1 = 4
Crete_Docks_2 = 5
#--Split Good
Labyrinth_Good_1 = 6
Labyrinth_Good_2 = 7
Labyrinth_Good_3 = 8
Labyrinth_Good_Ariadne = 9
Crete_Es_Ca_Pay = 10
Athens_Black_Sails_1 = 11
Athens_Black_Sails_2 = 12
Athens_Black_Sails_3 = 13
#Split Bad
Labyrinth_Bad_1 = 14
Labyrinth_Bad_2 = 15
Labyrinth_Bad_3 = 16
Labyrinth_Bad_Minotaur = 17
Death_Screen = 18
#Menuing Scenes
Menu_Scene = 19
Game_Startup_Scene = 20
Credits_Scene = 21


#---Main Program-----
while running:
        #Main Background
    screen.fill((50, 55, 45))

        #Main Screen
    pygame.draw.rect(screen, (25, 25, 25), (60, 60, 1080, 480))

        #Main Buttons Screen
    pygame.draw.rect(screen, (76, 76, 76), (60, 480, 1080, 100))
    pygame.draw.rect(screen, (25, 25, 25), (62, 482, 1078, 98))
    #left 'Z' button
    pygame.draw.rect(screen, (76, 76, 76), (63, 484, 538, 96))
    #right 'X' button
    pygame.draw.rect(screen, (72, 72, 72), (604, 484, 537, 96))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            elif event.key == pygame.K_z:
                #Main Accept key input
                z_pressed = True
                theseus_secret += 1
                click_tracker += 1

            elif event.key == pygame.K_x:
                #Main Decline key input
                x_pressed = True
                theseus_secret += 1

            elif event.key == pygame.K_SPACE:
                #Menu Trigger on/off
                menu_secret = True
                if menu_trig:
                    menu_trig = False
                else:
                    menu_trig = True

            else:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                #Main Accept key input up
                z_pressed = False

            elif event.key == pygame.K_x:
                #Main Decline key input up
                x_pressed = False

            elif event.key == pygame.K_SPACE:
                menu_secret = False

    z_button_label_rend = choice_font.render(z_button_label, True, (0, 0, 0))
    screen.blit(z_button_label_rend, (215, 505))

    x_button_label_rend = choice_font.render(x_button_label, True, (0, 0, 0))
    screen.blit(x_button_label_rend, (758, 505))

    if z_pressed:
        pygame.draw.rect(screen, (80, 80, 80), (60, 482, 543, 98))
        z_button_label_rend = choice_font.render(z_button_label, True, (24, 250, 80))
        screen.blit(z_button_label_rend, (215, 505))

    if x_pressed:
        pygame.draw.rect(screen, (69, 69, 69), (603, 482, 537, 98))
        x_button_label_rend = choice_font.render(x_button_label, True, (224, 60, 80))
        screen.blit(x_button_label_rend, (758, 505))

    if menu_trig:
        screen.fill((150, 155, 145))
        pygame.draw.rect(screen, (76, 76, 76), (60, 20, 1080, 150))

        menu_main_label_rend = screen_font.render(menu_main_label, True, (0, 0, 0))
        screen.blit(menu_main_label_rend, (525, 35))

        menu_sub_label_rend = choice_font.render(menu_sub_label, True, (0, 0, 0))
        if menu_secret:
            pygame.draw.rect(screen, (25, 26, 26), (482, 84, 222, 37))
            pygame.draw.rect(screen, (185, 206, 76), (485, 87, 216, 31))
            pygame.draw.rect(screen, (185, 46, 66), (495, 93, 196, 20))
            pygame.draw.rect(screen, (15, 196, 96), (500, 99, 186, 9))
            screen.blit(menu_sub_label_rend, (490, 85))

    if theseus_secret >= 9:
        theseus_secret_label_rend = choice_font.render(theseus_secret_label, True, (0, 0, 0))
        screen.blit(theseus_sprite_big, (250, 250))
        screen.blit(theseus_secret_label_rend, (250, 270))







    pygame.display.flip()


pygame.quit()