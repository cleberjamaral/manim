from manim import *
import numpy as np

config.pixel_height = 1080
config.pixel_width = 1080

class Speaker(Scene):

    def get_samples(self, n_dots):
        time_graph = self.graph
        axes = self.time_axes

        dot = Dot(radius = 0.05, color = BLUE)
        pre_dots = VGroup(*[
            dot.copy().move_to(axes.coords_to_point(t, 0))
            for t in np.linspace(axes.x_min, axes.x_max, n_dots)
        ])
        pre_dots.set_fill(opacity = 0)
        time_graph.save_state()
        time_graph.generate_target()
        if not hasattr(time_graph, "is_faded"):
            time_graph.target.fade(0.7)
        time_graph.is_faded = True
        dot_set = [
            dot.copy().move_to(time_graph.point_from_proportion(a))
            for a in np.linspace(0, 1, n_dots)
        ]
        time_graph.dots = VGroup(*dot_set)

        self.play(
            ReplacementTransform(
                pre_dots, time_graph.dots,
                lag_ratio = 0.5,
                run_time = 2,
            ),
            MoveToTarget(time_graph),
        )
        return VGroup(time_graph.dots), dot_set

    def link_dots(self, dots):
        lines = []
        for dot in dots:
            if not dot == dots[-1]:
                line = Line(dot, dots[dots.index(dot)+1], buff=0)
                lines.append(line)
        if len(lines) > 0:
            self.play(*list(map(Create, lines)))
        return lines

    def func(self,x):
        return np.sin(15*x)*np.sin(0.5*x)

    def construct(self):
        self.x_max = 6.5
        axes = Axes(
            y_min = -1, y_max = 1,
            x_min = 0, x_max = self.x_max,
            axis_config = {"include_tip" : False},
        )
        axes.stretch_to_fit_height(3)
        axes.stretch_to_fit_width(10)
        axes.shift(3*UP+4*LEFT)
        frequency = 2.1
        graph = axes.get_graph(lambda x : self.func(x))
        f_min, f_max = [
            axes.x_axis.point_to_number(graph.get_points()[i])
            for i in (0, -1)
        ]
        func = lambda f : axes.y_axis.point_to_number(
            graph.point_from_proportion((f - f_min)/(f_max - f_min))
        )
        graph.set_color(YELLOW)

        speaker = SVGMobject("assets/speaker.svg").move_to(3*DOWN)

        self.play(Create(speaker))
        self.play(
            Broadcast(speaker),
            Create(graph),
            run_time = 2
        )
        amplitude = Tex("amplitude").move_to(axes.x_axis.get_left() + 0.5*LEFT).rotate(PI / 2)
        time = Tex("tempo").move_to(axes.x_axis.get_right() + RIGHT)

        axes_graph = VGroup(axes, amplitude, time)

        brace = Brace(Line(
            axes.coords_to_point(5.5/frequency, 1),
            axes.coords_to_point(6.4/frequency, 1),
        ), UP)
        period = brace.get_text("período", buff=SMALL_BUFF)
        period.scale(0.8, about_point = period.get_bottom())
        period2 = brace.get_text("T (sinal)", buff=SMALL_BUFF)
        period2.scale(0.8, about_point = period2.get_bottom())

        self.play(
            FadeOut(speaker),
            FadeIn(amplitude),
            Create(axes.y_axis)
        )
        self.play(
            Write(time),
            Create(axes.x_axis)
        )
        self.play(
            GrowFromCenter(brace),
            Write(period)
        )
        frequency = Tex("f = 1/T").next_to(period, RIGHT, buff=LARGE_BUFF)
        self.play(
            Write(frequency),
            Transform(period, period2)
        )
        self.wait(3)

        self.graph = graph
        self.time_axes = axes

        v_lines = VGroup(*[
            DashedLine(ORIGIN, 3*UP).move_to(axes.coords_to_point(n*self.x_max/19, 1), 2*UP)
            for n in range(1, 20)
        ])
        brace2 = Brace(Line(
            axes.coords_to_point(5*self.x_max/19, -0.9),
            axes.coords_to_point(6*self.x_max/19, -0.9),
        ), DOWN)
        period_sampling = brace2.get_text("T (amostragem)", buff=SMALL_BUFF)
        period_sampling.scale(0.8, about_point = period_sampling.get_bottom())
        self.play(
            Create(v_lines),
            Create(brace2),
            Write(period_sampling)
        )

        dots, dot_set = self.get_samples(20)

        self.play(
            FadeOut(v_lines),
            FadeOut(brace),
            FadeOut(period),
            FadeOut(period2),
            FadeOut(brace2),
            FadeOut(period_sampling),
            FadeOut(frequency),
        )

        v_line = DashedLine(ORIGIN, 0.65 * UP).move_to(axes.coords_to_point(1.35, 0), DOWN)
        h_line = DashedLine(ORIGIN, 2 * RIGHT).move_to(axes.coords_to_point(1.35, 0.65), RIGHT)
        coord = Tex("amplitude").scale(0.8).next_to(v_line, 1.8*UP, buff=MED_SMALL_BUFF)
        coord2 = Tex("y").scale(0.8).next_to(v_line, 1.8*UP, buff=MED_SMALL_BUFF)
        self.play(
            #Create(v_line),
            Create(h_line)
        )
        self.play(Create(coord))
        self.play(Transform(coord, coord2))
        self.wait(3)
        self.play(
            #FadeOut(v_line),
            FadeOut(h_line),
            FadeOut(coord),
            FadeOut(coord2),
        )

        discrete = Text("""
            dis.cre.to\n
            4. separado, distinto\n
            8. Que exprime objectos distintos, mas
               semelhantes.
            9. Que tem natureza, unidades ou
               elementos distintos ou não contínuos.\n
            Fontes: Wikcionário e Priberam [18-04-2021]
            """,
            font="Arial",
            t2f={
                "dis.cre.to": "Consolas",
                "Fontes: Wikcionário e Priberam [18-04-2021]": "Times",
            }
        ).scale(0.8).move_to(DOWN*2)
        self.play(
            Create(discrete),
            run_time = 2
        )
        self.wait(3)
        self.play(
            FadeOut(discrete),
            run_time = 2
        )

        copy_axes_graph = axes_graph.copy()
        copy_axes_graph.generate_target()
        copy_axes_graph.target.to_edge(DOWN)
        self.play(
            MoveToTarget(copy_axes_graph),
            run_time = 2
        )

        dots.generate_target()
        dots.target.move_to(LEFT*0.7 + DOWN*2)
        self.play(
            MoveToTarget(dots),
            run_time = 2
        )

        lines = self.link_dots(dot_set)
        self.wait(4)
        self.play(
            FadeOut(dots),
            *list(map(FadeOut, lines)),
            *list(map(FadeOut, dot_set))
        )
        self.wait()

        dots2, dot_set = self.get_samples(300)
        dots2.generate_target()
        dots2.target.move_to(LEFT*0.7 + DOWN*2)
        self.play(
            MoveToTarget(dots2),
            run_time = 2
        )
        self.link_dots(dot_set)

        self.wait(5)


