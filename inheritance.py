class School:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.SSLC_Mark = int(input("Enter your 10th Mark: "))
    def group(self):
        if self.SSLC_Mark > 400:
            print("You are going to Group1")
            self.stream = "Group1"

        elif 300 < self.SSLC_Mark <= 400:
            print("You are going to Group2")
            self.stream = "Group2"

        elif 200 <= self.SSLC_Mark <= 300:
            print("You are going to Group3")
            self.stream = "Group3"

        else:
            print("Not eligible for any group")
            self.stream = None

        self.HSC_Mark = int(input("Enter your 12th Mark: "))

class College(School):
    def __init__(self):
        super().__init__()   

    def courses(self):
        if self.stream == "Group1" and self.HSC_Mark > 500:
            print("You are eligible to become a Doctor or Engineer")

        elif self.stream == "Group2" and self.HSC_Mark > 500:
            print("You are eligible to become a Nurse or Teacher")

        elif self.stream == "Group3" and self.HSC_Mark > 500:
            print("You are eligible to become a Manager or Accountant")

        else:
            print("You are not eligible for any course")

student = College()
student.group()
student.courses()
