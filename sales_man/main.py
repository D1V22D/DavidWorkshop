import os
from PyQt5 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from Custom_Widgets.Widgets import*
from sales_ui import*
import sys 
from PySide2.QtGui import QPainter
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis,QLineSeries
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import Qt
from functools import partial
from ChartsCreate import ChartPlot
from PyQt5.QtGui import QPainter
# from PySide2.QtWidgets import QSizePolicy




class MainWindow(QtWidgets.QMainWindow):
    def __init__ (self,parent =None):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self,self.ui)
        self.chart_data = ChartPlot()
        self.bar_graph()
        self.line_graph()
        self.show()

    def line_graph(self):
        points = self.chart_data.getPoint()
        date = self.chart_data.DateOnly()
        print(points)
        line_ser = QLineSeries()
        for i in range(len(date)):
                line_ser.append(date[i],float(points[i]))



        chart =  QChart()
 
        chart.addSeries(line_ser)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("whole sales")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
 
 
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        chartview.chart().setTheme(QChart.ChartThemeDark)
 
        self.ui.gridLayout.addWidget(chartview)
        self.ui.line_ch_frame.setStyleSheet(u"background-color: transparent ")
    def bar_graph(self):

        name_list = self.chart_data.getNameList()
        sales_list = self.chart_data.getSalesList()
        date_list = self.chart_data.getDateList()
        self.bar_ser = QPercentBarSeries()
        for ser in name_list:
            setattr(self,"set"+str(ser),QBarSet(str(ser)))
            self.bar_ser.append(getattr(self,"set"+str(ser)))
            getattr(self,"set"+str(ser)).append(sales_list[ser])
            self.bar_ser.append(getattr(self,"set"+str(ser)))
 
        chart = QChart()
        chart.addSeries(self.bar_ser)
        chart.setTitle(f"{name_list}")
        chart.setAnimationOptions(QChart.SeriesAnimations)
 
        categories =date_list
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, self.bar_ser)
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignRight)
 
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        chartView.chart().setTheme(QChart.ChartThemeDark)
 
        self.ui.gridLayout_3.addWidget(chartView)
        self.ui.bar_ch_frame.setStyleSheet(u"background-color: transparent ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
