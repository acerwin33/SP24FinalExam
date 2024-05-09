import tkinter as tk
from tkinter import ttk
import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
#region imports
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
import math
#these imports are necessary for drawing a matplot lib graph on my GUI
#no simple widget for this exists in QT Designer, so I have to add the widget in code.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
#endregion
from PyQt5 import QtCore, QtGui, QtWidgets

class QuarterCarModelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quarter Car Model")
        
        self.position_vs_time_graph_frame = ttk.Frame(self.root)
        self.position_vs_time_graph_frame.pack(fill=tk.BOTH, expand=True)
        
        self.force_vs_time_graph_frame = ttk.Frame(self.root)
        self.force_vs_time_graph_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tab_parent = ttk.Notebook(self.root)
        self.tab_parent.pack(fill=tk.BOTH, expand=True)
        
        self.position_vs_time_tab = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.position_vs_time_tab, text="Position vs. Time")
        
        self.force_vs_time_tab = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.force_vs_time_tab, text="Force vs. Time")
        
        self.position_vs_time_graph_canvas = tk.Canvas(self.position_vs_time_tab)
        self.position_vs_time_graph_canvas.pack(fill=tk.BOTH, expand=True)
        
        self.force_vs_time_graph_canvas = tk.Canvas(self.force_vs_time_tab)
        self.force_vs_time_graph_canvas.pack(fill=tk.BOTH, expand=True)
        
        self.compute_button = ttk.Button(self.root, text="Compute", command=self.compute)
        self.compute_button.pack()

    def compute(self):
        # Add code here to compute forces and positions
        
        # Update graphs
        self.plot_position_vs_time()
        self.plot_force_vs_time()

    def plot_position_vs_time(self):
        # Add code here to plot position vs. time graph
        # Example:
        t = np.linspace(0, 10, 100)
        position = np.sin(t)
        
        plt.figure()
        plt.plot(t, position)
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.title('Position vs. Time')
        plt.grid(True)
        plt.show()

    def plot_force_vs_time(self):
        # Add code here to plot force vs. time graph
        # Example:
        t = np.linspace(0, 10, 100)
        force = np.cos(t)
        
        plt.figure()
        plt.plot(t, force)
        plt.xlabel('Time')
        plt.ylabel('Force')
        plt.title('Force vs. Time')
        plt.grid(True)
        plt.show()

