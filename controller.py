# -*- coding: utf-8 -*-

# python imports
from math import degrees

# pyfuzzy imports
import Equations

class FuzzyController:

    def __init__(self):
        self.membership_soil_moisture = {
            "dry": 0,
            "moist": 0,
            "wet": 0,
        }
        self.membership_temperature = {
            "cold": 0,
            "mild": 0,
            "normal": 0,
            "warm": 0,
            "hot": 0
        }
        self.duration = {
            "short": 0,
            "medium": 0,
            "long": 0,
        }

    def fuzzify_soil_moisture(self, input):
        soil_moisture = Equations.soil_moisture()
        self.membership_soil_moisture["dry"] = soil_moisture.dry(input)
        self.membership_soil_moisture["moist"] = soil_moisture.moist(input)
        self.membership_soil_moisture["wet"] = soil_moisture.wet(input)

    def fuzzify_temperature(self, input):
        temperature = Equations.temperature()
        self.membership_temperature["cold"] = temperature.cold(input)
        self.membership_temperature["mild"] = temperature.mild(input)
        self.membership_temperature["normal"] = temperature.normal(input)
        self.membership_temperature["warm"] = temperature.warm(input)
        self.membership_temperature["hot"] = temperature.hot(input)

    def fuzzification(self, input):
        self.fuzzify_soil_moisture(input['soil_moisture'])
        self.fuzzify_temperature(input['temperature'])

    def inference(self):
        self.duration["long"] = max(
            min(self.membership_soil_moisture["dry"], self.membership_temperature["cold"]),
            min(self.membership_soil_moisture["dry"], self.membership_temperature["mild"]),
            min(self.membership_soil_moisture["dry"], self.membership_temperature["normal"]),
            min(self.membership_soil_moisture["dry"], self.membership_temperature["warm"]),
            min(self.membership_soil_moisture["dry"], self.membership_temperature["hot"])
        )
        self.duration["medium"] = max(
            min(self.membership_soil_moisture["moist"], self.membership_temperature["normal"]),
            min(self.membership_soil_moisture["moist"], self.membership_temperature["warm"]),
            min(self.membership_soil_moisture["moist"], self.membership_temperature["hot"]),
        )
        self.duration["short"] = max(
            min(self.membership_soil_moisture["moist"], self.membership_temperature["cold"]),
            min(self.membership_soil_moisture["moist"], self.membership_temperature["mild"]),
            min(self.membership_soil_moisture["wet"], self.membership_temperature["cold"]),
            min(self.membership_soil_moisture["wet"], self.membership_temperature["mild"]),
            min(self.membership_soil_moisture["wet"], self.membership_temperature["normal"]),
            min(self.membership_soil_moisture["wet"], self.membership_temperature["warm"]),
            min(self.membership_soil_moisture["wet"], self.membership_temperature["hot"])
        )

    def defuzzify_duration(self, point):
        duration = Equations.duration()
        short = min(duration.short(point), self.duration["short"])
        medium = min(duration.medium(point), self.duration["medium"])
        long = min(duration.long(point), self.duration["long"])
        return max(short, medium, long)

    def defuzzification(self):
        n = 10000
        delta = 100 / n
        points_of_duration = [0 + i * delta for i in range(n + 1)]
        sum_numerator = 0
        sum_denominator = 0
        dx = points_of_duration[1] - points_of_duration[0]
        for point in points_of_duration:
            membership = self.defuzzify_duration(point)
            sum_numerator += membership * point * dx
            sum_denominator += membership * dx
        try:
            return sum_numerator / sum_denominator
        except:
            return 0

    def sprinkle(self, input):
        self.fuzzification(input)
        self.inference()
        return self.defuzzification()

    def decide(self, input_test):
        duration = self.sprinkle(input_test)
        return duration
