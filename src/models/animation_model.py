"""Модуль, содержащий математическую модель капли дождя."""

import random


class Raindrop:
    """Класс, описывающий отдельную каплю дождя с учетом перспективы (3D)."""

    def __init__(self, screen_width: int, screen_height: int):
        """
        Инициализирует каплю дождя.

        Args:
            screen_width (int): Ширина экрана для случайной генерации по X.
            screen_height (int): Высота экрана.
        """
        self.screen_height = screen_height
        self.x = random.randint(0, screen_width)
        self.y = random.randint(-50, screen_height)

        # Z-ось для 3D-эффекта (от 1 до 20).
        # Чем больше Z, тем дальше капля.
        self.z = random.randint(1, 20)

        # Вычисление параметров на основе дальности (Z)
        # Близкие капли (z маленькое) падают быстрее и имеют больший размер
        self.speed_y = (20 / self.z) + random.uniform(2, 5)
        self.length = (30 / self.z) + 10
        self.width = max(1, int(4 / self.z))

    def fall(self) -> None:
        """Обновляет координату Y капли, имитируя падение."""
        self.y += self.speed_y

    def is_off_screen(self) -> bool:
        """
        Проверяет, улетела ли капля за пределы экрана.

        Returns:
            bool: True, если капля за экраном, иначе False.
        """
        return self.y > self.screen_height
