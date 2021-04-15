from manim import *
import numpy as np

class SemiBox(VGroup):
    CONFIG = {
        "stroke_color": YELLOW
    }
    def __init__(self, mobject, **kwargs):
        VGroup.__init__(self, **kwargs)
        vline = Line(start=[0,mobject.get_height(),0], end=[0,-0.2,0]).next_to(mobject, LEFT, buff=SMALL_BUFF)
        vline.set_stroke(self.stroke_color)
        hline = Line(start=[-0.2,0,0], end=[mobject.get_width(),0,0]).next_to(mobject, DOWN, buff=SMALL_BUFF)
        hline.set_stroke(self.stroke_color)
        self.add(vline, hline)


class NumericalSystems(Scene):
    def construct(self):
        target_amount = 1000.00
        currency = Tex(r"R\$")
        amount = DecimalNumber(0.00)
        amount.next_to(currency,RIGHT)
        money = VGroup(currency, amount)
        money.move_to(ORIGIN+LEFT*3)
        money.scale(4)
        self.play(
            Create(money),
        )
        self.play(
            ChangeDecimalToValue(amount, target_amount),
        )
        self.wait()
        self.play(
            money.animate.scale(0.4).move_to(LEFT*5+UP*3)
        )

        #Image created by Edward Boatman. Changed color and fill. Available at https://commons.wikimedia.org/wiki/File:Edward_Boatman_scale.svg
        scale = SVGMobject("assets/Edward_Boatman_scale.svg")
        scale.scale(2)
        self.play(Create(scale))
        self.wait()
        self.play(
            scale.animate.scale(0.5).move_to(LEFT*5)
        )
        # https://commons.wikimedia.org/wiki/File:Speedometer_(CoreUI_Icons_v1.0.0).svg
        speedometer = SVGMobject("assets/Speedometer_(CoreUI_Icons_v1.0.0).svg")
        speedometer.scale(2)
        self.play(Create(speedometer))
        self.wait()
        self.play(
            speedometer.animate.scale(0.5).move_to(LEFT*5+DOWN*3)
        )

        decimal = Integer(0)
        decimal.move_to(ORIGIN+RIGHT)
        decimal.scale(4)
        self.play(Create(decimal))
        self.play(ChangeDecimalToValue(decimal, 9))
        self.wait()
        decimal.set_value(0)
        self.wait()
        self.play(ChangeDecimalToValue(decimal, 9))
        self.wait(2)
        decimal.set_value(0)
        self.wait()
        self.play(ChangeDecimalToValue(decimal, 9))
        self.wait(2)

        self.play(
            FadeOut(money),
            FadeOut(speedometer),
            FadeOut(scale),
            FadeOut(decimal)
        )

        # https://commons.wikimedia.org/wiki/File:AnalogClockAnimation2_still_frame.svg
        clock = SVGMobject("assets/AnalogClockAnimation2_still_frame.svg")
        clock.scale(3)
        self.play(Create(clock))
        self.wait()
        self.play(
            clock.animate.scale(0.5).move_to(LEFT*5)
        )

        duodecimal = Integer(0)
        duodecimal.move_to(ORIGIN+RIGHT)
        duodecimal.scale(4)
        self.play(Create(duodecimal))
        self.play(ChangeDecimalToValue(duodecimal, 11))
        self.wait()
        duodecimal.set_value(0)
        self.play(ChangeDecimalToValue(duodecimal, 11))
        self.wait()
        duodecimal.set_value(0)
        self.play(ChangeDecimalToValue(duodecimal, 59))
        self.wait()
        duodecimal.set_value(0)
        self.play(ChangeDecimalToValue(duodecimal, 59))
        self.wait(4)

        self.play(
            FadeOut(duodecimal),
            FadeOut(clock)
        )

