# import sys 
# from PySide2.QtGui import QPainter
# from PySide2.QtCharts import QtCharts
# from functools import partial
import csv
# import os
# from PyQt5 import QtWidgets
# from Custom_Widgets.Widgets import*

class ChartPlot:
    def __init__(self) :
        self.date_list = []
        self.sales_list = {}
        self.name_list = []
        self.row_count = 0
        self.point = []
        self.whole = {}
        self.ProductAnalysis()
        self.LineSalesAnalysis()

    def ProductAnalysis(self):
        date_list = {}
        sales_list = {}
        name_list = []
        row_count = 0
        with open ('/home/david/Documents/Work/Python/projects/charts_tutorial_resource_files/csv/sales.csv') as csv_whole_sales:
            csv_read = csv.reader(csv_whole_sales,delimiter=",")
            for row in csv_read:
                if row_count > 0:
                    if not row[1] in date_list:
                        date_list[row[1]] = []
                        date_list[row[1]].append({"product":row[0],"sales":row[3]})
                    else:
                        date_list[row[1]].append({"product":row[0],"sales":row[3]})
                row_count += 1
        for x in date_list:
            for z in date_list[x]:
                if not z["product"] in name_list:
                    name_list.append(z["product"])
                if not z["product"] in sales_list:
                    sales_list[z["product"]] = []
                    sales_list[z["product"]].append(float(z["sales"]))
                else:
                    sales_list[z["product"]].append(float(z["sales"]))
        self.whole = date_list
        self.date_list = list(date_list.keys())
        self.sales_list = sales_list
        self.name_list = name_list
        self.row_count = row_count
        
    def LineSalesAnalysis (self):
        point = []
        for line in self.date_list:
            sell = self.whole[line]
            for sales in sell:
                point.append(sales['sales'])
        self.point = point

    def getSalesList(self):
        return self.sales_list
    
    def getDateList(self):
        return self.date_list
    
    def getNameList(self):
        return self.name_list
    
    def rowCount(self):
        return self.row_count
    
    def getPoint(self):
        return self.point
    
    def DateOnly(self):
        print(self.date_list)
        date_only = []
        for i in self.date_list:
            new_num = float(i[:2])
            date_only.append(new_num)
        return date_only
        # self.bar_ser = QtCharts.QBarSeries()

        # for ser in name_list:
        #     setattr(self,"set"+str(ser),QtCharts.QBarSet(str(x)))
        #     self.bar_ser.append(getattr(self,"set"+str(x)))
        #     getattr(self,"set"+str(x)).append(sales_list[x])
        #     self.bar_ser.append(getattr(self,"set"+str(x)))

        # self.chart = QtCharts.QChart()
        # self.chart.addSeries(self.bar_ser)
        # self.chart.setTitle(f"{name_list}")

        # self.categories = date_list
        # self.axisX = QtCharts.QBarCategoryAxis()
        # self.axisX.append(self.categories)
        # self.chart.setAxisX(self.axisX,self.bar_ser)

        # self.axisY = QtCharts.QValueAxis()
        # self.chart.setAxisY(self.axisY,self.bar_ser)

        # self.chart.legend().setVisible(True)
        # self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        # self.chartView = QtCharts.QChartView(self.chart)
        # self.chartView.setRenderHint(QPainter.Antialiasing)
        # self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        # self.chartView.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.hasHeightForWidth(self.chartView.sizePolicy().hasHeightForWidth())
        # self.chartView.setSizePolicy(sizePolicy)
        # self.chartView.setMinimumSize(0,300)

        # self.ui.bar_title_layout.addWidget(self.chartView)
        # self.ui.bar_title_frame.setStyleSheet(u"background-color: transparent ")
        # print(sales_list)
        # print(name_list)
        # print(date_list)

if __name__ == "__main__":
    ch = ChartPlot()
    ch.ProductAnalysis()
    ch.DateOnly()