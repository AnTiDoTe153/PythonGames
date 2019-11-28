from figures.figure import Figure
import math

class HealthBar(Figure):

    healthColor = (127,255,0)
    damageColor = (255,69,0)

    def __init__(self, target, health):
        width = target.width * 1.5
        height = target.height * 0.25
        
        pozY = target.pozY - (target.height / 2 + target.height * 0.3)
        pozX = target.pozX

        super().__init__(target.map, pozX, pozY, width, height, HealthBar.healthColor)

        self.maxHealth = health
        self.currentHealth = health
        self.damageBar = self.initDamageBar()

    def takeDamage(self, damage):
        self.currentHealth -= damage
        self.damageBar = self.initDamageBar()

    def initDamageBar(self):
        if self.currentHealth == self.maxHealth:
            damageBar = None
        else:
            damageWidth = math.ceil(((self.maxHealth - self.currentHealth) * self.width) / self.maxHealth)
            damagePoz = math.ceil(self.pozX + self.width / 2 - damageWidth / 2)
            damageBar = Figure(self.map, damagePoz, self.pozY, damageWidth, self.height, HealthBar.damageColor)
        return damageBar

    def draw(self):
        super().draw()
        if self.damageBar != None:
            self.damageBar.draw()
        
