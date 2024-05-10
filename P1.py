import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from scipy.integrate import quad

class Model:
    """
    A class to represent the aircraft model for calculating the Short Take-Off (STO) distance.

    Attributes:
        weight (float): The weight of the aircraft in pounds.
        S (float): The wing area of the aircraft in square feet.
        C_Lmax (float): The maximum lift coefficient.
        C_D (float): The drag coefficient.
        rho (float): The air density in slugs per cubic foot.
        gc (float): The gravitational constant in ft/s².

    Methods:
        calculate_sto(thrust): Calculates the STO distance for a given thrust.
    """

    def __init__(self, weight, S=1000, C_Lmax=2.4, C_D=0.0279, rho=0.002377, gc=32.2):
        """
        Constructs all the necessary attributes for the model object.

        Parameters:
            weight (float): The weight of the aircraft in pounds.
            S (float, optional): The wing area of the aircraft in square feet. Defaults to 1000.
            C_Lmax (float, optional): The maximum lift coefficient. Defaults to 2.4.
            C_D (float, optional): The drag coefficient. Defaults to 0.0279.
            rho (float, optional): The air density in slugs per cubic foot. Defaults to 0.002377.
            gc (float, optional): The gravitational constant in ft/s². Defaults to 32.2.
        """
        self.weight = weight
        self.S = S
        self.C_Lmax = C_Lmax
        self.C_D = C_D
        self.rho = rho
        self.gc = gc

    def calculate_sto(self, thrust):
        """
        Calculate the STO distance based on the thrust provided.

        Parameters:
            thrust (float): The thrust in pounds-force (lbf).

        Returns:
            float: The calculated STO distance in feet.
        """
        V_stall = np.sqrt(self.weight / (0.5 * self.rho * self.S * self.C_Lmax))
        V_TO = 1.2 * V_stall
        A = self.gc * thrust / self.weight
        B = self.gc * (0.5 * self.rho * self.S * self.C_D) / self.weight

        def integrand(v):
            return v / (A - B * v ** 2)

        sto, _ = quad(integrand, 0, V_TO)
        return sto

class View(QMainWindow):
    """
    A class to setup the GUI using PyQt5.

    Attributes:
        central_widget (QWidget): The central widget of the main window.
        weight_input (QLineEdit): Input field for aircraft weight.
        thrust_input (QLineEdit): Input field for aircraft thrust.
        calculate_button (QPushButton): Button to trigger STO calculation.
        canvas (FigureCanvas): Canvas to draw the matplotlib plot.

    Methods:
        __init__(): Initializes the GUI components and layout.
    """

    def __init__(self):
        """
        Constructs the GUI layout and widgets.
        """
        super().__init__()
        self.setWindowTitle("STO Calculator")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.weight_label = QLabel("Weight (lb):")
        self.weight_input = QLineEdit()

        self.thrust_label = QLabel("Thrust (lbf):")
        self.thrust_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate")

        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.thrust_label)
        layout.addWidget(self.thrust_input)
        layout.addWidget(self.calculate_button)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.central_widget.setLayout(layout)

class Controller:
    """
    A class to control interactions between the model and view.

    Attributes:
        model (Model): The model object that performs the calculations.
        view (View): The view object that manages the GUI.

    Methods:
        __init__(model, view): Binds the model and view together.
        calculate_sto(): Retrieves inputs, performs calculation, and updates the GUI.
    """

    def __init__(self, model, view):
        """
        Connects the model with the view and sets up event listeners.

        Parameters:
            model (Model): The model object to handle calculations.
            view (View): The view object to interact with the GUI.
        """
        self.model = model
        self.view = view
        self.view.calculate_button.clicked.connect(self.calculate_sto)

    def calculate_sto(self):
        """
        Handles the button click event to perform STO calculations and update the plot.
        """
        weight = float(self.view.weight_input.text())
        thrust = float(self.view.thrust_input.text())

        model = Model(weight)
        sto = model.calculate_sto(thrust)

        thrust_range = np.linspace(10000, 30000, 100)
        sto_values = [model.calculate_sto(t) for t in thrust_range]

        model_plus = Model(weight + 10000)
        sto_values_plus = [model_plus.calculate_sto(t) for t in thrust_range]

        model_minus = Model(weight - 10000)
        sto_values_minus = [model_minus.calculate_sto(t) for t in thrust_range]

        plt.clf()
        plt.plot(thrust_range, sto_values, label='Weight = {} lb'.format(weight))
        plt.plot(thrust_range, sto_values_plus, label='Weight = {} lb (+10k)'.format(weight + 10000))
        plt.plot(thrust_range, sto_values_minus, label='Weight = {} lb (-10k)'.format(weight - 10000))
        plt.scatter([thrust], [sto], color='red', zorder=5)
        plt.xlabel('Thrust (lbf)')
        plt.ylabel('STO Distance (ft)')
        plt.title('STO vs. Thrust for Different Weights')
        plt.legend()
        self.view.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model(56000)  # default weight
    view = View()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
