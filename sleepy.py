# import the pygame module, so you can use it
import pygame

def main():
    pygame.init()
    
    running = True
    
    volume = 0.5
    playing = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    if playing:
                        playing = False
                        pygame.mixer.music.fadeout(2000)
                    else:
                        playing = True
                        volume = 0.5
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.set_volume(volume)
                        pygame.mixer.music.play(-1, 10.0, 2000)
                elif event.key == pygame.K_KP0:
                    volume = 0.1
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP1:
                    volume = 0.2
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP2:
                    volume = 0.3
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP3:
                    volume = 0.4
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP4:
                    volume = 0.5
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP5:
                    volume = 0.6
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP6:
                    volume = 0.7
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP7:
                    volume = 0.8
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                        pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP8:
                    volume = 0.9
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP9:
                    volume = 1.0
                    if playing == False:
                        playing = True
                        pygame.mixer.music.load("HeavyRain.ogg")
                        pygame.mixer.music.play(-1, 10.0, 2000)
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP_PLUS:
                    volume += 0.01
                    if(volume > 1.0):
                        volume = 1.0
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_KP_MINUS:
                    volume -= 0.01
                    if(volume < 0.01):
                        volume = 0.01
                    pygame.mixer.music.set_volume(volume)
            elif event.type == pygame.QUIT:
                running = False
         
     
if __name__=="__main__":
    main()