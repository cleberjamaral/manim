from manim import *
import numpy as np

config.pixel_height = 1080
config.pixel_width = 1080

scale_div = 1.8
scale_bin = 3.0
numbers = [9, 67, 98, 350]

class SemiBox(VGroup):
    def __init__(self, mobject, **kwargs):
        VGroup.__init__(self, **kwargs)
        vline = Line(start=[0,mobject.get_height(),0], end=[0,-0.2,0]).next_to(mobject, LEFT, buff=SMALL_BUFF)
        vline.set_stroke(YELLOW)
        hline = Line(start=[-0.2,0,0], end=[mobject.get_width()*2,0,0]).next_to(vline, DOWN*0.05+RIGHT*0.01)
        hline.set_stroke(YELLOW)
        self.add(vline, hline)


class NumericalSystems(Scene):
    def construct(self):
        target_amount = 1000.00
        currency = Tex(r"R\$")
        amount = DecimalNumber(0.00)
        amount.next_to(currency,RIGHT)
        money = VGroup(currency, amount)
        money.move_to(UP*4+LEFT*2)
        money.scale(5)

        # https://commons.wikimedia.org/wiki/File:Speedometer_(CoreUI_Icons_v1.0.0).svg
        speedometer = SVGMobject("assets/Speedometer_(CoreUI_Icons_v1.0.0).svg")
        speedometer.scale(1.8).move_to(LEFT*5+DOWN*4)

        #Image created by Edward Boatman. Changed color and fill. Available at https://commons.wikimedia.org/wiki/File:Edward_Boatman_scale.svg
        scale = SVGMobject("assets/Edward_Boatman_scale.svg")
        scale.scale(1.8).move_to(UP*0.6)
        self.play(
            Create(money),
            run_time=0.1
        )
        self.play(
            ChangeDecimalToValue(amount, target_amount),
            Rotate(scale, TAU / 8),
            speedometer.animate.shift(RIGHT*10),
            run_time=2
        )
        self.wait()
        self.play(
            FadeOut(money),
            FadeOut(scale),
            FadeOut(speedometer),
            run_time=0.4
        )

        # https://commons.wikimedia.org/wiki/File:AnalogClockAnimation2_still_frame.svg
        clock = SVGMobject("assets/AnalogClockAnimation2_still_frame.svg")
        clock.scale(4).move_to(UP)

        self.play(
            Create(clock),
            run_time=3
        )
        self.play(
            FadeOut(clock),
            run_time=0.4
        )

        grid = VGroup(*[
            Text("010101010101010101010101010101010101010101010101010101010101010101\n101010101010101010101010101010101010101010101010101010101010101010", font="Courier").set_height(TAU*0.1).move_to(DOWN*i*0.8)
            for i in range(1,21)
        ]).move_to(UP*20)

        self.play(
            grid.animate.shift(DOWN*20),
            run_time=3
        )
        self.play(
            FadeOut(grid),
            run_time=0.4
        )

