class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        # Настройки корабля.
        self.ship_speed_factor = 2
