from figure import Figure

class HealthBar(Figure):

    healthColor = (127,255,0)

    def __init__(self, target, health):
        self.maxHealth = health

        width = target.width * 1.1
        height = target.height // 10
        
        pozY = target.pozY - (target.height // 2 + target.height * 0.2)
        pozX = target.pozX

        super().__init__(target.map, pozX, pozY, width, height, HealthBar.healthColor)


