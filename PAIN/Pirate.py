import pygame


class Pirate(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.treasure_chest = []
        self.HP = 10
        self.power_up = False

    def throw_bottle(self):
        # find nearest ninja and do throw bottle animation toward ninja
        # ninja dies
        return

    def check_powerup(self):
        return self.power_up
    # is this one necessary?