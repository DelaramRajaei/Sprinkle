class soil_moisture:
    # dry := (0, 1)(10, 1)(20, 0)
    def dry(self, input):
        if (0 <= input) and (input < 10):
            return 1
        elif (10 <= input) and (input <= 20):
            return (-0.1 * input) + 2
        else:
            return 0

    # moist := (10, 0)(20, 1)(40, 1)(50,0)
    def moist(self, input):
        if (10 <= input) and (input < 20):
            return (0.1 * input) - 1
        elif (20 <= input) and (input <= 40):
            return 1
        elif (40 <= input) and (input <= 50):
            return (-0.1 * input) + 5
        else:
            return 0

    # wet := (40, 0)(50, 1)(70, 1)
    def wet(self, input):
        if (40 <= input) and (input < 50):
            return (0.1 * input) - 4
        elif (50 <= input) and (input <= 70):
            return 1
        else:
            return 0


class temperature:
    # cold := (-10, 1)(0, 1)(3,0);
    def cold(self, input):
        if (-10 <= input) and (input < 0):
            return 1
        elif (0 <= input) and (input <= 3):
            return (-0.333 * input) + 1
        else:
            return 0

    # mild := (0, 0)(3, 1)(12, 1)(15, 0);
    def mild(self, input):
        if (0 <= input) and (input < 3):
            return 0.333 * input
        elif (3 <= input) and (input <= 12):
            return 1
        elif (12 <= input) and (input <= 15):
            return (-0.333 * input) + 5
        else:
            return 0

    # normal := (12, 0)(15, 1)(24, 1)(27, 0);
    def normal(self, input):
        if (12 <= input) and (input < 15):
            return (0.333 * input) - 4
        elif (15 <= input) and (input <= 24):
            return 1
        elif (24 <= input) and (input <= 27):
            return (-0.333 * input) + 9
        else:
            return 0

    # warm := (24, 0)(27, 1)(36, 1)(39, 0);
    def warm(self, input):
        if (24 <= input) and (input < 27):
            return (0.333 * input) - 8
        elif (27 <= input) and (input <= 36):
            return 1
        elif (36 <= input) and (input <= 39):
            return (-0.333 * input) + 13
        else:
            return 0

    # hot := (36, 0)(39, 1);
    def hot(self, input):
        if (36 <= input) and (input < 39):
            return (0.333 * input) - 12
        elif 39 <= input:
            return 1
        else:
            return 0


class duration:
    def short(self, input):
        if input == 20:
            return 1
        else:
            return 0

    def medium(self, input):
        if input == 40:
            return 1
        else:
            return 0

    def long(self, input):
        if input == 60:
            return 1
        else:
            return 0




