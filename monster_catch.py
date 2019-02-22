import pygame

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    # background = background("background.png")
    

    

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        
        class Background(pygame.sprite.Sprite):
            def __init__(self, image_file, location):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(image_file)
                self.rect = self.image.get_rect()
                self.rect.left, self.rect.top = location

        BackGround = Background('background.png', [0,0])
        screen.blit(BackGround.image, BackGround.rect)
            
              


        # Game display
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

print(polly)