root = tk.Tk()
app = QuarterCarModelGUI(root)
root.mainloop()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1143, 959)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grp_Inputs = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_Inputs.sizePolicy().hasHeightForWidth())
        self.grp_Inputs.setSizePolicy(sizePolicy)
        self.grp_Inputs.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.grp_Inputs.setFont(font)
        self.grp_Inputs.setFlat(False)
        self.grp_Inputs.setObjectName("grp_Inputs")
        self.gridLayout = QtWidgets.QGridLayout(self.grp_Inputs)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.le_k2 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_k2.sizePolicy().hasHeightForWidth())
        self.le_k2.setSizePolicy(sizePolicy)
        self.le_k2.setMinimumSize(QtCore.QSize(75, 0))
        self.le_k2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_k2.setFont(font)
        self.le_k2.setObjectName("le_k2")
        self.gridLayout.addWidget(self.le_k2, 5, 1, 1, 1)
        self.le_tmax = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_tmax.sizePolicy().hasHeightForWidth())
        self.le_tmax.setSizePolicy(sizePolicy)
        self.le_tmax.setMinimumSize(QtCore.QSize(75, 0))
        self.le_tmax.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_tmax.setObjectName("le_tmax")
        self.gridLayout.addWidget(self.le_tmax, 7, 1, 1, 1)
        self.lbl_CarSpeed = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_CarSpeed.sizePolicy().hasHeightForWidth())
        self.lbl_CarSpeed.setSizePolicy(sizePolicy)
        self.lbl_CarSpeed.setObjectName("lbl_CarSpeed")
        self.gridLayout.addWidget(self.lbl_CarSpeed, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_m2 = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_m2.sizePolicy().hasHeightForWidth())
        self.lbl_m2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_m2.setFont(font)
        self.lbl_m2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_m2.setObjectName("lbl_m2")
        self.gridLayout.addWidget(self.lbl_m2, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_k2 = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_k2.sizePolicy().hasHeightForWidth())
        self.lbl_k2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_k2.setFont(font)
        self.lbl_k2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_k2.setObjectName("lbl_k2")
        self.gridLayout.addWidget(self.lbl_k2, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lbl_Spring1 = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Spring1.sizePolicy().hasHeightForWidth())
        self.lbl_Spring1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Spring1.setFont(font)
        self.lbl_Spring1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Spring1.setObjectName("lbl_Spring1")
        self.gridLayout.addWidget(self.lbl_Spring1, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_c1 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_c1.sizePolicy().hasHeightForWidth())
        self.le_c1.setSizePolicy(sizePolicy)
        self.le_c1.setMinimumSize(QtCore.QSize(75, 0))
        self.le_c1.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_c1.setFont(font)
        self.le_c1.setObjectName("le_c1")
        self.gridLayout.addWidget(self.le_c1, 3, 1, 1, 1)
        self.le_m1 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_m1.sizePolicy().hasHeightForWidth())
        self.le_m1.setSizePolicy(sizePolicy)
        self.le_m1.setMinimumSize(QtCore.QSize(75, 0))
        self.le_m1.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_m1.setFont(font)
        self.le_m1.setObjectName("le_m1")
        self.gridLayout.addWidget(self.le_m1, 0, 1, 1, 1)
        self.lbl_tMax = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tMax.sizePolicy().hasHeightForWidth())
        self.lbl_tMax.setSizePolicy(sizePolicy)
        self.lbl_tMax.setObjectName("lbl_tMax")
        self.gridLayout.addWidget(self.lbl_tMax, 7, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_v = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_v.sizePolicy().hasHeightForWidth())
        self.le_v.setSizePolicy(sizePolicy)
        self.le_v.setMinimumSize(QtCore.QSize(75, 0))
        self.le_v.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_v.setObjectName("le_v")
        self.gridLayout.addWidget(self.le_v, 1, 1, 1, 1)
        self.lbl_CarBodyMass = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_CarBodyMass.sizePolicy().hasHeightForWidth())
        self.lbl_CarBodyMass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_CarBodyMass.setFont(font)
        self.lbl_CarBodyMass.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_CarBodyMass.setObjectName("lbl_CarBodyMass")
        self.gridLayout.addWidget(self.lbl_CarBodyMass, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gv_Schematic = QtWidgets.QGraphicsView(self.grp_Inputs)
        self.gv_Schematic.setMinimumSize(QtCore.QSize(500, 500))
        self.gv_Schematic.setMaximumSize(QtCore.QSize(600, 600))
        self.gv_Schematic.setObjectName("gv_Schematic")
        self.gridLayout.addWidget(self.gv_Schematic, 15, 0, 1, 2)
        self.chk_IncludeAccel = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_IncludeAccel.setObjectName("chk_IncludeAccel")
        self.gridLayout.addWidget(self.chk_IncludeAccel, 12, 0, 1, 2, QtCore.Qt.AlignRight)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_calculate = QtWidgets.QPushButton(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_calculate.sizePolicy().hasHeightForWidth())
        self.btn_calculate.setSizePolicy(sizePolicy)
        self.btn_calculate.setObjectName("btn_calculate")
        self.horizontalLayout_2.addWidget(self.btn_calculate, 0, QtCore.Qt.AlignRight)
        self.pb_Optimize = QtWidgets.QPushButton(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_Optimize.sizePolicy().hasHeightForWidth())
        self.pb_Optimize.setSizePolicy(sizePolicy)
        self.pb_Optimize.setObjectName("pb_Optimize")
        self.horizontalLayout_2.addWidget(self.pb_Optimize, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 2)
        self.chk_ShowAccel = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_ShowAccel.setObjectName("chk_ShowAccel")
        self.gridLayout.addWidget(self.chk_ShowAccel, 11, 0, 1, 2, QtCore.Qt.AlignRight)
        self.lbl_MaxMinInfo = QtWidgets.QLabel(self.grp_Inputs)
        self.lbl_MaxMinInfo.setObjectName("lbl_MaxMinInfo")
        self.gridLayout.addWidget(self.lbl_MaxMinInfo, 14, 0, 1, 2, QtCore.Qt.AlignRight)
        self.lbl_RampANgle = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_RampANgle.sizePolicy().hasHeightForWidth())
        self.lbl_RampANgle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_RampANgle.setFont(font)
        self.lbl_RampANgle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_RampANgle.setObjectName("lbl_RampANgle")
        self.gridLayout.addWidget(self.lbl_RampANgle, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        self.le_k1 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_k1.sizePolicy().hasHeightForWidth())
        self.le_k1.setSizePolicy(sizePolicy)
        self.le_k1.setMinimumSize(QtCore.QSize(75, 0))
        self.le_k1.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_k1.setFont(font)
        self.le_k1.setObjectName("le_k1")
        self.gridLayout.addWidget(self.le_k1, 2, 1, 1, 1)
        self.le_m2 = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_m2.sizePolicy().hasHeightForWidth())
        self.le_m2.setSizePolicy(sizePolicy)
        self.le_m2.setMinimumSize(QtCore.QSize(75, 0))
        self.le_m2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_m2.setFont(font)
        self.le_m2.setObjectName("le_m2")
        self.gridLayout.addWidget(self.le_m2, 4, 1, 1, 1)
        self.le_ang = QtWidgets.QLineEdit(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_ang.sizePolicy().hasHeightForWidth())
        self.le_ang.setSizePolicy(sizePolicy)
        self.le_ang.setMinimumSize(QtCore.QSize(75, 0))
        self.le_ang.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_ang.setFont(font)
        self.le_ang.setObjectName("le_ang")
        self.gridLayout.addWidget(self.le_ang, 6, 1, 1, 1)
        self.layourhorizontal = QtWidgets.QHBoxLayout()
        self.layourhorizontal.setObjectName("layourhorizontal")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layourhorizontal.addItem(spacerItem1)
        self.chk_LogX = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_LogX.setObjectName("chk_LogX")
        self.layourhorizontal.addWidget(self.chk_LogX, 0, QtCore.Qt.AlignRight)
        self.chk_LogY = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_LogY.setObjectName("chk_LogY")
        self.layourhorizontal.addWidget(self.chk_LogY, 0, QtCore.Qt.AlignRight)
        self.chk_LogAccel = QtWidgets.QCheckBox(self.grp_Inputs)
        self.chk_LogAccel.setObjectName("chk_LogAccel")
        self.layourhorizontal.addWidget(self.chk_LogAccel, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.layourhorizontal, 9, 0, 1, 2)
        self.lbl_Dashpot = QtWidgets.QLabel(self.grp_Inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Dashpot.sizePolicy().hasHeightForWidth())
        self.lbl_Dashpot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Dashpot.setFont(font)
        self.lbl_Dashpot.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Dashpot.setObjectName("lbl_Dashpot")
        self.gridLayout.addWidget(self.lbl_Dashpot, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.grp_Inputs)
        self.layout_Plot = QtWidgets.QVBoxLayout()
        self.layout_Plot.setObjectName("layout_Plot")
        self.horizontalLayout.addLayout(self.layout_Plot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.grp_Inputs.setTitle(_translate("Form", "Model Inputs"))
        self.le_k2.setText(_translate("Form", "90000"))
        self.le_tmax.setText(_translate("Form", "3"))
        self.lbl_CarSpeed.setText(_translate("Form", "Car Speed (kph)"))
        self.lbl_m2.setText(_translate("Form", "Wheel mass (m2, kg)"))
        self.lbl_k2.setText(_translate("Form", "Tire spring constant (k2, N/m)"))
        self.lbl_Spring1.setText(_translate("Form", "Suspension Spring (k1, N/m)"))
        self.le_c1.setText(_translate("Form", "4500"))
        self.le_m1.setText(_translate("Form", "450"))
        self.lbl_tMax.setText(_translate("Form", "t, max plot (s)"))
        self.le_v.setText(_translate("Form", "120"))
        self.lbl_CarBodyMass.setText(_translate("Form", "Car body mass (m1, kg)"))
        self.chk_IncludeAccel.setText(_translate("Form", "Include Accel in Opt."))
        self.btn_calculate.setText(_translate("Form", "Calculate"))
        self.pb_Optimize.setText(_translate("Form", "Optimize Suspension"))
        self.chk_ShowAccel.setText(_translate("Form", "Plot Car Accel."))
        self.lbl_MaxMinInfo.setText(_translate("Form", "TextLabel"))
        self.lbl_RampANgle.setText(_translate("Form", "Ramp Angle (deg)"))
        self.le_k1.setText(_translate("Form", "15000"))
        self.le_m2.setText(_translate("Form", "20"))
        self.le_ang.setText(_translate("Form", "45"))
        self.chk_LogX.setText(_translate("Form", "log scale t"))
        self.chk_LogY.setText(_translate("Form", "log scale Y"))
        self.chk_LogAccel.setText(_translate("Form", "log scale Y\'\'"))
        self.lbl_Dashpot.setText(_translate("Form", "Suspension Shock Absorber (c1, N*s/m)"))


#region class definitions
#region specialized graphic items
class MassBlock(qtw.QGraphicsItem):
    def __init__(self, CenterX, CenterY, width=30, height=10, parent=None, pen=None, brush=None, name='CarBody', label=None, mass=10):
        super().__init__(parent)
        self.x = CenterX
        self.y = CenterY
        self.y0 = self.y
        self.pen = pen
        self.brush = brush
        self.width = width
        self.height = height
        self.top = self.y - self.height/2
        self.left = self.x - self.width/2
        self.rect = qtc.QRectF(self.left, self.top, self.width, self.height)
        self.name = name
        self.label = label
        self.mass = mass
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
        self.setToolTip(stTT)

    def setMass(self, mass=None):
        if mass is not None:
            self.mass=mass
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect

    def paint(self, painter, option, widget=None):
        self.transformation.reset()
        if self.pen is not None:
            painter.setPen(self.pen)  # Red color pen
        if self.brush is not None:
            painter.setBrush(self.brush)
        self.top = -self.height/2
        self.left = -self.width/2
        self.rect=qtc.QRectF( self.left, self.top, self.width, self.height)
        painter.drawRect(self.rect)
        font=painter.font()
        font.setPointSize(6)
        painter.setFont(font)
        text="mass = {:0.1f} kg".format(self.mass)
        fm = qtg.QFontMetrics(painter.font())
        painter.drawText(qtc.QPointF(-fm.width(text)/2.0,fm.height()/2.0), text)
        if self.label is not None:
            font.setPointSize(12)
            painter.setFont(font)
            painter.drawText(qtc.QPointF((self.width/2.0)+10,0), self.label)
        self.transformation.translate(self.x, self.y)
        self.setTransform(self.transformation)
        self.transformation.reset()
        # brPen=qtg.QPen()
        # brPen.setWidth(0)
        # painter.setPen(brPen)
        # painter.setBrush(qtc.Qt.NoBrush)
        # painter.drawRect(self.boundingRect())

class Wheel(qtw.QGraphicsItem):
    def __init__(self, CenterX, radius=10, roady=10, parent=None, penTire=None, penMass=None, brushWheel=None, brushMass=None, name='Wheel', mass=10):
        super().__init__(parent)
        self.x = CenterX
        self.road_y = roady
        self.radius = radius
        self.y = self.road_y-self.radius
        self.y0 = self.y
        self.penTire = penTire
        self.brushWheel = brushWheel
        self.penMass = penMass
        self.brushMass = brushMass
        self.rect = qtc.QRectF(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        self.name = name
        self.mass = mass
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
        self.setToolTip(stTT)
        self.massWidth=2*self.radius*0.85
        self.massHeight=self.radius/3
        self.massBlock = MassBlock(CenterX, self.y, width=self.massWidth, height=self.massHeight, pen=penMass, brush=brushMass, name="Wheel Mass", mass=mass)

    def setMass(self, mass=None):
        if mass is not None:
            self.mass=mass
            self.massBlock.setMass(mass)
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect
    def addToScene(self, scene):
        scene.addItem(self)
        scene.addItem(self.massBlock)

    def paint(self, painter, option, widget=None):
        height = 2*(self.road_y-self.y)
        width = 2*self.radius
        if self.penTire is not None:
            painter.setPen(self.penTire)  # Red color pen
        if self.brushWheel is not None:
            painter.setBrush(self.brushWheel)
        left = -width/2.0
        top = self.y-height/2
        self.rect=qtc.QRectF(left, top, width, height)
        painter.drawEllipse(self.rect)
        self.massBlock.y=self.y
        point = qtc.QPointF(self.radius*1.1, 0.0)
        painter.drawText(point, self.name)
class LinearSpring(qtw.QGraphicsItem):
    def __init__(self, ptSt, ptEn, coilsWidth=10, coilsLength=30, parent=None, pen=None, name='Spring', label=None, k=10, nCoils=6):
        """
        This is my class for a spring,
        :param ptSt: a QPointF point
        :param ptEn: a QPointF point
        :param coilsWidth: float for width of coils part
        :param coilsLength: float for free length of coils part
        :param parent:
        :param pen: for drawing the lines
        :param brush: not used for this one
        :param name: just a convenient name
        :param label: text to be displayed beside the spring
        :param k: the spring constant
        :param nCoils: number of coils to be drawn
        """
        super().__init__(parent)
        self.stPt = ptSt
        self.enPt = ptEn
        self.freeLength = self.getLength() # this assumes the spring to be free on initial definition
        self.DL = self.length-self.freeLength
        self.centerPt=(self.stPt+self.enPt)/2.0
        self.pen = pen
        self.coilsWidth = coilsWidth
        self.coilsLength = coilsLength
        self.top = - self.coilsLength / 2
        self.left = -self.coilsWidth / 2
        self.rect = qtc.QRectF(self.left, self.top, self.coilsWidth, self.coilsLength)
        self.name = name
        self.label = label
        self.k = k
        self.nCoils = nCoils
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.1f}, y={:0.1f}\nk = {:0.1f}".format(self.centerPt.x(), self.centerPt.y(), self.k)
        self.setToolTip(stTT)

    def setk(self, k=None):
        if k is not None:
            self.k=k
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nk = {:0.3f}".format(self.stPt.x(), self.stPt.y(), self.k)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect
    def getLength(self):
        p=self.enPt-self.stPt
        self.length = math.sqrt(p.x()**2+p.y()**2)
        return self.length

    def getDL(self):
        self.DL=self.length-self.freeLength
        return self.DL

    def getAngleDeg(self):
        p=self.enPt-self.stPt
        self.angleRad=math.atan2(p.y(), p.x())
        self.angleDeg=180.0/math.pi*self.angleRad
        return self.angleDeg

    def paint(self, painter, option, widget=None):
        """
        My method for drawing the spring is:
        Step 1:  compute the rectangle that will contain the coils section
            - call self.getLength()
            - call self.getDL() # note that self.DL < 0 for compression > 0 for tension
            - self.rect = qtc.QRectF(-(self.coilLength+self.DL)/2, -self.coilWidth/2, (self.coilLength+self.DL), self.coilWidth)
        Step 2: draw lines representing the coils
        Step 3: draw lines connecting (-self.length/2,0) to (self.rect.left,0) and (self.rect.right,0) to (self.length/2,0)
        Step 4: draw little circles at (-self.length/2,0) and (self.length/2,0)
        Step 5: translate by (self.length/2,0)
        Step 6: rotate to self.angleDeg
        Step 7: translate to stPt
        Step 8: decorate with text
        :param painter:
        :param option:
        :param widget:
        :return:
        """
        self.transformation.reset()

        if self.pen is not None:
            painter.setPen(self.pen)  # Red color pen
        #Step 1:
        self.getLength()
        self.getAngleDeg()
        self.getDL()
        ht = self.coilsWidth
        wd = self.coilsLength+self.DL
        top = -ht / 2
        left = -wd / 2
        right = wd / 2
        self.rect=qtc.QRectF(left, top, wd, ht)
        #painter.drawRect(self.rect)
        #Step 2:
        painter.drawLine(qtc.QPointF(left,0), qtc.QPointF(left, ht/2))
        dX=wd/(self.nCoils)
        for i in range(self.nCoils):
            painter.drawLine(qtc.QPointF(left + i * dX, ht / 2), qtc.QPointF(left + (i + 0.5) * dX, -ht / 2))
            painter.drawLine(qtc.QPointF(left + (i+0.5) * dX, -ht / 2), qtc.QPointF(left + (i + 1) * dX, ht / 2))
        painter.drawLine(qtc.QPointF(right, ht/2), qtc.QPointF(right,0))
        #Step 3:
        painter.drawLine(qtc.QPointF(-self.length/2,0),qtc.QPointF(left,0))
        painter.drawLine(qtc.QPointF(right,0),qtc.QPointF(self.length/2,0))
        #Step 4:
        nodeRad = 2
        stRec=qtc.QRectF(-self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        enRec=qtc.QRectF(self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        painter.drawEllipse(stRec)
        painter.drawEllipse(enRec)
        #Step 5:
        self.transformation.translate(self.stPt.x(), self.stPt.y())
        self.transformation.rotate(self.angleDeg)
        self.transformation.translate(self.length/2,0)
        self.setTransform(self.transformation)
        #Step 6:
        # self.transformation.reset()
        # font=painter.font()
        # font.setPointSize(6)
        # painter.setFont(font)
        # text="k = {:0.1f} N/m".format(self.k)
        # fm = qtg.QFontMetrics(painter.font())
        # centerPt = (self.stPt+self.enPt)/2,0
        # painter.drawText(qtc.QPointF(-fm.width(text)/2.0,fm.height()/2.0), text)
        # if self.label is not None:
        #     font.setPointSize(12)
        #     painter.setFont(font)
        #     painter.drawText(qtc.QPointF((self.coilsWidth / 2.0) + 10, 0), self.label)


        self.transformation.reset()
        # brPen=qtg.QPen()
        # brPen.setWidth(0)
        # painter.setPen(brPen)
        # painter.setBrush(qtc.Qt.NoBrush)
        # painter.drawRect(self.boundingRect())
class DashPot(qtw.QGraphicsItem):
    def __init__(self, ptSt, ptEn, dpWidth=10, dpLength=30, parent=None, pen=None, name='Dashpot', label=None, c=10):
        """
        This is my class for a dashpot,
        :param ptSt: a QPointF point
        :param ptEn: a QPointF point
        :param dpWidth: float for width of dashpot part
        :param dpLength: float for free length of dashpot part
        :param parent:
        :param pen: for drawing the lines
        :param brush: not used for this one
        :param name: just a convenient name
        :param label: text to be displayed beside the dashpot
        :param c: the dashpot coefficient
        """
        super().__init__(parent)
        self.stPt = ptSt
        self.enPt = ptEn
        self.freeLength = self.getLength() # this assumes the dashpot to be free on initial definition
        self.DL = self.length-self.freeLength
        self.centerPt=(self.stPt+self.enPt)/2.0
        self.pen = pen
        self.dpWidth = dpWidth
        self.dpLength = dpLength
        self.top = - self.dpLength / 2
        self.left = -self.dpWidth / 2
        self.rect = qtc.QRectF(self.left, self.top, self.dpWidth, self.dpLength)
        self.name = name
        self.label = label
        self.c = c
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.1f}, y={:0.1f}\nc = {:0.1f}".format(self.centerPt.x(), self.centerPt.y(), self.c)
        self.setToolTip(stTT)

    def setc(self, c=None):
        if c is not None:
            self.c=c
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nc = {:0.3f}".format(self.stPt.x(), self.stPt.y(), self.c)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect
    def getLength(self):
        p=self.enPt-self.stPt
        self.length = math.sqrt(p.x()**2+p.y()**2)
        return self.length

    def getDL(self):
        self.DL=self.length-self.freeLength
        return self.DL

    def getAngleDeg(self):
        p=self.enPt-self.stPt
        self.angleRad=math.atan2(p.y(), p.x())
        self.angleDeg=180.0/math.pi*self.angleRad
        return self.angleDeg

    def paint(self, painter, option, widget=None):
        """
        My method for drawing the spring is:
        Step 1:  compute the rectangle that will contain the dashpot section
            - call self.getLength()
            - call self.getDL() # note that self.DL < 0 for compression > 0 for tension
            - self.rect = qtc.QRectF(-(self.dpLength)/2, -self.dpWidth/2, (self.dpLength), self.dpWidth)
        Step 2: draw lines representing the dashpot
        Step 3: draw lines connecting (-self.length/2,0) to (self.rect.left,0) and (self.rect.right,0) to (self.length/2,0)
        Step 4: draw little circles at (-self.length/2,0) and (self.length/2,0)
        Step 5: translate by (self.length/2,0)
        Step 6: rotate to self.angleDeg
        Step 7: translate to stPt
        Step 8: decorate with text
        :param painter:
        :param option:
        :param widget:
        :return:
        """
        self.transformation.reset()

        if self.pen is not None:
            painter.setPen(self.pen)  # Red color pen
        #Step 1:
        self.getLength()
        self.getAngleDeg()
        self.getDL()
        ht = self.dpWidth
        wd = self.dpLength
        top = -ht / 2
        left = -wd / 2
        right = wd / 2
        self.rect=qtc.QRectF(left, top, wd, ht)
        #painter.drawRect(self.rect)
        #Step 2:
        painter.drawLine(qtc.QPointF(left,-ht/2), qtc.QPointF(left, ht/2))
        painter.drawLine(qtc.QPointF(left,-ht/2), qtc.QPointF(right, -ht/2))
        painter.drawLine(qtc.QPointF(left,ht/2), qtc.QPointF(right, ht/2))
        painter.drawLine(qtc.QPointF(self.DL, ht/2*0.95), qtc.QPointF(self.DL, -ht/2*0.95))
        #Step 3:
        painter.drawLine(qtc.QPointF(-self.length/2,0),qtc.QPointF(left,0))
        painter.drawLine(qtc.QPointF(self.DL,0),qtc.QPointF(self.length/2,0))
        #Step 4:
        nodeRad = 2
        stRec=qtc.QRectF(-self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        enRec=qtc.QRectF(self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        painter.drawEllipse(stRec)
        painter.drawEllipse(enRec)
        #Step 5:
        self.transformation.translate(self.stPt.x(), self.stPt.y())
        self.transformation.rotate(self.angleDeg)
        self.transformation.translate(self.length/2,0)
        self.setTransform(self.transformation)
        #Step 6:
        # self.transformation.reset()
        # font=painter.font()
        # font.setPointSize(6)
        # painter.setFont(font)
        # text="k = {:0.1f} N/m".format(self.k)
        # fm = qtg.QFontMetrics(painter.font())
        # centerPt = (self.stPt+self.enPt)/2,0
        # painter.drawText(qtc.QPointF(-fm.width(text)/2.0,fm.height()/2.0), text)
        # if self.label is not None:
        #     font.setPointSize(12)
        #     painter.setFont(font)
        #     painter.drawText(qtc.QPointF((self.dpWidth / 2.0) + 10, 0), self.label)


        self.transformation.reset()
        # brPen=qtg.QPen()
        # brPen.setWidth(0)
        # painter.setPen(brPen)
        # painter.setBrush(qtc.Qt.NoBrush)
        # painter.drawRect(self.boundingRect())
class Road(qtw.QGraphicsItem):
    def __init__(self, x,y, width=30, height=10, parent=None, pen=None, brush=None, name='Road', label=None):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.x0 = x
        self.y0 = y
        self.pen = pen
        self.brush = brush
        self.width = width
        self.height = height
        self.top = self.y - self.height/2
        self.left = self.x - self.width/2
        self.rect = qtc.QRectF(self.left, self.top, self.width, self.height)
        self.name = name
        self.label = label
        self.transformation = qtg.QTransform()

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect

    def paint(self, painter, option, widget=None):
        if self.pen is not None:
            painter.setPen(self.pen)
        if self.brush is not None:
            painter.setBrush(self.brush)
        self.top = self.y
        self.left = self.x-self.width/2
        self.right = self.x+self.width/2

        painter.drawLine(qtc.QPointF(self.left,self.top), qtc.QPointF(self.right,self.top))
        self.rect=qtc.QRectF( self.left, self.top, self.width, self.height)
        penOutline = qtg.QPen(qtc.Qt.NoPen)
        painter.setPen(penOutline)
        painter.setBrush(self.brush)
        painter.drawRect(self.rect)
#endregion

#region MVC for quarter car model
class CarModel():
    """
    I re-wrote the quarter car model as an object oriented program
    and used the MVC pattern.  This is the quarter car model.  It just
    stores information about the car and results of the ode calculation.
    """
    def __init__(self):
        """
        self.results to hold results of odeint solution
        self.t time vector for odeint and for plotting
        self.tramp is time required to climb the ramp
        self.angrad is the ramp angle in radians
        self.ymag is the ramp height in m
        """
        self.results = []
        self.roadPosData = []
        self.wheelPosData = []
        self.bodyPosData = []
        self.bodyAccelData = []
        self.tmax = 3.0  # limit of timespan for simulation in seconds
        self.timeData = np.linspace(0, self.tmax, 200)
        self.tramp = 1.0  # time to traverse the ramp in seconds
        self.angrad = 0.1
        self.ymag = 6.0 / (12 * 3.3)  # ramp height in meters.  default is 0.1515 m
        self.yangdeg = 45.0  # ramp angle in degrees.  default is 45
        self.results = None
        self.m1 = 450  # mass of car body in kg
        self.m2 = 20  # mass of wheel in kg
        self.c1 = 4500  # damping coefficient in N*s/m
        self.k1 = 15000  # spring constant of suspension in N/m
        self.k2 = 90000  # spring constant of tire in N/m
        self.v = 120.0  # velocity of car in kph
        #self.mink1=(self.m1*9.81)/(16.0*25.4/1000.0)
        self.mink1=(self.m1*9.81)/(6.0*25.4/1000.0)
        self.maxk1=(self.m1*9.81)/(3.0*25.4/1000.0)
        self.mink2=((self.m1+self.m2)*9.81)/(1.5*25.4/1000.0)
        self.maxk2=((self.m1+self.m2)*9.81)/(0.75*25.4/1000.0)
        self.accelBodyData=None
        self.accelMax=0
        self.accelLim=1.5
        self.SSE=0.0

class CarView():
    def __init__(self, args):
        self.input_widgets, self.display_widgets = args
        # unpack widgets with same names as they have on the GUI
        self.le_m1, self.le_v, self.le_k1, self.le_c1, self.le_m2, self.le_k2, self.le_ang, \
         self.le_tmax, self.chk_IncludeAccel = self.input_widgets

        self.gv_Schematic, self.chk_LogX, self.chk_LogY, self.chk_LogAccel, \
        self.chk_ShowAccel, self.lbl_MaxMinInfo, self.layout_Plot = self.display_widgets

        # creating a canvas to draw a figure for the car model
        self.figure = Figure(tight_layout=True, frameon=True, facecolor='none')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layout_Plot.addWidget(NavigationToolbar2QT(self.canvas))
        self.layout_Plot.addWidget(self.canvas)

        # axes for the plotting using view
        self.ax = self.figure.add_subplot()
        if self.ax is not None:
            self.ax1 = self.ax.twinx()
        self.interpolatorWheel=None
        self.interpolatorBody=None
        self.interpolatorAccel=None
        self.posWheelTracer=None
        self.posBodyTracer=None
        self.posRoadTracer=None
        self.accelTracer=None
        self.buildScene()

    def updateView(self, model=None):
        self.le_m1.setText("{:0.2f}".format(model.m1))
        self.le_k1.setText("{:0.2f}".format(model.k1))
        self.le_c1.setText("{:0.2f}".format(model.c1))
        self.le_m2.setText("{:0.2f}".format(model.m2))
        self.le_k2.setText("{:0.2f}".format(model.k2))
        self.le_ang.setText("{:0.2f}".format(model.yangdeg))
        self.le_tmax.setText("{:0.2f}".format(model.tmax))
        stTmp="k1_min = {:0.2f}, k1_max = {:0.2f}\nk2_min = {:0.2f}, k2_max = {:0.2f}\n".format(model.mink1, model.maxk1, model.mink2, model.maxk2)
        stTmp+="SSE = {:0.2f}".format(model.SSE)
        self.lbl_MaxMinInfo.setText(stTmp)
        self.CarBody.setMass(model.m1)
        self.Wheel.setMass(model.m2)
        self.spring1.setk(model.k1)
        self.spring2.setk(model.k2)
        self.dashpot.setc(model.c1)
        self.doPlot(model)

    def buildScene(self):
        #create a scene object
        self.scene = qtw.QGraphicsScene()
        self.scene.setObjectName("MyScene")
        self.scene.setSceneRect(-200, -200, 400, 400)  # xLeft, yTop, Width, Height

        #set the scene for the graphics view object
        self.gv_Schematic.setScene(self.scene)
        #make some pens and brushes for my drawing
        self.setupPensAndBrushes()
        #make the components
        self.Road = Road(0,100,300,10,pen=self.groundPen,brush=self.groundBrush)
        self.Wheel = Wheel(0,50, roady=self.Road.y, penTire=self.penTire, brushWheel=self.brushWheel, penMass=self.penMass, brushMass=self.brushMass, name = "Wheel")
        self.CarBody = MassBlock(0, -70, 100, 30, pen=self.penMass, brush=self.brushMass, name="Car Body", label='Car Body', mass=150)
        self.spring1 = LinearSpring(qtc.QPointF(-35.0, self.Wheel.y), qtc.QPointF(-35, self.CarBody.y), pen=self.penMass, name='k1', label='Spring 1', k=10)
        self.spring2 = LinearSpring(qtc.QPointF(self.Wheel.x, self.Wheel.y), qtc.QPointF(self.Wheel.x, self.Road.y), coilsWidth=10, coilsLength=20, nCoils=4, pen=self.penMass, name='k2', label='Spring 2', k=10)
        self.dashpot = DashPot(qtc.QPointF(-self.spring1.stPt.x(), self.spring1.stPt.y()),qtc.QPointF(-self.spring1.enPt.x(), self.spring1.enPt.y()), dpWidth=10, dpLength=30, pen=self.penMass, name='c', label='Dashpot', c=10)
        self.scene.addItem(self.Road)
        self.Wheel.addToScene(self.scene)
        self.scene.addItem(self.CarBody)
        self.scene.addItem(self.spring1)
        self.scene.addItem(self.spring2)
        self.scene.addItem(self.dashpot)

    def setupCanvasMoveEvent(self, window):
        self.canvas.mpl_connect("motion_notify_event", window.mouseMoveEvent_Canvas)

    def setupEventFilter(self, window):
        self.gv_Schematic.setMouseTracking(True)
        self.gv_Schematic.scene().installEventFilter(window)
    def getZoom(self):
        return self.gv_Schematic.transform().m11()

    def setZoom(self, val):
        self.gv_Schematic.resetTransform()
        self.gv_Schematic.scale(val,val)
    def updateSchematic(self):
        self.scene.update()

    def setupPensAndBrushes(self):
        """
        Just sets up pens and brushes for drawing the schematic.
        :return:
        """
        self.penTire = qtg.QPen(qtg.QColor(qtc.Qt.black))
        self.penTire.setWidth(3)
        self.penMass = qtg.QPen(qtg.QColor("black"))
        self.penMass.setWidth(1)
        color = qtg.QColor(qtc.Qt.gray)
        color.setAlpha(64)
        self.brushWheel = qtg.QBrush(color)
        self.brushMass = qtg.QBrush(qtg.QColor(200,200,200, 64))
        self.groundPen = qtg.QPen(qtg.QColor(qtc.Qt.black))
        self.groundPen.setWidth(1)
        self.groundBrush = qtg.QBrush(qtg.QColor(qtc.Qt.black))
        self.groundBrush.setStyle(qtc.Qt.DiagCrossPattern)

    def doPlot(self, model=None):
        """
        Creates the plot.
        :param model:
        :return:
        """
        if model.results is None:
            return
        ax = self.ax
        ax1 = self.ax1
        # plot result of odeint solver
        QTPlotting = True  # assumes we are plotting onto a QT GUI form
        if ax == None:
            ax = plt.subplot()
            ax1 = ax.twinx()
            QTPlotting = False  # actually, we are just using CLI and showing the plot
        ax.clear()
        ax1.clear()
        t = model.timeData
        ywheel = model.wheelPosData
        ycar = model.bodyPosData
        accel = model.accelBodyData

        if self.chk_LogX.isChecked():
            ax.set_xlim(0.001,model.tmax)
            ax.set_xscale('log')
        else:
            ax.set_xlim(0.0, model.tmax)
            ax.set_xscale('linear')

        if self.chk_LogY.isChecked():
            ax.set_ylim(0.0001,max(ycar.max(), ywheel.max()*1.05))
            ax.set_yscale('log')
        else:
            ax.set_ylim(0.0, max(ycar.max(), ywheel.max()*1.05))
            ax.set_yscale('linear')

        ax.plot(t, ycar, 'b-', label='Body Position')
        ax.plot(t, ywheel, 'r-', label='Wheel Position')
        ax.plot(t, model.roadPosData, 'k-', label='Road Position', linewidth=3.0)
        if self.chk_ShowAccel.isChecked():
            ax1.plot(t, accel, 'g-', label='Body Accel')
            ax1.axhline(y=accel.max(), color='orange')  # horizontal line at accel.max()
            ax1.set_yscale('log' if self.chk_LogAccel.isChecked() else 'linear')
            ax1.set_ylabel("Y'' (g)", fontsize = 'large' if QTPlotting else 'medium')
            ax1.yaxis.set_label_coords(1.05,.5)

        # add axis labels
        ax.set_ylabel("Vertical Position (m)", fontsize='large' if QTPlotting else 'medium')
        ax.set_xlabel("time (s)", fontsize='large' if QTPlotting else 'medium')
        ax.legend()

        ax.axvline(x=model.tramp)  # vertical line at tramp
        ax.axhline(y=model.ymag)  # horizontal line at ymag
        # modify the tick marks
        ax.tick_params(axis='both', which='both', direction='in', top=True,
                       labelsize='large' if QTPlotting else 'medium')  # format tick marks
        ax1.tick_params(axis='both', which='both', direction='in', right=True,
                       labelsize='large' if QTPlotting else 'medium')  # format tick marks
        # show the plot
        if QTPlotting == False:
            plt.show()
        else:
            self.canvas.draw()

    def getPoints(self, model=None, t=0):
        """
        This gets interpolated values from the model data at a given time.
        :param model:
        :param t:
        :return: ywheel, ybody, yroad, accel
        """
        if model is None: return 0,0,0
        ywheel=np.interp(t, model.timeData, model.wheelPosData)
        ybody=np.interp(t, model.timeData, model.bodyPosData)
        yroad=np.interp(t,model.timeData, model.roadPosData)
        accel=np.interp(t, model.timeData, model.accelBodyData)
        return ywheel,ybody, yroad ,accel

    def animate(self, model=None, t=0):
        """
        Here I am interpolating the model data at time t and updating the vertical positions of the wheel and the car
        body.  The compression of the spring(s) occurs if I change their end point locations to something other
        than their free length which is established when they are first define.  Any change in the end point coordinates
        causes the active part of the spring to shorten/lengthen.  I could calculate the force of the spring by:
        F=k*deltaY.

        Similar idea for the dashpote.  Although in the case of the dashpot, it is the relative velocity difference
        between the end points that causes the force.
        :param model:
        :param t:
        :return:
        """
        if model is None: return
        ywheel, ybody, yroad, accel=self.getPoints(model, t)
        try:
            if self.posWheelTracer is not None:
                self.posWheelTracer.remove()
            if self.posBodyTracer is not None:
                self.posBodyTracer.remove()
            if self.posRoadTracer is not None:
                self.posRoadTracer.remove()
            if self.accelTracer is not None:
                self.accelTracer.remove()
        finally:
            pass
        # I'll assume a tire of size P275/55R20
        # This means the tire width is 275 mm -> 10.83 in
        # The height of the sidewall is:  0.55*10.85 = 5.95 in
        # The wheel diameter is 20 in
        # Therefore the tire diameter is 31.9 in
        # The Wheel radius is set to 100.  Hence scale is:  s*31.9(in)*[25.4(mm)/(in)]*[(m)/1000(mm)] = 200 => s=246.83/(m)
        self.scale  = 200*(1000/25.4)/self.Wheel.radius
        self.posWheelTracer=self.ax.plot(t, ywheel, 'o', markeredgecolor='red', markerfacecolor='none')[0]
        self.posBodyTracer=self.ax.plot(t, ybody, 'o', markeredgecolor='blue', markerfacecolor='none')[0]
        self.posRoadTracer=self.ax.plot(t, yroad, 'o', markeredgecolor='black', markerfacecolor='none')[0]
        self.Road.y=self.Road.y0-yroad*self.scale
        self.Wheel.road_y = self.Road.y
        self.Wheel.y=self.Wheel.y0-ywheel*self.scale
        self.spring2.enPt.setY(self.Road.y)
        self.spring2.stPt.setY(self.Wheel.y)
        self.CarBody.y=self.CarBody.y0-ybody*self.scale
        self.spring1.stPt.setY(self.Wheel.y)
        self.spring1.enPt.setY(self.CarBody.y)
        self.dashpot.stPt.setY(self.Wheel.y)
        self.dashpot.enPt.setY(self.CarBody.y)
        if self.chk_ShowAccel.isChecked():
            self.accelTracer=self.ax1.plot(t,accel,'o', markeredgecolor='green', markerfacecolor='none')[0]
        self.canvas.draw()
        self.scene.update()

class CarController():
    def __init__(self, args):
        """
        This is the controller I am using for the quarter car model.
        """
        self.input_widgets, self.display_widgets = args
        #unpack widgets with same names as they have on the GUI
        self.le_m1, self.le_v, self.le_k1, self.le_c1, self.le_m2, self.le_k2, self.le_ang, \
         self.le_tmax, self.chk_IncludeAccel = self.input_widgets

        self.gv_Schematic, self.chk_LogX, self.chk_LogY, self.chk_LogAccel, \
        self.chk_ShowAccel, self.lbl_MaxMinInfo, self.layout_horizontal_main = self.display_widgets

        self.model = CarModel()
        self.view = CarView(args)

    def ode_system(self, t ,X):
        # define the forcing function equation for the linear ramp
        # It takes self.tramp time to climb the ramp, so y position is
        # a linear function of time.
        if t < self.model.tramp:
            y = self.model.ymag * (t / self.model.tramp)
        else:
            y = self.model.ymag

        x1 = X[0]  # car position in vertical direction
        x1dot = X[1]  # car velocity  in vertical direction
        x2 = X[2]  # wheel position in vertical direction
        x2dot = X[3]  # wheel velocity in vertical direction

        # write the non-trivial equations in vertical direction
        x1ddot = (1 / self.model.m1) * (self.model.c1 * (x2dot - x1dot) + self.model.k1 * (x2 - x1))
        x2ddot = (1 / self.model.m2) * (
                    -self.model.c1 * (x2dot - x1dot) - self.model.k1 * (x2 - x1) + self.model.k2 * (y - x2))
        self.step += 1
        # return the derivatives of the input state vector
        return [x1dot, x1ddot, x2dot, x2ddot]

    def calculate(self, doCalc=True):
        """
        I will first set the basic properties of the car model and then calculate the result
        in another function doCalc.
        """
        #Step 1.  Read from the widgets
        self.model.m1 = float(self.le_m1.text())
        self.model.m2 = float(self.le_m2.text())
        self.model.c1 = float(self.le_c1.text())
        self.model.k1 = float(self.le_k1.text())
        self.model.k2 = float(self.le_k2.text())
        self.model.v = float(self.le_v.text())

        #recalculate min and max k values
        self.mink1=(self.model.m1*9.81)/(6.0*25.4/1000.0)
        self.maxk1=(self.model.m1*9.81)/(3.0*25.4/1000.0)
        self.mink2=((self.model.m1+self.model.m2)*9.81)/(1.5*25.4/1000.0)
        self.maxk2=((self.model.m1+self.model.m2)*9.81)/(0.75*25.4/1000.0)

        ymag=6.0/(12.0*3.3)   #This is the height of the ramp in m
        if ymag is not None:
            self.model.ymag = ymag
        self.model.yangdeg = float(self.le_ang.text())
        self.model.tmax = float(self.le_tmax.text())
        if(doCalc):
            self.doCalc()
        self.SSE((self.model.k1, self.model.c1, self.model.k2), optimizing=False)
        self.view.updateView(self.model)

    def setWidgets(self, w):
        """
        Pass widgets to view for setup.
        :param w:
        :return:
        """
        self.view.setWidgets(w)
        self.chk_IncludeAccel=self.view.chk_IncludeAccel

    def setupCanvasMoveEvent(self, window):
        """
        Pass through to view.
        :param window:
        :return:
        """
        self.view.setupCanvasMoveEvent(window)

    def setupEventFilter(self, window):
        self.view.setupEventFilter(window=window)
    def getZoom(self):
        """
        Pass request along to the view.
        :return:
        """
        return self.view.getZoom()

    def setZoom(self,val):
        """
        Pass request along to the view.
        :param val:
        :return:
        """
        self.view.setZoom(val=val)

    def updateSchematic(self):
        """
        Pass request along to the view.
        :return:
        """
        self.view.updateSchematic()

    def doCalc(self, doPlot=True, doAccel=True):
        """
        This solves the differential equations for the quarter car model.
        :param doPlot:
        :param doAccel:
        :return:
        """
        v = 1000 * self.model.v / 3600  # convert speed to m/s from kph
        self.model.angrad = self.model.yangdeg * math.pi / 180.0  # convert angle to radians
        self.model.tramp = self.model.ymag / (math.sin(self.model.angrad) * v)  # calculate time to traverse ramp

        self.model.timeData=np.logspace(np.log10(0.000001), np.log10(self.model.tmax), 2000)
        #self.model.timeData=np.linspace(0, self.model.tmax, 2000)
        self.model.roadPosData=[self.model.ymag if t>self.model.tramp else t*self.model.ymag/self.model.tramp for t in self.model.timeData]
        ic = [0, 0, 0, 0]
        # run odeint solver
        self.step=0
        self.model.results = solve_ivp(self.ode_system, t_span=[0,self.model.tmax], y0=ic, t_eval=self.model.timeData)
        if doAccel:
            self.calcAccel()
        if doPlot:
            self.doPlot()
        self.model.bodyPosData = self.model.results.y[0]
        self.model.wheelPosData = self.model.results.y[2]
        pass

    def calcAccel(self):
        """
        Calculate the acceleration in the vertical direction using the forward difference formula.
        """
        N=len(self.model.timeData)
        self.model.accelBodyData=np.zeros(shape=N)
        vel=self.model.results.y[1]
        for i in range(N):
            if i==N-1:
                h = self.model.timeData[i] - self.model.timeData[i - 1]
                self.model.accelBodyData[i]= (vel[i] - vel[i - 1]) / (9.81 * h)  # backward difference of velocity
            else:
                h = self.model.timeData[i + 1] - self.model.timeData[i]
                self.model.accelBodyData[i] = (vel[i + 1] - vel[i]) / (9.81 * h)  # forward difference of velocity
            # else:
            #     self.model.accel[i]=(vel[i+1]-vel[i-1])/(9.81*2.0*h)  # central difference of velocity
        self.model.accelMax=self.model.accelBodyData.max()
        return True

    def OptimizeSuspension(self):
        """
        Step 1:  set parameters based on GUI inputs by calling self.set(doCalc=False)
        Step 2:  make an initial guess for k1, c1, k2
        Step 3:  optimize the suspension
        :return:
        """
        #Step 1:
        #$JES MISSING CODE HERE$
        self.calculate(doCalc=False)
        #Step 2:
        #JES MISSING CODE HERE$
        x0=np.array([(self.model.mink1)*1.1, self.model.c1, (self.model.mink2)*1.1])
        #Step 3:
        #JES MISSING CODE HERE$
        answer=minimize(self.SSE,x0,method='Nelder-Mead')
        self.view.updateView(self.model)

    def SSE(self, vals, optimizing=True):
        """
        Calculates the sum of square errors between the contour of the road and the car body.
        :param vals:
        :param optimizing:
        :return:
        """
        k1, c1, k2=vals  #unpack the new values for k1, c1, k2
        self.model.k1=k1
        self.model.c1=c1
        self.model.k2=k2
        self.doCalc(doPlot=False)  #solve the odesystem with the new values of k1, c1, k2
        SSE=0
        for i in range(len(self.model.results.y[0])):
            t=self.model.timeData[i]
            y=self.model.results.y[0][i]
            if t < self.model.tramp:
                ytarget = self.model.ymag * (t / self.model.tramp)
            else:
                ytarget = self.model.ymag
            SSE+=(y-ytarget)**2

        #some penalty functions if the constants are too small
        if optimizing:
            if k1<self.model.mink1 or k1>self.model.maxk1:
                SSE+=100
            if c1<10:
                SSE+=100
            if k2<self.model.mink2 or k2>self.model.maxk2:
                SSE+=100
            o_IncludeAccel = self.chk_IncludeAccel.isChecked()
            # I'm overlaying a gradient in the acceleration limit that scales with distance from a target squared.
            if self.model.accelMax > self.model.accelLim and o_IncludeAccel:
                # need to soften suspension
                SSE+=10+10*(self.model.accelMax-self.model.accelLim)**2
        self.model.SSE=SSE
        return SSE

    def doPlot(self):
        self.view.doPlot(self.model)

    def animate(self, t):
        self.view.animate(self.model,t)

    def getPoints(self, t):
        return self.view.getPoints(self.model, t)
#endregion
#endregion

def main():
    QCM = CarController()
    QCM.doCalc()


#endregion

class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self):
        """
        Main window constructor.
        """
        super().__init__()
        #call setupUi feom Ui_Form parent
        self.setupUi(self)

        #setup car controller
        input_widgets = (self.le_m1, self.le_v, self.le_k1, self.le_c1, self.le_m2, self.le_k2, self.le_ang, \
                         self.le_tmax, self.chk_IncludeAccel)
        display_widgets = (self.gv_Schematic, self.chk_LogX, self.chk_LogY, self.chk_LogAccel, \
        self.chk_ShowAccel, self.lbl_MaxMinInfo, self.layout_Plot)

        #instantiate the car controller
        self.controller = CarController((input_widgets, display_widgets))

        # connect signal to slots
        self.btn_calculate.clicked.connect(self.controller.calculate)
        self.pb_Optimize.clicked.connect(self.doOptimize)
        self.chk_LogX.stateChanged.connect(self.controller.doPlot)
        self.chk_LogY.stateChanged.connect(self.controller.doPlot)
        self.chk_LogAccel.stateChanged.connect(self.controller.doPlot)
        self.chk_ShowAccel.stateChanged.connect(self.controller.doPlot)
        self.controller.setupEventFilter(self)
        self.controller.setupCanvasMoveEvent(self)
        self.show()

    def eventFilter(self, obj, event):
        """
        This overrides the default eventFilter of the widget.  It takes action on events and then passes the event
        along to the parent widget.
        :param obj: The object on which the event happened
        :param event: The event itself
        :return: boolean from the parent widget
        """
        if obj == self.gv_Schematic.scene():
            et = event.type()
            if et == qtc.QEvent.GraphicsSceneMouseMove:
                scenePos = event.scenePos()
                strScene = "Mouse Position:  x = {}, y = {}".format(round(scenePos.x(), 2), round(-scenePos.y(), 2))
                self.setWindowTitle(strScene)  # display information in a label
            if event.type() == qtc.QEvent.GraphicsSceneWheel:  # I added this to zoom on mouse wheel scroll
                zm=self.controller.getZoom()
                if event.delta() > 0:
                    zm+=0.1
                else:
                    zm-=0.1
                zm=max(0.1,zm)
                self.controller.setZoom(zm)
        self.controller.updateSchematic()

        # pass the event along to the parent widget if there is one.
        return super(MainWindow, self).eventFilter(obj, event)

    def mouseMoveEvent_Canvas(self, event):
        if event.inaxes:
            self.controller.animate(event.xdata)
            ywheel,ybody, yroad, accel = self.controller.getPoints(event.xdata)
            self.setWindowTitle('t={:0.2f}(ms), y-road:{:0.3f}(mm), y-wheel:{:0.2f}(mm) , y-car:{:0.2f}(mm), accel={:0.2f}(g) '.format(event.xdata, yroad*1000, ywheel*1000, ybody*1000, accel))

    def doOptimize(self):
        app.setOverrideCursor(qtc.Qt.WaitCursor)
        self.controller.OptimizeSuspension()
        app.restoreOverrideCursor()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Quarter Car Model')
    sys.exit(app.exec())
#region imports

#region class definitions
#region specialized graphic items
class MassBlock(qtw.QGraphicsItem):
    def __init__(self, CenterX, CenterY, width=30, height=10, parent=None, pen=None, brush=None, name='CarBody', label=None, mass=10):
        super().__init__(parent)
        self.x = CenterX
        self.y = CenterY
        self.y0 = self.y
        self.pen = pen
        self.brush = brush
        self.width = width
        self.height = height
        self.top = self.y - self.height/2
        self.left = self.x - self.width/2
        self.rect = qtc.QRectF(self.left, self.top, self.width, self.height)
        self.name = name
        self.label = label
        self.mass = mass
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
        self.setToolTip(stTT)

    def setMass(self, mass=None):
        if mass is not None:
            self.mass=mass
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect

    def paint(self, painter, option, widget=None):
        self.transformation.reset()
        if self.pen is not None:
            painter.setPen(self.pen)  # Red color pen
        if self.brush is not None:
            painter.setBrush(self.brush)
        self.top = -self.height/2
        self.left = -self.width/2
        self.rect=qtc.QRectF( self.left, self.top, self.width, self.height)
        painter.drawRect(self.rect)
        font=painter.font()
        font.setPointSize(6)
        painter.setFont(font)
        text="mass = {:0.1f} kg".format(self.mass)
        fm = qtg.QFontMetrics(painter.font())
        painter.drawText(qtc.QPointF(-fm.width(text)/2.0,fm.height()/2.0), text)
        if self.label is not None:
            font.setPointSize(12)
            painter.setFont(font)
            painter.drawText(qtc.QPointF((self.width/2.0)+10,0), self.label)
        self.transformation.translate(self.x, self.y)
        self.setTransform(self.transformation)
        self.transformation.reset()
        # brPen=qtg.QPen()
        # brPen.setWidth(0)
        # painter.setPen(brPen)
        # painter.setBrush(qtc.Qt.NoBrush)
        # painter.drawRect(self.boundingRect())

class Wheel(qtw.QGraphicsItem):
    def __init__(self, CenterX, radius=10, roady=10, parent=None, penTire=None, penMass=None, brushWheel=None, brushMass=None, name='Wheel', mass=10):
        super().__init__(parent)
        self.x = CenterX
        self.road_y = roady
        self.radius = radius
        self.y = self.road_y-self.radius
        self.y0 = self.y
        self.penTire = penTire
        self.brushWheel = brushWheel
        self.penMass = penMass
        self.brushMass = brushMass
        self.rect = qtc.QRectF(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        self.name = name
        self.mass = mass
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
        self.setToolTip(stTT)
        self.massWidth=2*self.radius*0.85
        self.massHeight=self.radius/3
        self.massBlock = MassBlock(CenterX, self.y, width=self.massWidth, height=self.massHeight, pen=penMass, brush=brushMass, name="Wheel Mass", mass=mass)

    def setMass(self, mass=None):
        if mass is not None:
            self.mass=mass
            self.massBlock.setMass(mass)
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nmass = {:0.3f}".format(self.x, self.y, self.mass)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect
    def addToScene(self, scene):
        scene.addItem(self)
        scene.addItem(self.massBlock)

    def paint(self, painter, option, widget=None):
        height = 2*(self.road_y-self.y)
        width = 2*self.radius
        if self.penTire is not None:
            painter.setPen(self.penTire)  # Red color pen
        if self.brushWheel is not None:
            painter.setBrush(self.brushWheel)
        left = -width/2.0
        top = self.y-height/2
        self.rect=qtc.QRectF(left, top, width, height)
        painter.drawEllipse(self.rect)
        self.massBlock.y=self.y
        point = qtc.QPointF(self.radius*1.1, 0.0)
        painter.drawText(point, self.name)
class LinearSpring(qtw.QGraphicsItem):
    def __init__(self, ptSt, ptEn, coilsWidth=10, coilsLength=30, parent=None, pen=None, name='Spring', label=None, k=10, nCoils=6):
        """
        This is my class for a spring,
        :param ptSt: a QPointF point
        :param ptEn: a QPointF point
        :param coilsWidth: float for width of coils part
        :param coilsLength: float for free length of coils part
        :param parent:
        :param pen: for drawing the lines
        :param brush: not used for this one
        :param name: just a convenient name
        :param label: text to be displayed beside the spring
        :param k: the spring constant
        :param nCoils: number of coils to be drawn
        """
        super().__init__(parent)
        self.stPt = ptSt
        self.enPt = ptEn
        self.freeLength = self.getLength() # this assumes the spring to be free on initial definition
        self.DL = self.length-self.freeLength
        self.centerPt=(self.stPt+self.enPt)/2.0
        self.pen = pen
        self.coilsWidth = coilsWidth
        self.coilsLength = coilsLength
        self.top = - self.coilsLength / 2
        self.left = -self.coilsWidth / 2
        self.rect = qtc.QRectF(self.left, self.top, self.coilsWidth, self.coilsLength)
        self.name = name
        self.label = label
        self.k = k
        self.nCoils = nCoils
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.1f}, y={:0.1f}\nk = {:0.1f}".format(self.centerPt.x(), self.centerPt.y(), self.k)
        self.setToolTip(stTT)

    def setk(self, k=None):
        if k is not None:
            self.k=k
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nk = {:0.3f}".format(self.stPt.x(), self.stPt.y(), self.k)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect
    def getLength(self):
        p=self.enPt-self.stPt
        self.length = math.sqrt(p.x()**2+p.y()**2)
        return self.length

    def getDL(self):
        self.DL=self.length-self.freeLength
        return self.DL

    def getAngleDeg(self):
        p=self.enPt-self.stPt
        self.angleRad=math.atan2(p.y(), p.x())
        self.angleDeg=180.0/math.pi*self.angleRad
        return self.angleDeg

    def paint(self, painter, option, widget=None):
        """
        My method for drawing the spring is:
        Step 1:  compute the rectangle that will contain the coils section
            - call self.getLength()
            - call self.getDL() # note that self.DL < 0 for compression > 0 for tension
            - self.rect = qtc.QRectF(-(self.coilLength+self.DL)/2, -self.coilWidth/2, (self.coilLength+self.DL), self.coilWidth)
        Step 2: draw lines representing the coils
        Step 3: draw lines connecting (-self.length/2,0) to (self.rect.left,0) and (self.rect.right,0) to (self.length/2,0)
        Step 4: draw little circles at (-self.length/2,0) and (self.length/2,0)
        Step 5: translate by (self.length/2,0)
        Step 6: rotate to self.angleDeg
        Step 7: translate to stPt
        Step 8: decorate with text
        :param painter:
        :param option:
        :param widget:
        :return:
        """
        self.transformation.reset()

        if self.pen is not None:
            painter.setPen(self.pen)  # Red color pen
        #Step 1:
        self.getLength()
        self.getAngleDeg()
        self.getDL()
        ht = self.coilsWidth
        wd = self.coilsLength+self.DL
        top = -ht / 2
        left = -wd / 2
        right = wd / 2
        self.rect=qtc.QRectF(left, top, wd, ht)
        #painter.drawRect(self.rect)
        #Step 2:
        painter.drawLine(qtc.QPointF(left,0), qtc.QPointF(left, ht/2))
        dX=wd/(self.nCoils)
        for i in range(self.nCoils):
            painter.drawLine(qtc.QPointF(left + i * dX, ht / 2), qtc.QPointF(left + (i + 0.5) * dX, -ht / 2))
            painter.drawLine(qtc.QPointF(left + (i+0.5) * dX, -ht / 2), qtc.QPointF(left + (i + 1) * dX, ht / 2))
        painter.drawLine(qtc.QPointF(right, ht/2), qtc.QPointF(right,0))
        #Step 3:
        painter.drawLine(qtc.QPointF(-self.length/2,0),qtc.QPointF(left,0))
        painter.drawLine(qtc.QPointF(right,0),qtc.QPointF(self.length/2,0))
        #Step 4:
        nodeRad = 2
        stRec=qtc.QRectF(-self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        enRec=qtc.QRectF(self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        painter.drawEllipse(stRec)
        painter.drawEllipse(enRec)
        #Step 5:
        self.transformation.translate(self.stPt.x(), self.stPt.y())
        self.transformation.rotate(self.angleDeg)
        self.transformation.translate(self.length/2,0)
        self.setTransform(self.transformation)
        #Step 6:
        # self.transformation.reset()
        # font=painter.font()
        # font.setPointSize(6)
        # painter.setFont(font)
        # text="k = {:0.1f} N/m".format(self.k)
        # fm = qtg.QFontMetrics(painter.font())
        # centerPt = (self.stPt+self.enPt)/2,0
        # painter.drawText(qtc.QPointF(-fm.width(text)/2.0,fm.height()/2.0), text)
        # if self.label is not None:
        #     font.setPointSize(12)
        #     painter.setFont(font)
        #     painter.drawText(qtc.QPointF((self.coilsWidth / 2.0) + 10, 0), self.label)


        self.transformation.reset()
        # brPen=qtg.QPen()
        # brPen.setWidth(0)
        # painter.setPen(brPen)
        # painter.setBrush(qtc.Qt.NoBrush)
        # painter.drawRect(self.boundingRect())
class DashPot(qtw.QGraphicsItem):
    def __init__(self, ptSt, ptEn, dpWidth=10, dpLength=30, parent=None, pen=None, name='Dashpot', label=None, c=10):
        """
        This is my class for a dashpot,
        :param ptSt: a QPointF point
        :param ptEn: a QPointF point
        :param dpWidth: float for width of dashpot part
        :param dpLength: float for free length of dashpot part
        :param parent:
        :param pen: for drawing the lines
        :param brush: not used for this one
        :param name: just a convenient name
        :param label: text to be displayed beside the dashpot
        :param c: the dashpot coefficient
        """
        super().__init__(parent)
        self.stPt = ptSt
        self.enPt = ptEn
        self.freeLength = self.getLength() # this assumes the dashpot to be free on initial definition
        self.DL = self.length-self.freeLength
        self.centerPt=(self.stPt+self.enPt)/2.0
        self.pen = pen
        self.dpWidth = dpWidth
        self.dpLength = dpLength
        self.top = - self.dpLength / 2
        self.left = -self.dpWidth / 2
        self.rect = qtc.QRectF(self.left, self.top, self.dpWidth, self.dpLength)
        self.name = name
        self.label = label
        self.c = c
        self.transformation = qtg.QTransform()
        stTT = self.name +"\nx={:0.1f}, y={:0.1f}\nc = {:0.1f}".format(self.centerPt.x(), self.centerPt.y(), self.c)
        self.setToolTip(stTT)

    def setc(self, c=None):
        if c is not None:
            self.c=c
            stTT = self.name + "\nx={:0.3f}, y={:0.3f}\nc = {:0.3f}".format(self.stPt.x(), self.stPt.y(), self.c)
            self.setToolTip(stTT)

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect
    def getLength(self):
        p=self.enPt-self.stPt
        self.length = math.sqrt(p.x()**2+p.y()**2)
        return self.length

    def getDL(self):
        self.DL=self.length-self.freeLength
        return self.DL

    def getAngleDeg(self):
        p=self.enPt-self.stPt
        self.angleRad=math.atan2(p.y(), p.x())
        self.angleDeg=180.0/math.pi*self.angleRad
        return self.angleDeg

    def paint(self, painter, option, widget=None):
        """
        My method for drawing the spring is:
        Step 1:  compute the rectangle that will contain the dashpot section
            - call self.getLength()
            - call self.getDL() # note that self.DL < 0 for compression > 0 for tension
            - self.rect = qtc.QRectF(-(self.dpLength)/2, -self.dpWidth/2, (self.dpLength), self.dpWidth)
        Step 2: draw lines representing the dashpot
        Step 3: draw lines connecting (-self.length/2,0) to (self.rect.left,0) and (self.rect.right,0) to (self.length/2,0)
        Step 4: draw little circles at (-self.length/2,0) and (self.length/2,0)
        Step 5: translate by (self.length/2,0)
        Step 6: rotate to self.angleDeg
        Step 7: translate to stPt
        Step 8: decorate with text
        :param painter:
        :param option:
        :param widget:
        :return:
        """
        self.transformation.reset()

        if self.pen is not None:
            painter.setPen(self.pen)  # Red color pen
        #Step 1:
        self.getLength()
        self.getAngleDeg()
        self.getDL()
        ht = self.dpWidth
        wd = self.dpLength
        top = -ht / 2
        left = -wd / 2
        right = wd / 2
        self.rect=qtc.QRectF(left, top, wd, ht)
        #painter.drawRect(self.rect)
        #Step 2:
        painter.drawLine(qtc.QPointF(left,-ht/2), qtc.QPointF(left, ht/2))
        painter.drawLine(qtc.QPointF(left,-ht/2), qtc.QPointF(right, -ht/2))
        painter.drawLine(qtc.QPointF(left,ht/2), qtc.QPointF(right, ht/2))
        painter.drawLine(qtc.QPointF(self.DL, ht/2*0.95), qtc.QPointF(self.DL, -ht/2*0.95))
        #Step 3:
        painter.drawLine(qtc.QPointF(-self.length/2,0),qtc.QPointF(left,0))
        painter.drawLine(qtc.QPointF(self.DL,0),qtc.QPointF(self.length/2,0))
        #Step 4:
        nodeRad = 2
        stRec=qtc.QRectF(-self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        enRec=qtc.QRectF(self.length/2-nodeRad, -nodeRad, 2*nodeRad, 2* nodeRad)
        painter.drawEllipse(stRec)
        painter.drawEllipse(enRec)
        #Step 5:
        self.transformation.translate(self.stPt.x(), self.stPt.y())
        self.transformation.rotate(self.angleDeg)
        self.transformation.translate(self.length/2,0)
        self.setTransform(self.transformation)
        #Step 6:
        # self.transformation.reset()
        # font=painter.font()
        # font.setPointSize(6)
        # painter.setFont(font)
        # text="k = {:0.1f} N/m".format(self.k)
        # fm = qtg.QFontMetrics(painter.font())
        # centerPt = (self.stPt+self.enPt)/2,0
        # painter.drawText(qtc.QPointF(-fm.width(text)/2.0,fm.height()/2.0), text)
        # if self.label is not None:
        #     font.setPointSize(12)
        #     painter.setFont(font)
        #     painter.drawText(qtc.QPointF((self.dpWidth / 2.0) + 10, 0), self.label)


        self.transformation.reset()
        # brPen=qtg.QPen()
        # brPen.setWidth(0)
        # painter.setPen(brPen)
        # painter.setBrush(qtc.Qt.NoBrush)
        # painter.drawRect(self.boundingRect())
class Road(qtw.QGraphicsItem):
    def __init__(self, x,y, width=30, height=10, parent=None, pen=None, brush=None, name='Road', label=None):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.x0 = x
        self.y0 = y
        self.pen = pen
        self.brush = brush
        self.width = width
        self.height = height
        self.top = self.y - self.height/2
        self.left = self.x - self.width/2
        self.rect = qtc.QRectF(self.left, self.top, self.width, self.height)
        self.name = name
        self.label = label
        self.transformation = qtg.QTransform()

    def boundingRect(self):
        bounding_rect = self.transformation.mapRect(self.rect)
        return bounding_rect

    def paint(self, painter, option, widget=None):
        if self.pen is not None:
            painter.setPen(self.pen)
        if self.brush is not None:
            painter.setBrush(self.brush)
        self.top = self.y
        self.left = self.x-self.width/2
        self.right = self.x+self.width/2

        painter.drawLine(qtc.QPointF(self.left,self.top), qtc.QPointF(self.right,self.top))
        self.rect=qtc.QRectF( self.left, self.top, self.width, self.height)
        penOutline = qtg.QPen(qtc.Qt.NoPen)
        painter.setPen(penOutline)
        painter.setBrush(self.brush)
        painter.drawRect(self.rect)
#endregion

#region MVC for quarter car model
class CarModel():
    """
    I re-wrote the quarter car model as an object oriented program
    and used the MVC pattern.  This is the quarter car model.  It just
    stores information about the car and results of the ode calculation.
    """
    def __init__(self):
        """
        self.results to hold results of odeint solution
        self.t time vector for odeint and for plotting
        self.tramp is time required to climb the ramp
        self.angrad is the ramp angle in radians
        self.ymag is the ramp height in m
        """
        self.results = []
        self.roadPosData = []
        self.wheelPosData = []
        self.bodyPosData = []
        self.bodyAccelData = []
        self.tmax = 3.0  # limit of timespan for simulation in seconds
        self.timeData = np.linspace(0, self.tmax, 200)
        self.tramp = 1.0  # time to traverse the ramp in seconds
        self.angrad = 0.1
        self.ymag = 6.0 / (12 * 3.3)  # ramp height in meters.  default is 0.1515 m
        self.yangdeg = 45.0  # ramp angle in degrees.  default is 45
        self.results = None
        self.m1 = 450  # mass of car body in kg
        self.m2 = 20  # mass of wheel in kg
        self.c1 = 4500  # damping coefficient in N*s/m
        self.k1 = 15000  # spring constant of suspension in N/m
        self.k2 = 90000  # spring constant of tire in N/m
        self.v = 120.0  # velocity of car in kph
        #self.mink1=(self.m1*9.81)/(16.0*25.4/1000.0)
        self.mink1=(self.m1*9.81)/(6.0*25.4/1000.0)
        self.maxk1=(self.m1*9.81)/(3.0*25.4/1000.0)
        self.mink2=((self.m1+self.m2)*9.81)/(1.5*25.4/1000.0)
        self.maxk2=((self.m1+self.m2)*9.81)/(0.75*25.4/1000.0)
        self.accelBodyData=None
        self.accelMax=0
        self.accelLim=1.5
        self.SSE=0.0

class CarView():
    def __init__(self, args):
        self.input_widgets, self.display_widgets = args
        # unpack widgets with same names as they have on the GUI
        self.le_m1, self.le_v, self.le_k1, self.le_c1, self.le_m2, self.le_k2, self.le_ang, \
         self.le_tmax, self.chk_IncludeAccel = self.input_widgets

        self.gv_Schematic, self.chk_LogX, self.chk_LogY, self.chk_LogAccel, \
        self.chk_ShowAccel, self.lbl_MaxMinInfo, self.layout_Plot = self.display_widgets

        # creating a canvas to draw a figure for the car model
        self.figure = Figure(tight_layout=True, frameon=True, facecolor='none')
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layout_Plot.addWidget(NavigationToolbar2QT(self.canvas))
        self.layout_Plot.addWidget(self.canvas)

        # axes for the plotting using view
        self.ax = self.figure.add_subplot()
        if self.ax is not None:
            self.ax1 = self.ax.twinx()
        self.interpolatorWheel=None
        self.interpolatorBody=None
        self.interpolatorAccel=None
        self.posWheelTracer=None
        self.posBodyTracer=None
        self.posRoadTracer=None
        self.accelTracer=None
        self.buildScene()

    def updateView(self, model=None):
        self.le_m1.setText("{:0.2f}".format(model.m1))
        self.le_k1.setText("{:0.2f}".format(model.k1))
        self.le_c1.setText("{:0.2f}".format(model.c1))
        self.le_m2.setText("{:0.2f}".format(model.m2))
        self.le_k2.setText("{:0.2f}".format(model.k2))
        self.le_ang.setText("{:0.2f}".format(model.yangdeg))
        self.le_tmax.setText("{:0.2f}".format(model.tmax))
        stTmp="k1_min = {:0.2f}, k1_max = {:0.2f}\nk2_min = {:0.2f}, k2_max = {:0.2f}\n".format(model.mink1, model.maxk1, model.mink2, model.maxk2)
        stTmp+="SSE = {:0.2f}".format(model.SSE)
        self.lbl_MaxMinInfo.setText(stTmp)
        self.CarBody.setMass(model.m1)
        self.Wheel.setMass(model.m2)
        self.spring1.setk(model.k1)
        self.spring2.setk(model.k2)
        self.dashpot.setc(model.c1)
        self.doPlot(model)

    def buildScene(self):
        #create a scene object
        self.scene = qtw.QGraphicsScene()
        self.scene.setObjectName("MyScene")
        self.scene.setSceneRect(-200, -200, 400, 400)  # xLeft, yTop, Width, Height

        #set the scene for the graphics view object
        self.gv_Schematic.setScene(self.scene)
        #make some pens and brushes for my drawing
        self.setupPensAndBrushes()
        #make the components
        self.Road = Road(0,100,300,10,pen=self.groundPen,brush=self.groundBrush)
        self.Wheel = Wheel(0,50, roady=self.Road.y, penTire=self.penTire, brushWheel=self.brushWheel, penMass=self.penMass, brushMass=self.brushMass, name = "Wheel")
        self.CarBody = MassBlock(0, -70, 100, 30, pen=self.penMass, brush=self.brushMass, name="Car Body", label='Car Body', mass=150)
        self.spring1 = LinearSpring(qtc.QPointF(-35.0, self.Wheel.y), qtc.QPointF(-35, self.CarBody.y), pen=self.penMass, name='k1', label='Spring 1', k=10)
        self.spring2 = LinearSpring(qtc.QPointF(self.Wheel.x, self.Wheel.y), qtc.QPointF(self.Wheel.x, self.Road.y), coilsWidth=10, coilsLength=20, nCoils=4, pen=self.penMass, name='k2', label='Spring 2', k=10)
        self.dashpot = DashPot(qtc.QPointF(-self.spring1.stPt.x(), self.spring1.stPt.y()),qtc.QPointF(-self.spring1.enPt.x(), self.spring1.enPt.y()), dpWidth=10, dpLength=30, pen=self.penMass, name='c', label='Dashpot', c=10)
        self.scene.addItem(self.Road)
        self.Wheel.addToScene(self.scene)
        self.scene.addItem(self.CarBody)
        self.scene.addItem(self.spring1)
        self.scene.addItem(self.spring2)
        self.scene.addItem(self.dashpot)

    def setupCanvasMoveEvent(self, window):
        self.canvas.mpl_connect("motion_notify_event", window.mouseMoveEvent_Canvas)

    def setupEventFilter(self, window):
        self.gv_Schematic.setMouseTracking(True)
        self.gv_Schematic.scene().installEventFilter(window)
    def getZoom(self):
        return self.gv_Schematic.transform().m11()

    def setZoom(self, val):
        self.gv_Schematic.resetTransform()
        self.gv_Schematic.scale(val,val)
    def updateSchematic(self):
        self.scene.update()

    def setupPensAndBrushes(self):
        """
        Just sets up pens and brushes for drawing the schematic.
        :return:
        """
        self.penTire = qtg.QPen(qtg.QColor(qtc.Qt.black))
        self.penTire.setWidth(3)
        self.penMass = qtg.QPen(qtg.QColor("black"))
        self.penMass.setWidth(1)
        color = qtg.QColor(qtc.Qt.gray)
        color.setAlpha(64)
        self.brushWheel = qtg.QBrush(color)
        self.brushMass = qtg.QBrush(qtg.QColor(200,200,200, 64))
        self.groundPen = qtg.QPen(qtg.QColor(qtc.Qt.black))
        self.groundPen.setWidth(1)
        self.groundBrush = qtg.QBrush(qtg.QColor(qtc.Qt.black))
        self.groundBrush.setStyle(qtc.Qt.DiagCrossPattern)

    def doPlot(self, model=None):
        """
        Creates the plot.
        :param model:
        :return:
        """
        if model.results is None:
            return
        ax = self.ax
        ax1 = self.ax1
        # plot result of odeint solver
        QTPlotting = True  # assumes we are plotting onto a QT GUI form
        if ax == None:
            ax = plt.subplot()
            ax1 = ax.twinx()
            QTPlotting = False  # actually, we are just using CLI and showing the plot
        ax.clear()
        ax1.clear()
        t = model.timeData
        ywheel = model.wheelPosData
        ycar = model.bodyPosData
        accel = model.accelBodyData

        if self.chk_LogX.isChecked():
            ax.set_xlim(0.001,model.tmax)
            ax.set_xscale('log')
        else:
            ax.set_xlim(0.0, model.tmax)
            ax.set_xscale('linear')

        if self.chk_LogY.isChecked():
            ax.set_ylim(0.0001,max(ycar.max(), ywheel.max()*1.05))
            ax.set_yscale('log')
        else:
            ax.set_ylim(0.0, max(ycar.max(), ywheel.max()*1.05))
            ax.set_yscale('linear')

        ax.plot(t, ycar, 'b-', label='Body Position')
        ax.plot(t, ywheel, 'r-', label='Wheel Position')
        ax.plot(t, model.roadPosData, 'k-', label='Road Position', linewidth=3.0)
        if self.chk_ShowAccel.isChecked():
            ax1.plot(t, accel, 'g-', label='Body Accel')
            ax1.axhline(y=accel.max(), color='orange')  # horizontal line at accel.max()
            ax1.set_yscale('log' if self.chk_LogAccel.isChecked() else 'linear')
            ax1.set_ylabel("Y'' (g)", fontsize = 'large' if QTPlotting else 'medium')
            ax1.yaxis.set_label_coords(1.05,.5)

        # add axis labels
        ax.set_ylabel("Vertical Position (m)", fontsize='large' if QTPlotting else 'medium')
        ax.set_xlabel("time (s)", fontsize='large' if QTPlotting else 'medium')
        ax.legend()

        ax.axvline(x=model.tramp)  # vertical line at tramp
        ax.axhline(y=model.ymag)  # horizontal line at ymag
        # modify the tick marks
        ax.tick_params(axis='both', which='both', direction='in', top=True,
                       labelsize='large' if QTPlotting else 'medium')  # format tick marks
        ax1.tick_params(axis='both', which='both', direction='in', right=True,
                       labelsize='large' if QTPlotting else 'medium')  # format tick marks
        # show the plot
        if QTPlotting == False:
            plt.show()
        else:
            self.canvas.draw()

    def getPoints(self, model=None, t=0):
        """
        This gets interpolated values from the model data at a given time.
        :param model:
        :param t:
        :return: ywheel, ybody, yroad, accel
        """
        if model is None: return 0,0,0
        ywheel=np.interp(t, model.timeData, model.wheelPosData)
        ybody=np.interp(t, model.timeData, model.bodyPosData)
        yroad=np.interp(t,model.timeData, model.roadPosData)
        accel=np.interp(t, model.timeData, model.accelBodyData)
        return ywheel,ybody, yroad ,accel

    def animate(self, model=None, t=0):
        """
        Here I am interpolating the model data at time t and updating the vertical positions of the wheel and the car
        body.  The compression of the spring(s) occurs if I change their end point locations to something other
        than their free length which is established when they are first define.  Any change in the end point coordinates
        causes the active part of the spring to shorten/lengthen.  I could calculate the force of the spring by:
        F=k*deltaY.

        Similar idea for the dashpote.  Although in the case of the dashpot, it is the relative velocity difference
        between the end points that causes the force.
        :param model:
        :param t:
        :return:
        """
        if model is None: return
        ywheel, ybody, yroad, accel=self.getPoints(model, t)
        try:
            if self.posWheelTracer is not None:
                self.posWheelTracer.remove()
            if self.posBodyTracer is not None:
                self.posBodyTracer.remove()
            if self.posRoadTracer is not None:
                self.posRoadTracer.remove()
            if self.accelTracer is not None:
                self.accelTracer.remove()
        finally:
            pass
        # I'll assume a tire of size P275/55R20
        # This means the tire width is 275 mm -> 10.83 in
        # The height of the sidewall is:  0.55*10.85 = 5.95 in
        # The wheel diameter is 20 in
        # Therefore the tire diameter is 31.9 in
        # The Wheel radius is set to 100.  Hence scale is:  s*31.9(in)*[25.4(mm)/(in)]*[(m)/1000(mm)] = 200 => s=246.83/(m)
        self.scale  = 200*(1000/25.4)/self.Wheel.radius
        self.posWheelTracer=self.ax.plot(t, ywheel, 'o', markeredgecolor='red', markerfacecolor='none')[0]
        self.posBodyTracer=self.ax.plot(t, ybody, 'o', markeredgecolor='blue', markerfacecolor='none')[0]
        self.posRoadTracer=self.ax.plot(t, yroad, 'o', markeredgecolor='black', markerfacecolor='none')[0]
        self.Road.y=self.Road.y0-yroad*self.scale
        self.Wheel.road_y = self.Road.y
        self.Wheel.y=self.Wheel.y0-ywheel*self.scale
        self.spring2.enPt.setY(self.Road.y)
        self.spring2.stPt.setY(self.Wheel.y)
        self.CarBody.y=self.CarBody.y0-ybody*self.scale
        self.spring1.stPt.setY(self.Wheel.y)
        self.spring1.enPt.setY(self.CarBody.y)
        self.dashpot.stPt.setY(self.Wheel.y)
        self.dashpot.enPt.setY(self.CarBody.y)
        if self.chk_ShowAccel.isChecked():
            self.accelTracer=self.ax1.plot(t,accel,'o', markeredgecolor='green', markerfacecolor='none')[0]
        self.canvas.draw()
        self.scene.update()

class CarController():
    def __init__(self, args):
        """
        This is the controller I am using for the quarter car model.
        """
        self.input_widgets, self.display_widgets = args
        #unpack widgets with same names as they have on the GUI
        self.le_m1, self.le_v, self.le_k1, self.le_c1, self.le_m2, self.le_k2, self.le_ang, \
         self.le_tmax, self.chk_IncludeAccel = self.input_widgets

        self.gv_Schematic, self.chk_LogX, self.chk_LogY, self.chk_LogAccel, \
        self.chk_ShowAccel, self.lbl_MaxMinInfo, self.layout_horizontal_main = self.display_widgets

        self.model = CarModel()
        self.view = CarView(args)

    def ode_system(self, t ,X):
        # define the forcing function equation for the linear ramp
        # It takes self.tramp time to climb the ramp, so y position is
        # a linear function of time.
        if t < self.model.tramp:
            y = self.model.ymag * (t / self.model.tramp)
        else:
            y = self.model.ymag

        x1 = X[0]  # car position in vertical direction
        x1dot = X[1]  # car velocity  in vertical direction
        x2 = X[2]  # wheel position in vertical direction
        x2dot = X[3]  # wheel velocity in vertical direction

        # write the non-trivial equations in vertical direction
        x1ddot = (1 / self.model.m1) * (self.model.c1 * (x2dot - x1dot) + self.model.k1 * (x2 - x1))
        x2ddot = (1 / self.model.m2) * (
                    -self.model.c1 * (x2dot - x1dot) - self.model.k1 * (x2 - x1) + self.model.k2 * (y - x2))
        self.step += 1
        # return the derivatives of the input state vector
        return [x1dot, x1ddot, x2dot, x2ddot]

    def calculate(self, doCalc=True):
        """
        I will first set the basic properties of the car model and then calculate the result
        in another function doCalc.
        """
        #Step 1.  Read from the widgets
        self.model.m1 = float(self.le_m1.text())
        self.model.m2 = float(self.le_m2.text())
        self.model.c1 = float(self.le_c1.text())
        self.model.k1 = float(self.le_k1.text())
        self.model.k2 = float(self.le_k2.text())
        self.model.v = float(self.le_v.text())

        #recalculate min and max k values
        self.mink1=(self.model.m1*9.81)/(6.0*25.4/1000.0)
        self.maxk1=(self.model.m1*9.81)/(3.0*25.4/1000.0)
        self.mink2=((self.model.m1+self.model.m2)*9.81)/(1.5*25.4/1000.0)
        self.maxk2=((self.model.m1+self.model.m2)*9.81)/(0.75*25.4/1000.0)

        ymag=6.0/(12.0*3.3)   #This is the height of the ramp in m
        if ymag is not None:
            self.model.ymag = ymag
        self.model.yangdeg = float(self.le_ang.text())
        self.model.tmax = float(self.le_tmax.text())
        if(doCalc):
            self.doCalc()
        self.SSE((self.model.k1, self.model.c1, self.model.k2), optimizing=False)
        self.view.updateView(self.model)

    def setWidgets(self, w):
        """
        Pass widgets to view for setup.
        :param w:
        :return:
        """
        self.view.setWidgets(w)
        self.chk_IncludeAccel=self.view.chk_IncludeAccel

    def setupCanvasMoveEvent(self, window):
        """
        Pass through to view.
        :param window:
        :return:
        """
        self.view.setupCanvasMoveEvent(window)

    def setupEventFilter(self, window):
        self.view.setupEventFilter(window=window)
    def getZoom(self):
        """
        Pass request along to the view.
        :return:
        """
        return self.view.getZoom()

    def setZoom(self,val):
        """
        Pass request along to the view.
        :param val:
        :return:
        """
        self.view.setZoom(val=val)

    def updateSchematic(self):
        """
        Pass request along to the view.
        :return:
        """
        self.view.updateSchematic()

    def doCalc(self, doPlot=True, doAccel=True):
        """
        This solves the differential equations for the quarter car model.
        :param doPlot:
        :param doAccel:
        :return:
        """
        v = 1000 * self.model.v / 3600  # convert speed to m/s from kph
        self.model.angrad = self.model.yangdeg * math.pi / 180.0  # convert angle to radians
        self.model.tramp = self.model.ymag / (math.sin(self.model.angrad) * v)  # calculate time to traverse ramp

        self.model.timeData=np.logspace(np.log10(0.000001), np.log10(self.model.tmax), 2000)
        #self.model.timeData=np.linspace(0, self.model.tmax, 2000)
        self.model.roadPosData=[self.model.ymag if t>self.model.tramp else t*self.model.ymag/self.model.tramp for t in self.model.timeData]
        ic = [0, 0, 0, 0]
        # run odeint solver
        self.step=0
        self.model.results = solve_ivp(self.ode_system, t_span=[0,self.model.tmax], y0=ic, t_eval=self.model.timeData)
        if doAccel:
            self.calcAccel()
        if doPlot:
            self.doPlot()
        self.model.bodyPosData = self.model.results.y[0]
        self.model.wheelPosData = self.model.results.y[2]
        pass

    def calcAccel(self):
        """
        Calculate the acceleration in the vertical direction using the forward difference formula.
        """
        N=len(self.model.timeData)
        self.model.accelBodyData=np.zeros(shape=N)
        vel=self.model.results.y[1]
        for i in range(N):
            if i==N-1:
                h = self.model.timeData[i] - self.model.timeData[i - 1]
                self.model.accelBodyData[i]= (vel[i] - vel[i - 1]) / (9.81 * h)  # backward difference of velocity
            else:
                h = self.model.timeData[i + 1] - self.model.timeData[i]
                self.model.accelBodyData[i] = (vel[i + 1] - vel[i]) / (9.81 * h)  # forward difference of velocity
            # else:
            #     self.model.accel[i]=(vel[i+1]-vel[i-1])/(9.81*2.0*h)  # central difference of velocity
        self.model.accelMax=self.model.accelBodyData.max()
        return True

    def OptimizeSuspension(self):
        """
        Step 1:  set parameters based on GUI inputs by calling self.set(doCalc=False)
        Step 2:  make an initial guess for k1, c1, k2
        Step 3:  optimize the suspension
        :return:
        """
        #Step 1:
        #$JES MISSING CODE HERE$
        self.calculate(doCalc=False)
        #Step 2:
        #JES MISSING CODE HERE$
        x0=np.array([(self.model.mink1)*1.1, self.model.c1, (self.model.mink2)*1.1])
        #Step 3:
        #JES MISSING CODE HERE$
        answer=minimize(self.SSE,x0,method='Nelder-Mead')
        self.view.updateView(self.model)

    def SSE(self, vals, optimizing=True):
        """
        Calculates the sum of square errors between the contour of the road and the car body.
        :param vals:
        :param optimizing:
        :return:
        """
        k1, c1, k2=vals  #unpack the new values for k1, c1, k2
        self.model.k1=k1
        self.model.c1=c1
        self.model.k2=k2
        self.doCalc(doPlot=False)  #solve the odesystem with the new values of k1, c1, k2
        SSE=0
        for i in range(len(self.model.results.y[0])):
            t=self.model.timeData[i]
            y=self.model.results.y[0][i]
            if t < self.model.tramp:
                ytarget = self.model.ymag * (t / self.model.tramp)
            else:
                ytarget = self.model.ymag
            SSE+=(y-ytarget)**2

        #some penalty functions if the constants are too small
        if optimizing:
            if k1<self.model.mink1 or k1>self.model.maxk1:
                SSE+=100
            if c1<10:
                SSE+=100
            if k2<self.model.mink2 or k2>self.model.maxk2:
                SSE+=100
            o_IncludeAccel = self.chk_IncludeAccel.isChecked()
            # I'm overlaying a gradient in the acceleration limit that scales with distance from a target squared.
            if self.model.accelMax > self.model.accelLim and o_IncludeAccel:
                # need to soften suspension
                SSE+=10+10*(self.model.accelMax-self.model.accelLim)**2
        self.model.SSE=SSE
        return SSE

    def doPlot(self):
        self.view.doPlot(self.model)

    def animate(self, t):
        self.view.animate(self.model,t)

    def getPoints(self, t):
        return self.view.getPoints(self.model, t)
#endregion
#endregion

def main():
    QCM = CarController()
    QCM.doCalc()

if __name__ == '__main__':
    main()
