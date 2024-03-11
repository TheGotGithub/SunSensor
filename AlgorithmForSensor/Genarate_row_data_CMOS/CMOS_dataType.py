import numpy as np
class CMOS_datatype(object):
    def __init__(self):
        self.rawData = None 
        self.roiData = None
        self.sumRowVal = None
        self.sumColVal = None

        self.peakPoint = None

        self.Xc = None
        self.Yc = None

        self.Px = None
        self.Py = None

        self.coordinateX = None
        self.coordinateY = None
        self.h = None

        self.alpha = None
        self.beta = None

    def printAll(self):
        exclude_attributes = ['rawData', 'roiData', 'sumRowVal', 'sumColVal']
        attributes = vars(self)
        for attribute, value in attributes.items():
            if attribute not in exclude_attributes:
                print(f"{attribute}: {value}")

    def clearAll(self):
        attributes = vars(self)
        for attribute in attributes:
            setattr(self, attribute, None)