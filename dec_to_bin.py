from manim import *
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
            bin0.animate.shift(UP),
        )
        self.wait(6)
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
        self.wait(4)

        for nn in reversed(range(0,len(bin1)//3)):
            bin1[1+(nn*3)].set_color(colors[-nn])
            bin2[1+(nn*3)].set_color(colors[-nn])
        self.wait(3)

        recbs = []
        for nn in range(0,len(bin2)//3):
            recb = SurroundingRectangle(bin2[1+(nn*3)], color = YELLOW)
            recbs.append(recb)
        self.play(*list(map(Create, recbs)))
        self.wait(3)

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

        udb1 = Underline(bin_decomposed[0], color = YELLOW)
        udb2 = Underline(bin_decomposed[2], color = YELLOW)
        self.play(
            Create(udb1),
            Create(udb2),
        )
        text_nibbles = Tex("Nibbles")
        text_nibbles.set_color(YELLOW)
        text_nibbles.next_to(bin_group, DOWN * 2)
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
        text_byte.next_to(bin_group, RIGHT * 2)
        self.play(
            Create(text_byte)
        )


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
            self.play(Create(semi_box))
            self.play(Write(ndv))

        return quotient, qu, ndv

    def construct(self):
        dividend = 67
        divisor = 2

        dd = Tex(str(dividend))
        self.play(Write(dd))
        self.play(dd.animate.to_corner(UP + LEFT))
        dv = Tex(str(divisor)).next_to(dd, RIGHT, buff=MED_SMALL_BUFF)
        semi_box = SemiBox(dv, color = YELLOW)
        self.play(Create(semi_box))
        self.play(Write(dv))

        rlist = []
        quotient, qu, ndv = self.print_result(dividend, divisor, dd, dv, rlist)
        while quotient >= divisor:
            quotient, qu, ndv = self.print_result(quotient, divisor, qu, ndv, rlist);
        bin = qu.copy()

        rect = SurroundingRectangle(qu, color = PINK)
        self.play(Create(rect))
        clist = [bin]
        for r in reversed(rlist):
            rect = SurroundingRectangle(r, color = PINK)
            self.play(Create(rect))
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
            Create(amsb),
            Create(msb),
            Create(tmsb),
            tmsb.animate.shift(LEFT),
            clist[0].animate.scale(1.5)
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
            clist[-1].animate.scale(0.75)
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
