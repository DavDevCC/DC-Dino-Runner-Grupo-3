from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import COIN, COIN_TYPE


class Coin(PowerUp):
    def __init__(self):
        super().__init__(COIN, COIN_TYPE)