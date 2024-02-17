"""
Exercise13 -> Write a program that receives a student's grades and calculates Average.(Using OOP)
"""


class Average:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def avg(self):
        if type(self.scores) == list:
            scores_sum = 0
            for score in self.scores:
                scores_sum += score
            avg = scores_sum / len(self.scores)
            print(f"Student {name}")
            print(f"The Average is: {avg}")
        else:
            print("Scores Must Be In a List!")


scores = [5, 5, 6, 4, 3]
name = "amir"
stu1 = Average(name, scores)
stu1.avg()

