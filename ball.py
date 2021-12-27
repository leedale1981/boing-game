from pgzero.builtins import Actor

from boing import HALF_WIDTH


class Ball(Actor):
    def __init__(self, dx):
        super().__init__("ball", (0, 0))

    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y += self.dy

            if abs(self.x - HALF_WIDTH) >= 344 and abs(original_x - HALF_WIDTH) < 344:
                if self.x < HALF_WIDTH:
                    new_dir_x = 1
                    bat = game.bats[0]
                else
                new_dir_x = -1
                bat = game.bats[1]
