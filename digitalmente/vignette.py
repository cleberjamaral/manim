from manimlib import *

# Based on AnimatingMethods(Scene) provided in the file example_scenes.py of manim library

class Vignette(Scene):
    def construct(self):
        grid = Text("01010101 01010101 01010101 01010101 digitalmente 01010101 01010101 01010101", font="Courier").get_grid(16, 1, height=3).set_height(TAU*1)
        self.add(grid)

        self.play(grid.animate.shift(LEFT*2).set_submobject_colors_by_gradient(BLUE, GREEN), run_time=1)
        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()
