class Student:
    
    def __init__(self) -> None:
        self.x="vaibhav"
        self.y="ram ram"
        print("In constructor")

    def helloworld(self)-> None:
        print(self.x)


def main():
    student = Student()
    student.helloworld()
    

if __name__ == "__main__":
    main()