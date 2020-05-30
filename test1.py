import pygame
 
from constants import *
from loading import *
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

    # Set the height and width of the screen
    size = (SCREEN_WIDTH, SCREEN_HEIGHT,)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Idle1")

    screen.fill(BLACK)

    tasks = [TimedTask("Task {}".format(x/1), x) for x in range(1, 20, 1)]
    for i, task in enumerate(tasks):
        TaskGUI(task, x=0, y=50*i, width=400, height=50)

    active_sprite_list = [tasks]

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

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
