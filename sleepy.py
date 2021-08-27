# import the pygame module, so you can use it
import pygame
import yaml
config = yaml.safe_load(open("config.yml"))
version = "0.2.12"

print("Sleepy Speaker V"+version);
print("Loaded config");
print("Default volume: "+str(config["default_volume"]));
print("Resume last volume: "+str(config["resume_last_volume"]));

volume = config["default_volume"]
playing = False

def play():
    pygame.mixer.music.load("HeavyRain.ogg")
    pygame.mixer.music.play(-1, 10.0, 2000)

def stop():
    playing = False
    pygame.mixer.music.fadeout(2000)
    

def set_volume(vol):
    if(vol < 0.0):
        vol = 0.0
    if(vol > 1.0):
        vol = 1.0
    volume = vol
    pygame.mixer.music.set_volume(vol)
    
def play_at_volume(vol):
    if not playing:
        playing = True
        play()
    set_volume(vol)


def main():
    pygame.init()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    if playing:
                        stop()
                    else:
                        if config["resume_last_volume"]:
                            play_at_volume(volume)
                        else:
                            play_at_volume(config["default_volume"])
                elif event.key == pygame.K_KP0:
                    play_at_volume(0.1)
                elif event.key == pygame.K_KP1:
                    play_at_volume(0.2)
                elif event.key == pygame.K_KP2:
                    play_at_volume(0.3)
                elif event.key == pygame.K_KP3:
                    play_at_volume(0.4)
                elif event.key == pygame.K_KP4:
                    play_at_volume(0.5)
                elif event.key == pygame.K_KP5:
                    play_at_volume(0.6)
                elif event.key == pygame.K_KP6:
                    play_at_volume(0.7)
                elif event.key == pygame.K_KP7:
                    play_at_volume(0.8)
                elif event.key == pygame.K_KP8:
                    play_at_volume(0.9)
                elif event.key == pygame.K_KP9:
                    play_at_volume(1.0)
                elif event.key == pygame.K_KP_PLUS:
                    set_volume(volume + 0.01)
                elif event.key == pygame.K_KP_MINUS:
                    set_volume(volume - 0.01)
            elif event.type == pygame.QUIT:
                running = False
         
     
if __name__=="__main__":
    main()