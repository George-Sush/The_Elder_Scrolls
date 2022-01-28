from player import Player
import os
import pygame
from sprite_objects import Sprites
from ray_casting import ray_casting_walls
from drawing import Drawing
import settings
import computer_settings
from interaction import Interaction
from settings import TILE, HALF_FOV, NUM_RAYS, math, PROJ_COEFF, DELTA_ANGLE, CENTER_RAY, HEIGHT, \
    TEXTURE_SCALE, SCALE, TEXTURE_HEIGHT, HALF_WIDTH, HALF_HEIGHT, WIDTH, HEIGHT, MAP_RES


if os.path.isfile('data.txt'):
    os.remove('data.txt')
computer_settings.hide_taskbar()
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()

sc_map = pygame.Surface(MAP_RES)
sprites = Sprites()
player = Player(sprites)
drawing = Drawing(sc, sc_map, player, clock)
interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
interaction.play_music()


while True:
    if settings.STATUS == settings.STATUS_PLAY:
        player.movement()
        drawing.background()
        walls, wall_shot = ray_casting_walls(player, drawing.textures)
        drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
        drawing.fps(clock)
        drawing.Hit_points()
        drawing.mini_map()
        drawing.player_weapon([wall_shot, sprites.sprite_shot])

        drawing.dialog()

        interaction.interaction_objects()
        interaction.npc_action()
        interaction.clear_world()
        interaction.check_is_dialog_was_play()

        interaction.check_loss()
        if interaction.check_win():
            sprites.END()

        pygame.display.flip()
        settings.DELTA_MS = clock.tick()
    elif settings.STATUS == settings.STATUS_LOSE:
        pygame.mouse.set_visible(True)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            computer_settings.unhide_taskbar()
            print("да")
            exit()
        if keys[pygame.K_SPACE]:
            if os.path.isfile('data.txt'):
                os.remove('data.txt')
            settings.STATUS = settings.STATUS_PLAY
            settings.HP[0] = 100
            settings.NEED_TO_GO[0] = False
            settings.END_BOSS[0] = False

            # sc_map = pygame.Surface(MAP_RES)
            sprites = Sprites()
            player = Player(sprites)
            drawing = Drawing(sc, sc_map, player, clock)
            interaction = Interaction(player, sprites, drawing)

            drawing.menu()
            pygame.mouse.set_visible(False)
            interaction.play_music()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                computer_settings.unhide_taskbar()
                print("да")
                exit()
        drawing.loss()
    elif settings.STATUS == settings.STATUS_WIN:
        pygame.mouse.set_visible(True)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            computer_settings.unhide_taskbar()
            print("да")
            exit()
        if keys[pygame.K_SPACE]:
            if os.path.isfile('data.txt'):
                os.remove('data.txt')
            settings.STATUS = settings.STATUS_PLAY
            settings.HP[0] = 100
            settings.NEED_TO_GO[0] = False
            settings.END_BOSS[0] = False

            # sc_map = pygame.Surface(MAP_RES)
            sprites = Sprites()
            player = Player(sprites)
            drawing = Drawing(sc, sc_map, player, clock)
            interaction = Interaction(player, sprites, drawing)

            drawing.menu()
            pygame.mouse.set_visible(False)
            interaction.play_music()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                computer_settings.unhide_taskbar()
                print("да")
                exit()
        drawing.win()
