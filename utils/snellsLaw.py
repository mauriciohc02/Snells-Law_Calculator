import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

import warnings
# Ignore warnings
warnings.filterwarnings('ignore')


class SnellsLaw(QMainWindow):
    def __init__(self) -> None:
        """
        Constructor with basic attributes
        returns: None
        rtype: None
        """
        super().__init__()
        self.title = 'Snell\'s Law Graphing Calculator'
        self.left = 10
        self.top = 10
        self.width = 720
        self.height = 720
        self.icon_size = 40
        self.spinbox_width = 120
        self.spinbox_height = 30
        self.initUI()


    def initUI(self) -> None:
        """
        Create each element and objetc of the UI
        returns: None
        rtype: None
        """
        # Set an icon image for the app
        self.setWindowIcon(QIcon('images/app_icon.png'))
        self.setWindowTitle(self.title)
        # Set a window static size
        self.setFixedSize(self.width, self.height)
        # Dialog for the save method
        self.file_dialog = QFileDialog()
        layout = QVBoxLayout()
        # Container where elements will be
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        # Figure for plots
        self.figure = plt.figure()
        self.figure.set_tight_layout(True)
        # Initialized axes attribute
        self.axes = None
        # Canvas for the figure
        self.canvas = FigureCanvasQTAgg(self.figure)
        # Toolbar where buttons or actions will be
        toolbar_menu = QToolBar()
        toolbar_menu.setIconSize(QSize(self.icon_size, self.icon_size))
        toolbar_menu.setMovable(False)
        self.addToolBar(toolbar_menu)
        # Add save_plot action with an icon, status tip and connected to its respective method
        save_plot_action = QAction(QIcon('images/save_plot.png'), 'Save Plot', self)
        save_plot_action.setStatusTip('Save Plot')
        save_plot_action.triggered.connect(self.save_plot)
        toolbar_menu.addAction(save_plot_action)
        # Add reset_data action with an icon, status tip and connected to its respective method
        reset_data_action = QAction(QIcon('images/reset_data.png'), 'Reset Data', self)
        reset_data_action.setStatusTip('Reset Data')
        reset_data_action.triggered.connect(self.reset_data)
        toolbar_menu.addAction(reset_data_action)
        # Add a Title
        label_title = QLabel(self.title)
        label_title.setFont(QFont('Times', 24, italic=True))
        label_title.setAlignment(Qt.AlignCenter)
        # Add thetaI objects to get the value of this variable
        layout_thetaI = QHBoxLayout()
        layout_thetaI.addStretch()
        label_thetaI = QLabel('Angle of Incidence (θi):')
        self.spinbox_thetaI = QDoubleSpinBox()
        # Set conditions to thetaI value
        self.spinbox_thetaI.setFixedSize(self.spinbox_width, self.spinbox_height)
        self.spinbox_thetaI.setAlignment(Qt.AlignCenter)
        self.spinbox_thetaI.setMinimum(0)
        self.spinbox_thetaI.setMaximum(90)
        self.spinbox_thetaI.setSuffix(' °')
        self.spinbox_thetaI.setSingleStep(0.1)
        layout_thetaI.addWidget(label_thetaI)
        layout_thetaI.addWidget(self.spinbox_thetaI)
        layout_thetaI.addStretch()
        # Add nI objects to get the value of this variable
        layout_nI = QHBoxLayout()
        layout_nI.addStretch()
        label_nI = QLabel('Refractive Index (ni):')
        self.spinbox_nI = QDoubleSpinBox()
        # Set conditions to nI value
        self.spinbox_nI.setFixedSize(self.spinbox_width, self.spinbox_height)
        self.spinbox_nI.setAlignment(Qt.AlignCenter)
        self.spinbox_nI.setMinimum(1)
        self.spinbox_nI.setMaximum(3)
        self.spinbox_nI.setSingleStep(0.1)
        layout_nI.addWidget(label_nI)
        layout_nI.addWidget(self.spinbox_nI)
        layout_nI.addStretch()
        # Add nR objects to get the value of this variable
        layout_nR = QHBoxLayout()
        layout_nR.addStretch()
        label_nR = QLabel('Refractive Index (nr):')
        self.spinbox_nR = QDoubleSpinBox()
        # Set conditions to nR value
        self.spinbox_nR.setFixedSize(self.spinbox_width, self.spinbox_height)
        self.spinbox_nR.setAlignment(Qt.AlignCenter)
        self.spinbox_nR.setMinimum(1)
        self.spinbox_nR.setMaximum(3)
        self.spinbox_nR.setSingleStep(0.1)
        layout_nR.addWidget(label_nR)
        layout_nR.addWidget(self.spinbox_nR)
        layout_nR.addStretch()
        # Add thetaR objects to get the value of this variable
        layout_thetaR = QHBoxLayout()
        layout_thetaR.addStretch()
        label_thetaR = QLabel('Angle of Refraction (θr):')
        self.spinbox_thetaR = QDoubleSpinBox()
        # Set conditions to thetaR value
        self.spinbox_thetaR.setFixedSize(self.spinbox_width, self.spinbox_height)
        self.spinbox_thetaR.setAlignment(Qt.AlignCenter)
        self.spinbox_thetaR.setMinimum(0)
        self.spinbox_thetaR.setMaximum(90)
        self.spinbox_thetaR.setSuffix(' °')
        self.spinbox_thetaR.setSingleStep(0.1)
        self.spinbox_thetaR.setDisabled(True)
        self.spinbox_thetaR.valueChanged.connect(self.update_thetaR)
        # It'll update the plot only when thetaR value has changed
        self.spinbox_thetaR.valueChanged.connect(self.update_plot)
        layout_thetaR.addWidget(label_thetaR)
        layout_thetaR.addWidget(self.spinbox_thetaR)
        layout_thetaR.addStretch()
        # Add widgets to main layout
        layout.addWidget(label_title)
        layout.addLayout(layout_thetaI)
        layout.addLayout(layout_nI)
        layout.addWidget(self.canvas)
        layout.addLayout(layout_nR)
        layout.addLayout(layout_thetaR)
        layout.addStretch()
        # Initialize plot figure
        self.update_plot()
        # Auto update plot and thetaR value with a timer
        self.timer = QTimer()
        self.timer.setInterval(100)
        # self.timer.timeout.connect(self.update_plot)
        self.timer.timeout.connect(self.update_thetaR)
        self.timer.start()
        # Show interface
        self.show()


    def update_thetaR(self) -> None:
        """
        Get and update thetaR value
        returns: None
        rtype: None
        """
        # Get values
        nI = self.spinbox_nI.value()
        thetaI = self.spinbox_thetaI.value()
        nR = self.spinbox_nR.value()
        # Calculate thetaR value based on the Snell's Formula
        thetaR = np.arcsin((nI * np.sin(np.deg2rad(thetaI))) / nR)
        self.spinbox_thetaR.setValue(np.rad2deg(thetaR))

    
    def update_plot(self) -> None:
        """
        Create and set a new plot with current data
        returns: None
        rtype: None
        """
        self.figure.clear()
        # Set up new axes
        self.axes = self.figure.add_subplot(111)
        self.axes.set_xlim(-10, 10)
        self.axes.set_ylim(-10, 10)
        self.axes.axhline(0, color = 'black', linewidth = 2)
        self.axes.axvline(0, color = 'black', linewidth = 2, linestyle = '--')
        # Set Text to plot
        self.axes.text(1, 9, 'Normal', style = 'italic', fontweight = 'bold')
        self.axes.text(7, 1, 'Interface', style = 'italic', fontweight = 'bold')
        self.axes.text(-8, 3, r'$n_i$', style = 'italic', fontweight = 'bold', fontsize = 18)
        self.axes.text(-8, -3, r'$n_r$', style = 'italic', fontweight = 'bold', fontsize = 18)
        self.axes.text(-1, 5, r'$θ_i$', style = 'italic', fontweight = 'bold', fontsize = 18)
        self.axes.text(0.5, -5, r'$θ_r$', style = 'italic', fontweight = 'bold', fontsize = 18)
        self.axes.text(4, -8, r'$n_isin(θ_i) = n_rsin(θ_r)$')
        self.axes.text(3, -9, f'({round(self.spinbox_nI.value(), 2)})sin({round(self.spinbox_thetaI.value(), 2)}) = ({round(self.spinbox_nR.value(), 2)})sin({round(self.spinbox_thetaR.value(), 2)})')
        self.axes.set_yticks([])
        self.axes.set_xticks([])
        # Get parameters in order to plot the data
        tan_thetaI = np.tan(np.deg2rad(self.spinbox_thetaI.value()))
        tan_thetaR = np.tan(np.deg2rad(self.spinbox_thetaR.value()))
        linsI = np.linspace(-10, 0, 100)
        linsR = np.linspace(0, 10, 100)
        # Plot data
        self.axes.plot(linsI * tan_thetaI, -linsI, linewidth = 2)
        self.axes.plot(linsR * tan_thetaR, -linsR, linewidth = 2)
        # Refresh canvas
        self.canvas.draw()

    
    def save_plot(self) -> None:
        """
        Save current plot as a png image
        returns: None
        rtype: None
        """
        # Open file explorer in order to save the plot
        options = self.file_dialog.Options()
        options |= self.file_dialog.DontUseNativeDialog
        path, _ = self.file_dialog.getSaveFileName(self, 'Save Plot', '', 'Images (*.png); All files (*.*)', '', options=options)
        # If dialog is cancelled, will return ''
        if not path:
            return
        
        self.figure.savefig(path)


    def reset_data(self) -> None:
        """
        Reset current data of the entire window (plot and values)
        returns: None
        rtype: None
        """
        # Set data at their minimum values
        self.spinbox_thetaI.setValue(self.spinbox_thetaI.minimum())
        self.spinbox_nI.setValue(self.spinbox_nI.minimum())
        self.spinbox_nR.setValue(self.spinbox_nR.minimum())
        self.spinbox_thetaR.setValue(self.spinbox_thetaR.minimum())


    def __str__(self) -> str:
        return f'SnellsLaw Object'
