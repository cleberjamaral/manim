from manim import *
import numpy as np

class Speaker(Scene):
    def func(self,x):
        return np.sin(15*x)*np.sin(0.5*x)

    def construct(self):
        axes = Axes(
            y_min = -2, y_max = 2,
            x_min = 0, x_max = 10,
            axis_config = {"include_tip" : False},
        )
        axes.stretch_to_fit_height(2)
        axes.to_corner(UP+LEFT)
        axes.shift(MED_SMALL_BUFF*DOWN+RIGHT)
        frequency = 2.1
        graph = axes.get_graph(lambda x : np.sin(15*x)*np.sin(0.5*x))
        f_min, f_max = [
            axes.x_axis.point_to_number(graph.get_points()[i])
            for i in (0, -1)
        ]
        func = lambda f : axes.y_axis.point_to_number(
            graph.point_from_proportion((f - f_min)/(f_max - f_min))
        )
        graph.set_color(YELLOW)

        speaker = SVGMobject("assets/speaker.svg").move_to(DOWN)

        self.play(Create(speaker))
        self.play(
            Broadcast(speaker),
            ShowCreation(graph),
            run_time = 2
        )
        self.play(
            Broadcast(speaker),
        )

        amplitude = Tex("amplitude").move_to(axes.x_axis.get_left() + 0.5*LEFT).rotate(PI / 2)
        time = Tex("tempo").next_to(axes.x_axis.get_right(), 3*DOWN+LEFT)

        n = 10.5
        brace = Brace(Line(
            axes.coords_to_point(n/frequency, self.func(n/frequency)),
            axes.coords_to_point((n+1)/frequency, self.func((n+1)/frequency)),
        ), UP)
        words = brace.get_text("período", buff = SMALL_BUFF)
        words.scale(0.8, about_point = words.get_bottom())


        self.play(
            FadeIn(amplitude),
            ShowCreation(axes.y_axis)
        )
        self.play(
            Write(time),
            ShowCreation(axes.x_axis)
        )
        self.play(
            GrowFromCenter(brace),
            Write(words)
        )
        self.wait()


class Broadcast(LaggedStart):
    def __init__(self, focal_point, **kwargs):
        animations = []
        circles = VGroup()
        for x in range(5):
            circle = Circle(
                radius=5,
                stroke_color=BLACK,
                stroke_width=0,
            )
            circle.add_updater(
                lambda c: c.move_to(focal_point)
            )
            circle.save_state()
            circle.set_width(0.1 * 2)
            circle.set_stroke(WHITE, 8)
            circles.add(circle)
        for circle in circles:
            animations.append(Restore(circle))
        super().__init__(*animations, **kwargs)
