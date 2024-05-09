import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import math


class Model:
    def __init__(self):
        self.weight = 0
        self.thrust = 0
        self.sto = 0

    def set_weight(self, weight):
        self.weight = weight

    def set_thrust(self, thrust):
        self.thrust = thrust

    def calculate_sto(self, weight, thrust):
        cal = weight / 0.5 * 0.02377 * 1000 * 2.4
        vstall = math.sqrt(cal)
        vto = 1.2 * vstall
        A = 32.2 * thrust / weight
        B = 32.2 / weight * 0.5 * 0.02377 * 1000 * 0.0279
        sto = vto / A - B * vto * vto

        # Your STO calculation logic here
        self.sto = sto  # Example calculation


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STO Calculator")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.weight_label = QLabel("Weight:")
        self.weight_line_edit = QLineEdit()
        self.thrust_label = QLabel("Thrust:")
        self.thrust_line_edit = QLineEdit()
        self.calculate_button = QPushButton("Calculate")

        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_line_edit)
        layout.addWidget(self.thrust_label)
        layout.addWidget(self.thrust_line_edit)
        layout.addWidget(self.calculate_button)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.central_widget.setLayout(layout)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.calculate_button.clicked.connect(self.calculate)

    def calculate(self):
        weight = float(self.view.weight_line_edit.text())
        thrust = float(self.view.thrust_line_edit.text())

        self.model.set_weight(weight)
        self.model.set_thrust(thrust)
        self.model.calculate_sto(weight, thrust)
        # calculating specified weight

        # Plot graph
        plt.clf()
        weights = [weight, weight + 5000, weight + 10000]
        sto_values = [self.model.sto + 10000, self.model.sto + 200, self.model.sto]

        # Add thrust values
        thrust_values = [thrust, thrust - 2000, thrust + 5000]

        # Plot STO values with a solid line
        plt.plot(weights, sto_values, marker='o', linestyle='-', label='STO')

        # Plot thrust values with a solid line
        plt.plot(weights, thrust_values, marker='x', linestyle='-', label='Thrust')

        # Plot specified weight and STO
        plt.scatter(weight, self.model.sto, color='red', label='STO at specified weight')  # Circle indicating STO

        plt.xlabel('Weight')
        plt.ylabel('Values')
        plt.title('STO and Thrust vs Weight')

        # Legend
        plt.legend()

        self.view.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    view = View()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
