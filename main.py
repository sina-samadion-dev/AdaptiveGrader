class AdaptiveGrader:
    def __init__(self, center = 220, offside = -60, radius = 30):
        self.num = 1
        self.answers = ""
        self.center = center
        self.offside_left = center - 10
        self.radius = radius
        self.offside = offside
        self.answer = " "

    def grade(self, mean):
        dis = mean - self.center
        if mean > self.offside_left:
            pass
        elif dis < 0:
            if self.answer == " ":
                self.answer = str(self.num)
            else:
                self.answer = "*"

            if dis < self.offside:
                self.center = (mean * 0.8) + (self.center * 0.2)
                self.answer = str(self.num)
            else:
                multiplier = ((dis / self.offside) * 0.2)
                self.center = (mean * multiplier) + (self.center * (1 - multiplier))
        elif dis < self.radius:
            if self.answer == " ":
                self.answer = str(self.num)
            else:
                self.answer = "*"
            multiplier = ((dis / self.radius) * 0.3)
            self.center = (mean * (1 - multiplier)) + (self.center * multiplier)
        self.num += 1
        if self.num == 5:
            self.num = 1
            self.answers += self.answer
            self.answer = " "
            return self.answers[-1]
        return " "

    def get_answers(self):
        return self.answers
