import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tokofoto import *

# warning: kode spaghetti italiano mamma mia

# todo
# link ui ke cuda
# kamera
# save image
# apply edits

class mainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        
        self.setWindowTitle("Tokofoto")

        self.setFixedSize(1366,768)

        self.contrastval = [0]
        self.saturationval = [100]
        self.blurval = [0]
        self.grayscalemode = [False]
        self.edgemode = [False]
        self.cameramode = [False]

        self.image_path = ""

        image_label = QLabel(self)
        image_label.resize(1280,720)
        image_label.setAlignment(Qt.AlignCenter)
        self.image_label = image_label

        self.setCentralWidget(image_label)
        
        menu = self.menuBar()
        self.menu = menu

        open_button = QAction("Open", self)
        open_button.triggered.connect(self.open_image)
        self.open_button = open_button

        save_button = QAction("Save", self)
        self.save_button = save_button

        save_as_button = QAction("Save As", self)
        self.save_as_button = save_as_button


        camera_button = QAction("Enable Camera", self)
        camera_button.setCheckable(True)
        camera_button.toggled.connect(self.onCameraToggle)

        grayscale_button = QAction("Greyscale", self)
        grayscale_button.setCheckable(True)
        grayscale_button.toggled.connect(lambda: self.onToggleClick(grayscale_button,self.grayscalemode))
        self.grayscale_button = grayscale_button
        
        contrast_button = QAction("Contrast", self)
        contrast_button.triggered.connect(lambda: self.onSliderClick("Contrast",-255,255,self.contrastval))
        self.contrast_button = contrast_button

        saturation_button = QAction("Saturation", self)
        saturation_button.triggered.connect(lambda: self.onSliderClick("Saturation",0,200,self.saturationval))
        self.saturation_button = saturation_button

        edge_button = QAction("Edge Detection", self)
        edge_button.setCheckable(True)
        edge_button.toggled.connect(lambda: self.onToggleClick(edge_button,self.edgemode))
        self.edge_button = edge_button
        
        blur_button = QAction("Blur", self)
        blur_button.triggered.connect(lambda: self.onSliderClick("Blur",0,10,self.blurval))
        self.blur_button = blur_button

        file_menu = menu.addMenu("File")
        file_menu.addAction(open_button)
        file_menu.addAction(save_button)
        file_menu.addAction(save_as_button)
        file_menu.addSeparator()
        file_menu.addAction(camera_button)

        adjustments_menu = menu.addMenu("Adjustments")
        adjustments_menu.addAction(grayscale_button)
        adjustments_menu.addAction(contrast_button)
        adjustments_menu.addAction(saturation_button)

        effects_menu = menu.addMenu("Effects")
        effects_menu.addAction(edge_button)
        effects_menu.addAction(blur_button)

        toolbar = QToolBar()
        
        self.addToolBar(Qt.BottomToolBarArea,toolbar)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        apply_button = QAction("Apply Edits",self)
        toolbar.addAction(apply_button)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)


    def onCameraToggle(self,checked):
        
        if (checked):
            self.open_button.setDisabled(True)
            self.save_button.setDisabled(True)
            self.save_as_button.setDisabled(True)

    def onSliderClick(self,title,min,max,attr):

        print(attr)
        self.slider_window = sliderWindow(title,min,max,attr)
        self.slider_window.show()

    def onToggleClick(self,button,attr):
        
        print(attr[0])
        attr[0] = button.isChecked()

    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Pick an image", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            self.load_image(file_name)

    def save_image(self):
        
        cv2.imwrite(self.image_path,self.cv_image)

    def reset_vals(self):

        self.contrastval = [0]
        self.saturationval = [100]
        self.blurval = [0]
        self.grayscalemode = [False]
        self.edgemode = [False]
        self.cameramode = [False]

    def load_image(self,file_name):

        self.image_path = file_name
        self.cv_image = cv2.imread(self.image_path)

        self.reset_vals(self)

        rgb_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2RGB)

        self.height, self.width, self.channel = rgb_image.shape
        self.bytes_per_line = 3 * self.width

        q_image = QImage(rgb_image.data, self.width, self.height, self.bytes_per_line, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(q_image)

        aspect_ratio = pixmap.width() / pixmap.height()

        if 1280 / 720 > aspect_ratio:
            self.pic_scale = int(720 * aspect_ratio)
            self.image_label.setPixmap(pixmap.scaledToWidth(self.pic_scale))
            self.pic_scale_method = "width"
        else:
            self.pic_scale = int(1280 / aspect_ratio)
            self.image_label.setPixmap(pixmap.scaledToHeight(self.pic_scale))
            self.pic_scale_method = "height"


class sliderWindow(QWidget):

    def __init__(self,title,min,max,variable_ref,parent=None):

        super().__init__(parent)

        self.ok = False

        self.setWindowTitle(title)

        self.layout = QVBoxLayout()

        self.variable_ref = variable_ref
        self.original_val = self.variable_ref[0]

        self.slider_layout = QHBoxLayout()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(min,max)
        self.slider.setValue(self.original_val)
        self.slider.valueChanged.connect(self.update_spinbox)
        self.slider_layout.addWidget(self.slider)

        self.spinbox = QSpinBox()
        self.spinbox.setRange(min,max)
        self.spinbox.setValue(self.original_val)
        self.spinbox.valueChanged.connect(self.update_slider)
        self.slider_layout.addWidget(self.spinbox)

        self.layout.addLayout(self.slider_layout)

        # Buttons
        self.buttons_layout = QHBoxLayout()

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept_changes)
        self.buttons_layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reset_changes)
        self.buttons_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.buttons_layout)
        self.setLayout(self.layout)

        self.temp_value = self.original_val

    def update_spinbox(self):
        self.temp_value = self.slider.value()
        self.spinbox.setValue(self.temp_value)
        self.update_variable()

    def update_slider(self):
        self.temp_value = self.spinbox.value()
        self.slider.setValue(self.temp_value)
        self.update_variable()
    
    def update_variable(self):
        self.variable_ref[0] = self.temp_value

    def accept_changes(self):
        self.ok = True
        self.close()

    def reset_changes(self):
        self.variable_ref[0] = self.original_val
        self.slider.setValue(self.original_val)
        self.spinbox.setValue(self.original_val)
        self.close()

    def closeEvent(self, event):
        # Reset changes if the window is closed without using OK button
        if (not self.ok):
            self.reset_changes()
    

app = QApplication(sys.argv)
w = mainWindow()
w.show()
app.exec()