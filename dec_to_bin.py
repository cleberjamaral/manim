from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class SemiBox(VGroup):
    CONFIG = {
        "stroke_color": YELLOW
    }

    def __init__(self, mobject, **kwargs):
        VGroup.__init__(self, **kwargs)

        hline = Line(start=[-0.2,0,0], end=[mobject.get_width(),0,0]).next_to(mobject, DOWN, buff=SMALL_BUFF)
        hline.set_stroke(self.stroke_color)
        #hline.set_width(hline.get_width() * 3)
        vline = Line(start=[0,-0.2,0], end=[0,mobject.get_height(),0]).next_to(mobject, LEFT, buff=SMALL_BUFF)
        vline.set_stroke(self.stroke_color)
        #vline.set_height(vline.get_height() * 2)
        self.add(hline, vline)

class DecimalSystem(Scene):
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

        rect1 = SurroundingRectangle(dec2[0], color = YELLOW)
        rect2 = SurroundingRectangle(dec2[3], color = YELLOW)
        rect3 = SurroundingRectangle(dec2[6], color = YELLOW)
        self.play(
            ShowCreation(rect1),
            ShowCreation(rect2),
            ShowCreation(rect3),
        )

        self.play(
            FadeOut(dec2[0]),
            FadeOut(dec2[3]),
            FadeOut(dec2[6]),
            FadeOut(dec2[8])
        )
        self.wait()


class DecToBin(Scene):

    def print_result(self, dividend, divisor, dd, dv, rlist):
        quotient = dividend // divisor
        remainder = dividend % divisor

        re = Tex(str(remainder)).next_to(dd, DOWN, buff=MED_SMALL_BUFF)
        rlist.append(re)
        qu = Tex(str(quotient)).next_to(dv, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(qu))
        self.play(Write(re))

        ndv = Tex(str(divisor)).next_to(qu, RIGHT, buff=MED_SMALL_BUFF)
        if quotient >= divisor:
            semi_box = SemiBox(ndv, color = YELLOW)
            self.play(ShowCreation(semi_box))
            self.play(Write(ndv))

        return quotient, qu, ndv

    def show_division(self, dividend, divisor):
        dd = Tex(str(dividend))
        self.play(Write(dd))
        self.play(dd.to_corner, UP+LEFT)
        dv = Tex(str(divisor)).next_to(dd, RIGHT, buff=MED_SMALL_BUFF)
        semi_box = SemiBox(dv, color = YELLOW)
        self.play(ShowCreation(semi_box))
        self.play(Write(dv))

        rlist = []
        quotient, qu, ndv = self.print_result(dividend, divisor, dd, dv, rlist)
        while quotient >= divisor:
            quotient, qu, ndv = self.print_result(quotient, divisor, qu, ndv, rlist);
        bin = qu.copy()

        rect = SurroundingRectangle(qu, color = PINK)
        self.play(ShowCreation(rect))
        clist = [bin]
        for r in reversed(rlist):
            rect = SurroundingRectangle(r, color = PINK)
            self.play(ShowCreation(rect))
            rem = r.copy()
            clist.append(rem)

        for c in clist:
            c.generate_target()
            if clist.index(c) == 0:
                c.target.move_to(ORIGIN)
            else:
                c.target.next_to(clist[clist.index(c)-1], RIGHT)
            c.set_height(2*c.get_height())
            self.play(
                MoveToTarget(c)
            )
            self.play(
                c.animate.scale(1.5)
            )

        amsb = Arrow(start=UP, end=DOWN, buff=SMALL_BUFF).next_to(clist[0], DOWN)
        msb = Tex(r"MSB").next_to(amsb, DOWN)
        tmsb = Tex(r"Most~Significant~Bit")
        tmsb.next_to(msb, DOWN)
        tmsb.scale(0.8)
        amsb.set_color(GREEN)
        msb.set_color(GREEN)
        tmsb.set_color(GREEN)
        self.play(
            ShowCreation(amsb),
            ShowCreation(msb),
            ShowCreation(tmsb),
            tmsb.animate.shift(LEFT)
        )

        alsb = Arrow(start=UP, end=DOWN, buff=SMALL_BUFF).next_to(clist[-1], DOWN)
        lsb = Tex(r"LSB").next_to(alsb, DOWN)
        tlsb = Tex(r"Least~Significant~Bit")
        tlsb.scale(0.8)
        tlsb.next_to(lsb, DOWN)
        alsb.set_color(BLUE)
        lsb.set_color(BLUE)
        tlsb.set_color(BLUE)
        self.play(
            ShowCreation(alsb),
            ShowCreation(lsb),
            ShowCreation(tlsb),
            tlsb.animate.shift(RIGHT*1.5)
        )

        for c in clist:
            c.save_state()
            self.play(
                c.animate.scale(((len(clist) - clist.index(c)) / len(clist)) * 2),
            )
        for c in clist:
            self.play(
                c.restore
            )

    def construct(self):
        self.show_division(47,2)

class ShowWords(Scene):
    def construct(self):
        words = VGroup(
            TexText("Machine", "learning").set_color(GREEN),
            TexText("Neural network").set_color(BLUE),
        )
        words[0].save_state()
        words[0].shift(DOWN)
        words[0].fade(1)

        self.wait()

        self.play(
            words[0].restore
        )

        self.wait()

        #self.play(
        #    words[0].shift,
        #    FadeIn(words[1]),
        #)

        self.play(words.to_corner, UP+RIGHT)

        self.words = words
        self.wait()
        #self.play(
        #    ReplacementTransform(
        #        VGroup(self.words[1].copy())
        #    ),
        #    run_time = 1
        #)

        equation = Tex(
            "\\textbf{a}_{l+1}", "=",
            "\\sigma(",
                "W_l", "\\textbf{a}_l", "+", "b_l",
            ")"
        )
        equation.set_color_by_tex_to_color_map({
            "\\textbf{a}" : GREEN,
        })
        equation.move_to(UP+LEFT)
        equation.to_edge(UP)

        self.play(Write(equation, run_time = 2))
        self.wait()

        self.equation = equation

        self.wait()

        word = self.words[0][1].copy()
        rect = SurroundingRectangle(word, color = YELLOW)

        word_group = VGroup(word, rect)
        word_group.generate_target()
        word_group.target.move_to(self.equation, LEFT)
        word_group.target[0].set_color(YELLOW)
        word_group.target[1].set_stroke(width = 0)

        self.play(ShowCreation(rect))
        self.play(
            FadeOut(self.equation),
            MoveToTarget(word_group),
        )
