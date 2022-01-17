import pygame
 
from constants import *
from Task import *
from TaskGUI import *
#import levels

#from player import Player

def update(stuff, time_since):
    if isinstance(stuff, list):
        for smaller_stuff in stuff:
            update(smaller_stuff, time_since)
    else:
        stuff.update(time_since)

def draw(stuff, screen):
    if isinstance(stuff, list):
        for smaller_stuff in stuff:
            draw(smaller_stuff, screen)
    else:
        stuff.draw(screen)

def main():
    """ Main Program """
    pygame.init()

    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT,)
    screen_caption = "Idle1"
    screen_color = BLACK

    screen = pygame.display.set_mode(screen_size)
    screen.fill(screen_color)
    pygame.display.set_caption(screen_caption)

    active_sprite_list = []

    # Test tasks
    tasks    = [TimedTask("{}".format(int(x/1)), x) for x in range(1, 10, 1)]
    taskguis = [TaskGUI(task, x=0, y=50*i, width=400, height=50) for i, task in enumerate(tasks)]
    taskpane = TaskGUIPane(taskguis, x=300, height=100)
    active_sprite_list.append(taskpane)

    # -------- Main Program Loop -----------
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


            elif event.type == pygame.MOUSEWHEEL:
                print(event)
                print(event.x, event.y)
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_LEFT:
#                    player.go_left()
#                if event.key == pygame.K_RIGHT:
#                    player.go_right()
#                if event.key == pygame.K_UP:
#                    player.jump()

#            if event.type == pygame.KEYUP:
#                if event.key == pygame.K_LEFT and player.change_x < 0:
#                    player.stop()
#                if event.key == pygame.K_RIGHT and player.change_x > 0:
#                    player.stop()

        # Update the player.
        update(active_sprite_list, clock.get_time())

        # Update items in the level
        #current_level.update()

        # If the player gets near the right side, shift the world left (-x)
#        if player.rect.right >= 500:
#            diff = player.rect.right - 500
#            player.rect.right = 500
#            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
#        if player.rect.left <= 120:
#            diff = 120 - player.rect.left
#            player.rect.left = 120
#            current_level.shift_world(diff)
#
#        # If the player gets to the end of the level, go to the next level
#        current_position = player.rect.x + current_level.world_shift
#        if current_position < current_level.level_limit:
#            player.rect.x = 120
#            if current_level_no < len(level_list)-1:
#                current_level_no += 1
#                current_level = level_list[current_level_no]
#                player.level = current_level

        ### DRAW ###
        draw(active_sprite_list, screen)
        #screen.blit(tasks[0].image, (0,0))
        #current_level.draw(screen)
        #active_sprite_list.draw(screen)
        ############

        # Limit to 60 frames per second
        clock.tick(60)

        # Update the screen
        pygame.display.flip()

    # IDLE friendly. Without this line, the program will 'hang' on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()
