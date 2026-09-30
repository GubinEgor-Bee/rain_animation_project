"""Модуль, содержащий главный цикл приложения и интерфейс."""

import tkinter as tk
from src.models.animation_model import Raindrop
from src.renderers.renderer import RainRenderer

class App:
    """Главный класс приложения, управляющий окном и анимацией."""

    def __init__(self, root: tk.Tk):
        """
        Инициализирует графический интерфейс и параметры анимации.

        Args:
            root (tk.Tk): Корневое окно tkinter.
        """
        self.root = root
        self.root.title("Анимация: Дождь")
        self.root.geometry("800x600")
        
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Слайдер для настройки плотности дождя (интерактивность)
        self.density_slider = tk.Scale(
            self.root, from_=1, to=20, orient=tk.HORIZONTAL,
            label="Плотность (капель в кадр)", bg="gray"
        )
        self.density_slider.set(5)
        self.density_slider.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.drops = []
        self.renderer = RainRenderer(self.canvas)
        self.is_running = True

    def update(self) -> None:
        """Главный цикл анимации. Обновляет логику и перерисовывает кадр."""
        if not self.is_running:
            return

        screen_width = self.canvas.winfo_width()
        screen_height = self.canvas.winfo_height()

        if screen_width > 1:  # Ждем, пока окно инициализируется
            # 1. Генерация новых капель в зависимости от значения слайдера
            density = self.density_slider.get()
            for _ in range(density):
                self.drops.append(Raindrop(screen_width, screen_height))
            
            # 2. Обновление координат капель и удаление тех, что упали
            for drop in self.drops[:]:
                drop.fall()
                if drop.is_off_screen():
                    self.drops.remove(drop)
            
            # 3. Отрисовка
            self.renderer.draw(self.drops)

        # Планирование следующего кадра (примерно 60 FPS)
        self.root.after(16, self.update)