class Speaker_old(Scene):

    def get_samples(self, n_dots):
        time_graph = self.graph
        axes = self.time_axes

        dot = Dot(radius = 0.05, color = BLUE)
        pre_dots = VGroup(*[
            dot.copy().move_to(axes.coords_to_point(t, 0))
            for t in np.linspace(axes.x_min, axes.x_max, n_dots)
        ])
        pre_dots.set_fill(opacity = 0)
        time_graph.save_state()
        time_graph.generate_target()
        if not hasattr(time_graph, "is_faded"):
            time_graph.target.fade(0.7)
        time_graph.is_faded = True
        dot_set = [
            dot.copy().move_to(time_graph.point_from_proportion(a))
            for a in np.linspace(0, 1, n_dots)
        ]
        time_graph.dots = VGroup(*dot_set)

        self.play(
            ReplacementTransform(
                pre_dots, time_graph.dots,
                lag_ratio = 0.5,
                run_time = 2,
            ),
            MoveToTarget(time_graph),
        )
        return VGroup(time_graph.dots), dot_set

    def link_dots(self, dots):
        lines = []
        for dot in dots:
            if not dot == dots[-1]:
                line = Line(dot, dots[dots.index(dot)+1], buff=0)
                lines.append(line)
        if len(lines) > 0:
            self.play(*list(map(Create, lines)))
        return lines

    def func(self,x):
        return np.sin(15*x)*np.sin(0.5*x)

    def construct(self):
        axes = Axes(
            y_min = -1, y_max = 1,
            x_min = 0, x_max = 10,
            axis_config = {"include_tip" : False},
        )
        axes.stretch_to_fit_height(2)
        axes.shift(2.5*UP+5.4*LEFT)
        frequency = 2.1
        graph = axes.get_graph(lambda x : self.func(x))
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
            Create(graph),
            run_time = 2
        )

        amplitude = Tex("amplitude").move_to(axes.x_axis.get_left() + 0.5*LEFT).rotate(PI / 2)
        time = Tex("tempo").move_to(axes.x_axis.get_right() + RIGHT)

        axes_graph = VGroup(axes, amplitude, time)

        brace = Brace(Line(
            axes.coords_to_point(5.5/frequency, 0.8),
            axes.coords_to_point(6.4/frequency, 0.8),
        ), UP)
        period = brace.get_text("período", buff=SMALL_BUFF)
        period.scale(0.8, about_point = period.get_bottom())
        period2 = brace.get_text("T (sinal)", buff=SMALL_BUFF)
        period2.scale(0.8, about_point = period2.get_bottom())

        self.play(
            FadeOut(speaker),
            FadeIn(amplitude),
            Create(axes.y_axis)
        )
        self.play(
            Write(time),
            Create(axes.x_axis)
        )
        self.play(
            GrowFromCenter(brace),
            Write(period)
        )
        frequency = Tex("f = 1/T").next_to(period, RIGHT, buff=LARGE_BUFF)
        self.play(
            Write(frequency),
            Transform(period, period2)
        )
        self.wait(3)

        self.graph = graph
        self.time_axes = axes

        v_lines = VGroup(*[
            DashedLine(ORIGIN, 2*UP).move_to(axes.coords_to_point(n*10/19, 1), 3*UP)
            for n in range(1, 20)
        ])
        brace2 = Brace(Line(
            axes.coords_to_point(5*10/19, -0.9),
            axes.coords_to_point(6*10/19, -0.9),
        ), DOWN)
        period_sampling = brace2.get_text("T (amostragem)", buff=SMALL_BUFF)
        period_sampling.scale(0.8, about_point = period_sampling.get_bottom())
        self.play(
            Create(v_lines),
            Create(brace2),
            Write(period_sampling)
        )

        dots, dot_set = self.get_samples(20)

        self.play(
            FadeOut(v_lines),
            FadeOut(brace),
            FadeOut(period),
            FadeOut(period2),
            FadeOut(brace2),
            FadeOut(period_sampling),
            FadeOut(frequency),
        )

        v_line = DashedLine(ORIGIN, 0.95 * UP).move_to(axes.coords_to_point(2.63, 0), DOWN)
        h_line = DashedLine(ORIGIN, 2.63 * RIGHT).move_to(axes.coords_to_point(2.63, 0.95), RIGHT)
        coord = Tex("amplitude").scale(0.8).next_to(v_line, UP, buff=SMALL_BUFF)
        coord2 = Tex("y").scale(0.8).next_to(v_line, UP, buff=SMALL_BUFF)
        self.play(
            #Create(v_line),
            Create(h_line)
        )
        self.play(Create(coord))
        self.play(Transform(coord, coord2))
        self.wait(3)
        self.play(
            #FadeOut(v_line),
            FadeOut(h_line),
            FadeOut(coord),
            FadeOut(coord2),
        )

        discrete = Text("""
            dis.cre.to\n
            4. separado, distinto\n
            8. Que exprime objectos distintos, mas
               semelhantes.
            9. Que tem natureza, unidades ou
               elementos distintos ou não contínuos.\n
            Fontes: Wikcionário e Priberam [18-04-2021]
            """,
            font="Arial",
            t2f={
                "dis.cre.to": "Consolas",
                "Fontes: Wikcionário e Priberam [18-04-2021]": "Times",
            }
        ).scale(0.5).move_to(DOWN*1.5)
        self.play(
            Create(discrete),
            run_time = 2
        )
        self.wait(3)
        self.play(
            FadeOut(discrete),
            run_time = 2
        )

        copy_axes_graph = axes_graph.copy()
        copy_axes_graph.generate_target()
        copy_axes_graph.target.to_edge(DOWN)
        self.play(
            MoveToTarget(copy_axes_graph),
            run_time = 2
        )

        dots.generate_target()
        dots.target.move_to(LEFT*0.4 + DOWN*2.38)
        self.play(
            MoveToTarget(dots),
            run_time = 2
        )

        lines = self.link_dots(dot_set)
        self.wait(4)
        self.play(
            FadeOut(dots),
            *list(map(FadeOut, lines)),
            *list(map(FadeOut, dot_set))
        )
        self.wait()

        dots2, dot_set = self.get_samples(300)
        dots2.generate_target()
        dots2.target.move_to(LEFT*0.4 + DOWN*2.38)
        self.play(
            MoveToTarget(dots2),
            run_time = 2
        )
        self.link_dots(dot_set)

        self.wait(5)


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
