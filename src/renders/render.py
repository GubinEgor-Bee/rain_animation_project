"""Модуль для отрисовки графических объектов на холсте."""

import tkinter as tk

class RainRenderer:
    """Класс, отвечающий за отрисовку капель дождя на холсте."""

    def __init__(self, canvas: tk.Canvas):
        """
        Инициализирует рендерер.

        Args:
            canvas (tk.Canvas): Холст tkinter, на котором происходит рисование.
        """
        self.canvas = canvas

    def draw(self, drops: list) -> None:
        """
        Отрисовывает список капель и очищает предыдущие кадры.

        Args:
            drops (list): Список объектов Raindrop.
        """
        # Очистка холста перед новым кадром
        self.canvas.delete("all")
        
        for drop in drops:
            # Цвет зависит от дальности (Z): дальние капли темнее
            color_intensity = max(50, 255 - (drop.z * 10))
            color_hex = f"#{color_intensity:02x}{color_intensity:02x}ff" # Оттенки синего
            
            # Рисование линии (капли)
            self.canvas.create_line(
                drop.x, drop.y, 
                drop.x, drop.y + drop.length, 
                fill=color_hex, 
                width=drop.width
            )
