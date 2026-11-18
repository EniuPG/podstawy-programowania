# Draws figures in different positions

import importlib.util
from pathlib import Path

import turtle

# The figures module is in the parent folder (04-Functions).
script_dir = Path(__file__).resolve().parent
figures_path = script_dir.parent / "figures.py"
if not figures_path.exists():
    figures_path = script_dir / "figures.py"

figures_spec = importlib.util.spec_from_file_location("figures", figures_path)
if figures_spec is None or figures_spec.loader is None:
    raise ImportError(f"Could not find the figures module at {figures_path}")
figures = importlib.util.module_from_spec(figures_spec)
figures_spec.loader.exec_module(figures)

window = turtle.Screen()

window.bgcolor("lightgreen")

figures.pen.penup()
figures.pen.goto(-200, 100)
figures.pen.pendown()
figures.draw_square(80)

figures.pen.penup()
figures.pen.goto(50, 100)
figures.pen.pendown()
figures.draw_square(80)

figures.pen.penup()
figures.pen.goto(-200, -50)
figures.pen.pendown()
figures.draw_triangle(100)

figures.pen.penup()
figures.pen.goto(50, -50)
figures.pen.pendown()
figures.draw_triangle(100)

figures.pen.penup()
figures.pen.goto(-200, -200)
figures.pen.pendown()
figures.draw_rectangle(120, 60)

figures.pen.penup()
figures.pen.goto(50, -200)
figures.pen.pendown()
figures.draw_rectangle(120, 60)

figures.pen.hideturtle()

window.mainloop()