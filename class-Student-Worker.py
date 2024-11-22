class Student(Person), Worker(Person)


student_attrs = [attr for attr in dir(Student) if not attr.startswith('_')]

print("Атрибути класу Student:", student_attrs)
student_methods = [member for member in inspect.getmembers(Student, predicate=inspect.ismethod)]

print("Методи класу Student:")

for method in student_methods:

print(method[0])

worker_attrs = [attr for attr in dir(Worker) if not attr.startswith('_')]

print("Атрибути класу Worker:", worker_attrs)

worker_methods = [member for member in inspect.getmembers(Worker, predicate=inspect.ismethod)]

print("Методи класу Worker:")

for method in worker_methods:

print(method[0])
