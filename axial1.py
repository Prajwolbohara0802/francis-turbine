import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QTabWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QFormLayout, QGroupBox, QTableWidget, QTableWidgetItem
)
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# === Velocity Triangle Plot Widget ===
class VelocityTriangleCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.draw_empty_plot()

    def draw_empty_plot(self):
        self.ax.clear()
        self.ax.set_title("Velocity Triangle")
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.grid(True)
        self.draw()


# === Axial View Plot Widget ===
class AxialViewCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.draw_empty_plot()

    def draw_empty_plot(self):
        self.ax.clear()
        self.ax.set_title("Axial View")
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.grid(True)
        self.draw()


# === Velocity Triangle Tab ===
class VelocityTriangleTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        canvas = VelocityTriangleCanvas()
        layout.addWidget(canvas)

        input_group = QGroupBox("Design Inputs")
        form = QFormLayout()
        form.addRow("U_1:", QLineEdit("0.74115"))
        form.addRow("Z_p:", QLineEdit("3"))
        form.addRow("D_2 [m]:", QLineEdit("0.54"))
        form.addRow("Acceleration [%]:", QLineEdit("35.3"))
        input_group.setLayout(form)
        layout.addWidget(input_group)

        button_layout = QHBoxLayout()
        button_layout.addWidget(QPushButton("Check Values"))
        button_layout.addWidget(QPushButton("Update Design"))
        layout.addLayout(button_layout)

        info = QLabel(
            "Submit the head and the flow rate of the design case in question.\n"
            "This will execute plotting of the velocity triangles."
        )
        info.setWordWrap(True)
        layout.addWidget(info)

        # Dummy table
        table = QTableWidget(1, 5)
        table.setHorizontalHeaderLabels(["U1", "Zp", "D2", "W1", "beta1"])
        for i in range(5):
            table.setItem(0, i, QTableWidgetItem("0.00"))
        layout.addWidget(table)

        self.setLayout(layout)


# === Axial View Tab ===
class AxialViewTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        self.canvas = AxialViewCanvas()
        layout.addWidget(self.canvas, 3)

        control_layout = QVBoxLayout()
        form_group = QGroupBox("Streamline Settings")
        form = QFormLayout()
        self.streamline_input = QLineEdit("10")
        self.b_input = QLineEdit("0.16")
        form.addRow("Streamlines", self.streamline_input)
        form.addRow("b", self.b_input)
        form_group.setLayout(form)
        control_layout.addWidget(form_group)

        update_btn = QPushButton("Update Design")
        reset_btn = QPushButton("Reset Plot")
        update_btn.clicked.connect(self.update_plot)
        reset_btn.clicked.connect(self.reset_plot)
        control_layout.addWidget(update_btn)
        control_layout.addWidget(reset_btn)

        desc = QLabel("The streamline is governed by Bezier curves.\nYou can modify values and update the design.")
        desc.setWordWrap(True)
        control_layout.addWidget(desc)

        layout.addLayout(control_layout, 2)
        self.setLayout(layout)

    def update_plot(self):
        """Empty update method - can be implemented later"""
        pass

    def reset_plot(self):
        """Empty reset method - can be implemented later"""
        pass


# === Main Application ===
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Francis Turbine Optimization")
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowIcon(QIcon("francis.ico"))

        tabs = QTabWidget()
        tabs.addTab(VelocityTriangleTab(), "Velocity Triangle")
        tabs.addTab(AxialViewTab(), "Axial View")

        self.setCentralWidget(tabs)


# === Run App ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())