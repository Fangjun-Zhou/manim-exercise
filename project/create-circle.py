from manim import *

class CreateCircle(Scene):
    def construct(self):
        # Create a circle.
        circle = Circle(
            radius=2,
            color=BLUE,
        )
        
        # Show creation of circle.
        self.play(Create(circle))
        
        self.wait(1)