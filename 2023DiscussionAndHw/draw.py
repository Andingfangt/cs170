from manim import *

class FeasibleRegionLines(Scene):
    def construct(self):

        # Create axes with labels
        axes = Axes(
            x_range=[-5, 25],
            y_range=[-5, 40],
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(-5, 25, 5),
                "numbers_with_elongated_ticks": np.arange(-5, 25, 5),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-5, 40, 5),
                "numbers_with_elongated_ticks": np.arange(-5, 40, 5),
            },
        )

        # Add axes to the scene
        self.add(axes)

        line_1 = axes.plot(lambda x : -4 * x + 80, x_range=[0,30])
        line_2 = axes.plot(lambda x : -2/3 * x +30, x_range=[0,30])
        # line_3 = axes.plot(lambda x : -x + 4, x_range= [-1,7])
        line_4 = axes.plot(lambda x : 0, x_range=[-5,30])
        line_5 = Line(start=axes.c2p(0, 0), end=axes.c2p(0, 40))
        line_1_label = axes.get_graph_label(line_1, label="4x+y \leq 80", x_val=1, direction=RIGHT)
        line_2_label = axes.get_graph_label(line_2, label="2x+3y \leq 90", direction= UP )
        # line_3_label = axes.get_graph_label(line_3, label="4x+4y \geq 16" )
        self.add(line_1, line_2, line_4, line_5,line_1_label ,line_2_label)   
        
        line_down = line_4
        line_up = axes.plot(lambda x: -2/3*x + 30 if x <=15 else -4 * x + 80)
        area_1 = axes.get_area(line_up, [0, 20], bounded_graph=line_down, color=GREY, opacity=0.5)
        self.add(area_1)
        
        dot_1 = axes.c2p(0,30)
        dot_1_text = Text('(0,30)').next_to(dot_1,UP)
        dot_2 = axes.c2p(0,0)
        dot_2_text = Text('(0,0)').next_to(dot_2,DOWN)
        dot_3 = axes.c2p(20,0)
        dot_3_text = Text('(20,0)').next_to(dot_3, DOWN)
        dot_4 = axes.c2p(15,20)
        dot_4_text = Text('(15,20)').next_to(dot_4, UP)
        self.add(dot_4_text,dot_3_text,dot_2_text,dot_1_text)
        
        
        # manim -pql draw.py FeasibleRegionLines