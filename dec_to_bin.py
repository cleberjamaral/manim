from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class AnimatingMethodsBit(Scene):
    def construct(self):
        dec1 = Tex(r"1*100", r" + ", r"4*10", r" + ", r"7*1", r" = 147")
        self.play(Write(dec1))
        self.wait()
        self.play(dec1.animate.shift(UP))
        self.wait()

        dec2 = Tex(r"1*",r"10^2", r" + ", r"4*",r"10^1", r" + ", r"7*",r"10^0", r" = 147")
        self.play(Write(dec2))
        self.wait()
        self.play(
            dec1.animate.shift(UP),
            dec2.animate.shift(UP)
        )
        self.wait()

        dec3 = Tex(r"1~centena", r" + ", r"4~dezenas", r" + ", r"7~unidades", r" = 147")
        self.play(Write(dec3))
        self.play(
            dec3.animate.shift(ORIGIN)
        )
        self.wait()

        dec1.set_color_by_tex("1*100",RED)
        dec1.set_color_by_tex("4*10",BLUE)
        dec1.set_color_by_tex("7*1",GREEN)
        dec2.set_color_by_tex("1*",RED)
        dec2.set_color_by_tex("10^2",RED)
        dec2.set_color_by_tex("4*",BLUE)
        dec2.set_color_by_tex("10^1",BLUE)
        dec2.set_color_by_tex("7*",GREEN)
        dec2.set_color_by_tex("10^0",GREEN)
        dec3.set_color_by_tex("1~centena",RED)
        dec3.set_color_by_tex("4~dezenas",BLUE)
        dec3.set_color_by_tex("7~unidades",GREEN)
        self.wait()

        self.play(
            FadeOut(dec1),
            FadeOut(dec3),
            dec2.animate.shift(ORIGIN).scale(1.5)
        )
        self.wait()

        dec2.set_color_by_tex("1*",WHITE)
        dec2.set_color_by_tex("4*",WHITE)
        dec2.set_color_by_tex("7*",WHITE)
        self.wait()

