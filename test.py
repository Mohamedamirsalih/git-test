class student :
  def __init__(self,name, id, grade) :
    self.name = name
    self.id = id
    self.grade = grade

student1 = student ("Mohamed", 2501306, 79)
print (vars(student1))