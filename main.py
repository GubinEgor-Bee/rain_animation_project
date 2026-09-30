"""Точка входа в программу."""
import tkinter as tk
from src.app import App


def main() -> None:
    """Создает корневое окно и запускает приложение."""
    root = tk.Tk()
    app = App(root)
    app.update()
    root.mainloop()


if __name__ == "__main__":
    main()