class DecToBin(Scene):
    def construct(self):
        self.intro()
        self.write_steps(numbers[0],2,0.5)
        self.write_steps(numbers[1],2,0.2)
        self.write_steps(numbers[2],2,0.1)
        self.write_steps(numbers[3],2,0.1)

    def intro(self):
        examples = []
        for n in numbers:
            if len(examples) == 0:
                example = Tex(f"${n:d}$", "~=~", f"0b${n:b}$").scale(3).move_to(UP*4)
                example[0].set_color(YELLOW)
                example[2].set_color(BLUE)
                examples.append(example)
            else:
                example = Tex(f"${n:d}$", "~=~", f"0b${n:b}$").scale(3).next_to(examples[-1], DOWN, buff=LARGE_BUFF)
                example[0].set_color(YELLOW)
                example[2].set_color(BLUE)
                examples.append(example)

        self.play(Write(VGroup(*examples)))
        self.wait()
        self.clear()

    def print_result(self, dividend, divisor, dd, dv, rlist, rt):
        quotient = dividend // divisor
        remainder = dividend % divisor

        re = Tex(str(remainder)).next_to(dd, DOWN, buff=MED_LARGE_BUFF).scale(scale_div)
        rlist.append(re)
        qu = Tex(str(quotient)).next_to(dv, DOWN + RIGHT*0.1, buff=MED_LARGE_BUFF).scale(scale_div)
        self.play(Write(qu), run_time=rt)
        self.play(Write(re), run_time=rt)

        ndv = Tex(str(divisor)).next_to(qu, RIGHT, buff=MED_LARGE_BUFF).scale(scale_div)
        if quotient >= divisor:
            semi_box = SemiBox(ndv, color = YELLOW)
            self.play(Create(semi_box, run_time=rt))
            self.play(Write(ndv), run_time=rt)

        return quotient, qu, ndv

    def dec_digits(self, number):
        if (number > 10):
            return self.dec_digits(number // 10) + 1
        else:
            return 1

    def write_steps(self,dividend,divisor,rt):
        dd = Tex(str(dividend)).scale(scale_div)
        self.play(Write(dd), run_time=rt)
        self.play(dd.animate.move_to(6*UP + LEFT*self.dec_digits(dividend)*2), run_time=rt)
        dv = Tex(str(divisor)).next_to(dd, RIGHT, buff=MED_LARGE_BUFF).scale(scale_div)
        semi_box = SemiBox(dv, color = YELLOW)
        self.play(Create(semi_box), run_time=rt)
        self.play(Write(dv), run_time=rt)

        rlist = []
        quotient, qu, ndv = self.print_result(dividend, divisor, dd, dv, rlist, rt)
        while quotient >= divisor:
            quotient, qu, ndv = self.print_result(quotient, divisor, qu, ndv, rlist, rt);
        bin = qu.copy()

        rect = SurroundingRectangle(qu, color = PINK)
        self.play(Create(rect), run_time=rt)
        clist = [bin]
        for r in reversed(rlist):
            rect = SurroundingRectangle(r, color = PINK)
            self.play(Create(rect), run_time=rt)
            rem = r.copy()
            clist.append(rem)

        binary = Tex(r"0b").move_to(LEFT*self.dec_digits(dividend)*1.8+DOWN*2.2).scale(scale_bin)

        for c in clist:
            c.generate_target()
            if clist.index(c) == 0:
                c.target.next_to(binary, RIGHT, buff=MED_LARGE_BUFF)
            else:
                c.target.next_to(clist[clist.index(c)-1], RIGHT, buff=MED_LARGE_BUFF)
            self.play(MoveToTarget(c), run_time=rt)
            self.play(c.animate.scale(scale_bin/scale_div), run_time=rt)

        answer = VGroup(binary, *clist)
        answer_rect = SurroundingRectangle(answer, color = BLUE, buff=MED_SMALL_BUFF)

        amsb = Arrow(start=UP, end=DOWN, buff=SMALL_BUFF).next_to(clist[0], DOWN)
        msb = Tex(r"MSB").next_to(amsb, DOWN+LEFT, buff=MED_LARGE_BUFF).scale(scale_bin)
        amsb.set_color(GREEN)
        msb.set_color(GREEN)
        self.play(
            Create(binary),
            Create(answer_rect),
            Create(amsb),
            Create(msb),
            clist[0].animate.scale(1.2), run_time=rt
        )

        alsb = Arrow(start=UP, end=DOWN, buff=SMALL_BUFF).next_to(clist[-1], DOWN)
        lsb = Tex(r"LSB").next_to(alsb, DOWN+RIGHT, buff=MED_LARGE_BUFF).scale(scale_bin)
        alsb.set_color(ORANGE)
        lsb.set_color(ORANGE)
        self.play(
            Create(alsb),
            Create(lsb),
            clist[-1].animate.scale(0.85), run_time=rt
        )

        self.wait(2)
        self.clear()
