from manim import *
import numpy as np

class NeuralNetwork(Scene):
    def construct(self):
        # Define input values (Study Hours, Sleep Hours)
        input_values = np.array([6, 8])  

        # Define weight matrices (Input → Hidden: 2x2, Hidden → Output: 2x1)
        input_to_hidden_weights = np.array([
            [0.5, -0.3],  
            [0.8, -0.5]  
        ])

        hidden_to_output_weights = np.array([
            [0.7],  
            [-0.8]  
        ])

        # Biases for hidden and output layers
        hidden_biases = np.array([2, -3])
        output_bias = np.array([1.5])

        # Compute neuron inputs (weighted sum)
        hidden_inputs = np.dot(input_values, input_to_hidden_weights) + hidden_biases
        output_inputs = np.dot(hidden_inputs, hidden_to_output_weights) + output_bias  

        # Define positions for each neuron (Fixed to 3D format)
        input_positions = [np.array([-4, 2, 0]), np.array([-4, -2, 0])]
        hidden_positions = [np.array([0, 2, 0]), np.array([0, -2, 0])]
        output_position = np.array([4, 0, 0])

        # Step 1: Show input neurons
        input_neurons = []
        for pos in input_positions:
            neuron = Circle(radius=0.5, color=WHITE, fill_opacity=1).move_to(pos)
            input_neurons.append(neuron)
            self.play(Create(neuron), run_time=0.5)

        # Step 2: Show input labels (Study Hours, Sleep Hours) & store references
        input_labels = ["Study Hours", "Sleep Hours"]
        input_label_texts = []
        for i, neuron in enumerate(input_neurons):
            label = Text(f"{input_labels[i]}", font_size=20).next_to(neuron, UP, buff=0.3)
            input_label_texts.append(label)  # Store label references
            self.play(Write(label), run_time=0.5)

        # Step 3: Draw input-to-hidden connections (one at a time)
        for i, input_neuron in enumerate(input_neurons):
            for j, hidden_pos in enumerate(hidden_positions):
                line = Line(input_neuron.get_center(), hidden_pos, color=BLUE)
                self.play(Create(line), run_time=0.5)

                # Step 4: Show weights (one at a time) without overlap
                shift_direction = UP if j % 2 == 0 else DOWN
                weight_text = Text(f"{input_to_hidden_weights[i][j]:.2f}", font_size=20, color=WHITE).next_to(
                    line.get_center(), shift_direction, buff=0.2)
                self.play(Write(weight_text), run_time=0.5)

        # Step 5: Show hidden layer neurons (one at a time)
        hidden_neurons = []
        for pos in hidden_positions:
            neuron = Circle(radius=0.5, color=WHITE, fill_opacity=1).move_to(pos)
            hidden_neurons.append(neuron)
            self.play(Create(neuron), run_time=0.5)

        # Step 6: Show hidden biases
        for i, neuron in enumerate(hidden_neurons):
            bias_text = Text(f"Bias: {hidden_biases[i]:.2f}", font_size=20).next_to(neuron, UP, buff=0.3)
            self.play(Write(bias_text), run_time=0.5)

        # Step 7: Draw hidden-to-output connections (one at a time)
        output_neuron = Circle(radius=0.5, color=WHITE, fill_opacity=1).move_to(output_position)
        for i, hidden_neuron in enumerate(hidden_neurons):
            line = Line(hidden_neuron.get_center(), output_position, color=BLUE)
            self.play(Create(line), run_time=0.5)

            # Step 8: Show hidden-to-output weights (one at a time)
            shift_direction = UP if j % 2 == 0 else DOWN
            weight_text = Text(f"{hidden_to_output_weights[i][0]:.2f}", font_size=20, color=WHITE).next_to(
                line.get_center(), shift_direction, buff=0.2)
            self.play(Write(weight_text), run_time=0.5)

        # Step 9: Show output neuron
        self.play(Create(output_neuron), run_time=0.5)

        # Step 10: Show output bias
        output_bias_text = Text(f"Bias: {output_bias[0]:.2f}", font_size=20).next_to(output_neuron, UP, buff=0.3)
        self.play(Write(output_bias_text), run_time=0.5)

        # Step 11: FINALLY, SHOW INPUT VALUES ABOVE INPUT NODES
        for i, neuron in enumerate(input_neurons):
            value_text = Text(f"{input_values[i]:.2f}", font_size=22, color=YELLOW).next_to(input_label_texts[i], UP, buff=0.2)
            self.play(Write(value_text), run_time=0.5)

        # Hold final frame
        self.wait(2)