class DecimalSystem(Scene):
    def construct(self):
        target_number = 147

        dec0 = Integer(1)
        self.play(
            ChangeDecimalToValue(dec0, target_number)
        )
        self.wait()
        self.play(dec0.animate.shift(UP))
        self.wait()

        dec1 = Tex(
            r"1*",r"100", r"+",
            r"4*",r"10", r"+",
            r"7*",r"1", r" = 147"
        )
        self.play(Write(dec1))
        self.wait()
        self.play(
            dec0.animate.shift(UP),
            dec1.animate.shift(UP)
        )
        self.wait()

        dec2 = Tex(
            r"1*",r"$10^2$", r"+",
            r"4*",r"$10^1$", r"+",
            r"7*",r"$10^0$", r" = 147"
        )
        self.play(Write(dec2))
        self.wait()
        self.play(
            dec0.animate.shift(UP),
            dec1.animate.shift(UP),
            dec2.animate.shift(UP)
        )
        self.wait()

        dec3 = Tex(
            r"1~",r"centena", r"+",
            r"4~",r"dezenas", r"+",
            r"7~",r"unidades", r" = 147")
        self.play(Write(dec3))
        self.play(
            dec3.animate.shift(ORIGIN)
        )
        self.wait()

        colors = [ORANGE,PINK,PURPLE,GRAY,RED,BLUE,GREEN]
        for nn in reversed(range(0,len(dec1)//3)):
            dec1[1+(nn*3)].set_color(colors[-nn])
            dec2[1+(nn*3)].set_color(colors[-nn])
            dec3[1+(nn*3)].set_color(colors[-nn])
        self.wait()

        self.play(
            FadeOut(dec0),
            FadeOut(dec1),
            FadeOut(dec3),
            dec2.animate.shift(ORIGIN).scale(1.5)
        )
        self.wait()

        dec2.set_color_by_tex("1*",WHITE)
        dec2.set_color_by_tex("4*",WHITE)
        dec2.set_color_by_tex("7*",WHITE)
        self.wait()

        rects = []
        for nn in range(0,len(dec2)//3):
            rect = SurroundingRectangle(dec2[1+(nn*3)], color = YELLOW)
            rects.append(rect)
        self.play(*list(map(Create, rects)))

        self.wait(2)

        rects_arrows = []
        for re in reversed(rects):
            if len(rects_arrows) < (len(rects) - 1):
                arrow = CurvedArrow(
                    re.get_left()+UP/2,
                    rects[rects.index(re)-1].get_right()+UP/2,
                    radius=1,
                    color=YELLOW
                )
                rects_arrows.append(arrow)
                self.play(Create(arrow))
        self.wait(4)

        arrow = DoubleArrow(ORIGIN, 5*RIGHT).move_to(ORIGIN)
        self.play(
            Create(arrow),
        )
        tleft = Tex("Mais~significativo").next_to(arrow, LEFT)
        tright = Tex("Menos~significativo").next_to(arrow, RIGHT)
        self.play(
            Create(tleft),
            Create(tright)
        )
        self.wait(2)

        self.play(
            *list(map(FadeOut, rects)),
            *list(map(FadeOut, rects_arrows)),
            dec2.animate.shift(UP).scale(0.667),
            FadeOut(arrow),
            FadeOut(tleft),
            FadeOut(tright)
        )

        bin0 = Tex(f"${target_number:d}$" , "~=~", f"0b{target_number:b}")
        self.play(
            Create(bin0),
        )
        self.wait(2)

        bin1 = Tex(
            r"1*", r"128", r"+",
            r"0*", r"64", r"+",
            r"0*", r"32", r"+",
            r"1*", r"16", r"+",
            r"0*", r"8", r"+",
            r"0*", r"4", r"+",
            r"1*", r"2", r"+",
            r"1*", r"1", "~=~", "0b", f"${target_number:b}$"
        )
        self.play(
            bin0.animate.shift(UP)
        )
        self.wait(1)
        for nn in reversed(range(0,len(bin1)//3)):
            bin1[1+(nn*3)].set_color(colors[-nn])
        self.wait(5)

        self.play(
            dec2.animate.shift(UP),
            bin0.animate.shift(UP),
            bin1.animate.shift(UP)
        )
        self.wait(4)

        bin2 = Tex(
            r"1*", r"$2^7$", r"+",
            r"0*", r"$2^6$", r"+",
            r"0*", r"$2^5$", r"+",
            r"1*", r"$2^4$", r"+",
            r"0*", r"$2^3$", r"+",
            r"0*", r"$2^2$", r"+",
            r"1*", r"$2^1$", r"+",
            r"1*", r"$2^0$", "~=~", "0b", f"${target_number:b}$"
        )
        self.play(Write(bin2))
        self.wait(1)

        for nn in reversed(range(0,len(bin1)//3)):
            bin2[1+(nn*3)].set_color(colors[-nn])
        self.wait(5)

        for nn in range(0,len(dec2)//3):
            rects[nn] = SurroundingRectangle(dec2[1+(nn*3)], color = YELLOW)
        self.play(*list(map(FadeIn, rects)))
        self.wait(2)

        recbs = []
        for nn in range(0,len(bin2)//3):
            recb = SurroundingRectangle(bin2[1+(nn*3)], color = GREEN)
            recbs.append(recb)
        self.play(*list(map(Create, recbs)))
        self.wait(2)

        recbs_arrows = []
        for re in reversed(recbs):
            if len(recbs_arrows) < (len(recbs) - 1):
                arrow = CurvedArrow(
                    re.get_left()+UP/2,
                    recbs[recbs.index(re)-1].get_right()+UP/2,
                    radius=1,
                    color=GREEN
                )
                recbs_arrows.append(arrow)
        self.play(*list(map(Create, recbs_arrows)))
        self.wait(8)

        self.play(
            *list(map(FadeOut, recbs_arrows)),
            *list(map(FadeOut, rects)),
            *list(map(FadeOut, recbs)),
        )

        bin = bin0[2].copy()
        bin.generate_target()
        bin.target.move_to(DOWN)
        self.play(
            MoveToTarget(bin)
        )
        self.wait()

        bin_notation = Tex(r"0b")
        bin_decomposed = Tex(r"1001", r"~~", r"0011")
        bin_decomposed.next_to(bin_notation, RIGHT)
        bin_group = VGroup(bin_notation, bin_decomposed)
        bin_group.next_to(bin, DOWN)
        self.play(
            Transform(bin, bin_group),
        )
        self.wait(2)

        bits_arrows = []
        for i in range(0,4):
            arrow = Arrow(
                bin_decomposed[0].get_left()+UP + RIGHT*0.05 + RIGHT*(i*0.25),
                bin_decomposed[0].get_left()    + RIGHT*0.05 + RIGHT*(i*0.25),
                color=PURPLE
            )
            bits_arrows.append(arrow)
        for i in range(0,4):
            arrow = Arrow(
                bin_decomposed[2].get_left()+UP + RIGHT*0.05 + RIGHT*(i*0.25),
                bin_decomposed[2].get_left()    + RIGHT*0.05 + RIGHT*(i*0.25),
                color=PURPLE
            )
            bits_arrows.append(arrow)
        self.play(*list(map(Create, bits_arrows)))
        self.wait(4)

        text_bits = Tex("Bits")
        text_bits.set_color(PURPLE)
        text_bits.next_to(bin_group, UP * 2 + RIGHT)
        self.play(
            Create(text_bits)
        )
        self.wait(2)


        udb1 = Underline(bin_decomposed[0], color = ORANGE)
        udb2 = Underline(bin_decomposed[2], color = ORANGE)
        self.play(
            Create(udb1),
            Create(udb2),
        )
        text_nibbles = Tex("Nibbles")
        text_nibbles.set_color(ORANGE)
        text_nibbles.next_to(bin_group, RIGHT * 2)
        self.play(
            Create(text_nibbles)
        )
        self.wait(2)

        rec_byte = SurroundingRectangle(bin_decomposed, color = BLUE, buff=MED_SMALL_BUFF)
        self.play(
            Create(rec_byte)
        )
        text_byte = Tex("Byte")
        text_byte.set_color(BLUE)
        text_byte.next_to(bin_group, DOWN * 2 + RIGHT)
        self.play(
            Create(text_byte)
        )

class Test(Scene):
    def construct(self):
        #Image created by Edward Boatman. Changed color and fill. Available at https://commons.wikimedia.org/wiki/File:Edward_Boatman_scale.svg
        img_mobject = SVGMobject("assets/Edward_Boatman_scale.svg")
        img_mobject.scale(3)
        self.add(img_mobject)
        self.play(Create(img_mobject))

        self.wait(5)


class DecToBin(Scene):
    def print_result(self, dividend, divisor, dd, dv, rlist, rt):
        quotient = dividend // divisor
        remainder = dividend % divisor

        re = Tex(str(remainder)).next_to(dd, DOWN, buff=MED_SMALL_BUFF)
        rlist.append(re)
        qu = Tex(str(quotient)).next_to(dv, DOWN, buff=MED_SMALL_BUFF)
        self.play(Write(qu), run_time=rt)
        self.play(Write(re), run_time=rt)

        ndv = Tex(str(divisor)).next_to(qu, RIGHT, buff=MED_SMALL_BUFF)
        if quotient >= divisor:
            semi_box = SemiBox(ndv, color = YELLOW)
            self.play(Create(semi_box, run_time=rt))
            self.play(Write(ndv), run_time=rt)

        return quotient, qu, ndv

    def construct(self):
        dividend = 9
        divisor = 2
        rt = 0.2

        dd = Tex(str(dividend))
        self.play(Write(dd), run_time=rt)
        self.play(dd.animate.to_corner(UP + LEFT), run_time=rt)
        dv = Tex(str(divisor)).next_to(dd, RIGHT, buff=MED_SMALL_BUFF)
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

        for c in clist:
            c.generate_target()
            if clist.index(c) == 0:
                c.target.move_to(ORIGIN)
            else:
                c.target.next_to(clist[clist.index(c)-1], RIGHT)
            c.set_height(2*c.get_height())
            self.play(
                MoveToTarget(c), run_time=rt
            )
            self.play(
                c.animate.scale(1.5), run_time=rt
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
            Create(amsb),
            Create(msb),
            Create(tmsb),
            tmsb.animate.shift(LEFT),
            clist[0].animate.scale(1.5), run_time=rt
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
            Create(alsb),
            Create(lsb),
            Create(tlsb),
            tlsb.animate.shift(RIGHT*1.5),
            clist[-1].animate.scale(0.75), run_time=rt
        )

        self.wait()

class Notation(Scene):
    def construct(self):
        dividend = 67
        result = Tex(str(dividend), "~=~", f"{dividend:b}")
        self.play(
            result.animate.shift(UP*3),
            Write(result)
        )
        self.wait(2)

        result2 = Tex(f"${dividend:d}$", "$_{10}$", "~=~", f"${dividend:b}_2$")
        self.play(
            Transform(result, result2)
        )
        self.wait(2)

        result3 = Tex(f"$0d{dividend:d}$", "~=~",  f"$0b{dividend:b}$")
        self.play(
            FadeOut(result),
            Transform(result2, result3)
        )
        self.wait(2)

        result4 = Tex(f"${dividend:d}$", "~=~", f"$0b{dividend:b}$")
        self.play(
            FadeOut(result2),
            Transform(result3, result4)
        )
        self.play(FadeOut(result3))
        self.wait(3)
