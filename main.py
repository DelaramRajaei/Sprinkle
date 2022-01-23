#!/usr/bin/env python
# -*- coding: utf-8 -*-

# project imports
from controller import FuzzyController

if __name__ == '__main__':
    # test
    input_test = {'soil_moisture': 9, 'temperature': 20}
    controller = FuzzyController()
    print("The watering duration is", controller.decide(input_test), "minutes")
