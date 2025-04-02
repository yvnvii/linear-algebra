from manim import *

class GeneralizedNeuralNetwork(Scene):
    def construct(self):
        # Positions
        input_pos = [LEFT * 5 + UP * 2, LEFT * 5 + DOWN * 2]
        hidden_pos = [ORIGIN + UP * 2, ORIGIN + DOWN * 2]
        output_pos = RIGHT * 5

        # Title
        title = Text("Neural Network", font_size=32).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 1: Input Neurons
        input_labels = ["input 1", "input2"]
        input_nodes = []
        for i, pos in enumerate(input_pos):
            node = Circle(radius=0.5, color=WHITE, fill_opacity=1).move_to(pos)
            label = Text(input_labels[i], font_size=24).next_to(node, UP)
            self.play(Create(node), Write(label))
            input_nodes.append(node)

        # Step 2: Hidden Neurons
        hidden_nodes = []
        for i, pos in enumerate(hidden_pos):
            node = Circle(radius=0.5, color=WHITE, fill_opacity=1).move_to(pos)
            hidden_label = Text(f"hidden node {i+1}", font_size=20, color=GREEN).next_to(node, UP)
            self.play(Create(node), Write(hidden_label))
            hidden_nodes.append(node)

        # Step 3: Output Neuron
        output_node = Circle(radius=0.5, color=WHITE, fill_opacity=1).move_to(output_pos)
        bias_out = Text("output", font_size=20, color=GREEN).next_to(output_node, UP)
        self.play(Create(output_node), Write(bias_out))

        # Step 4: Draw input → hidden connections
        weight_names = [["w₁", "w₂"], ["w₃", "w₄"]]
        for i, input_node in enumerate(input_nodes):
            for j, hidden_node in enumerate(hidden_nodes):
                line = Line(input_node.get_center(), hidden_node.get_center(), color=BLUE)
                label = Text(weight_names[i][j], font_size=20).next_to(
                    line.get_center(), UP if j == 0 else DOWN, buff=0.15)
                self.play(Create(line), Write(label))

        # Step 5: Draw hidden → output connections
        output_weights = ["w₅", "w₆"]
        for i, hidden_node in enumerate(hidden_nodes):
            line = Line(hidden_node.get_center(), output_node.get_center(), color=BLUE)
            output_label = Text(output_weights[i], font_size=20).next_to(
                line.get_center(), UP if i == 0 else DOWN, buff=0.15)
            self.play(Create(line), Write(output_label))

        self.wait(1)

                # Step 7: input1 & input2 → h₁
        pulse1 = Dot(color=ORANGE).scale(0.8).move_to(input_nodes[0].get_center())
        pulse2 = Dot(color=ORANGE).scale(0.8).move_to(input_nodes[1].get_center())
        self.add(pulse1, pulse2)

        path1 = Line(input_nodes[0].get_center(), hidden_nodes[0].get_center())
        path2 = Line(input_nodes[1].get_center(), hidden_nodes[0].get_center())

        self.play(
            MoveAlongPath(pulse1, path1),
            MoveAlongPath(pulse2, path2),
            run_time=1
        )

        # ノードが「影響された」演出
        self.play(hidden_nodes[0].animate.set_fill(ORANGE, opacity=0.6).scale(1.2), run_time=0.3)
        self.play(hidden_nodes[0].animate.set_fill(WHITE, opacity=1).scale(1 / 1.2), run_time=0.3)

        self.play(FadeOut(pulse1), FadeOut(pulse2))

        # Step 8: input1 & input2 → h₂
        pulse3 = Dot(color=ORANGE).scale(0.8).move_to(input_nodes[0].get_center())
        pulse4 = Dot(color=ORANGE).scale(0.8).move_to(input_nodes[1].get_center())
        self.add(pulse3, pulse4)

        path3 = Line(input_nodes[0].get_center(), hidden_nodes[1].get_center())
        path4 = Line(input_nodes[1].get_center(), hidden_nodes[1].get_center())

        self.play(
            MoveAlongPath(pulse3, path3),
            MoveAlongPath(pulse4, path4),
            run_time=1
        )

        self.play(hidden_nodes[1].animate.set_fill(ORANGE, opacity=0.6).scale(1.2), run_time=0.3)
        self.play(hidden_nodes[1].animate.set_fill(WHITE, opacity=1).scale(1 / 1.2), run_time=0.3)

        self.play(FadeOut(pulse3), FadeOut(pulse4))



                # Step 9: h₁ & h₂ → o₁
        pulse5 = Dot(color=ORANGE).scale(0.8).move_to(hidden_nodes[0].get_center())
        pulse6 = Dot(color=ORANGE).scale(0.8).move_to(hidden_nodes[1].get_center())
        self.add(pulse5, pulse6)

        path5 = Line(hidden_nodes[0].get_center(), output_node.get_center())
        path6 = Line(hidden_nodes[1].get_center(), output_node.get_center())

        self.play(
            MoveAlongPath(pulse5, path5),
            MoveAlongPath(pulse6, path6),
            run_time=1
        )

        self.play(output_node.animate.set_fill(ORANGE, opacity=0.6).scale(1.2), run_time=0.3)
        self.play(output_node.animate.set_fill(WHITE, opacity=1).scale(1 / 1.2), run_time=0.3)

        self.play(FadeOut(pulse5), FadeOut(pulse6))

