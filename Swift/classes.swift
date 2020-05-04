class Person {
    private var _name: String

    var name: String {
        get { return _name }
        set { _name = newValue }
    }

    init(name: String) {
        _name = name
        print("Person Init")
    }
}

class Student: Person {
    var studentID: String
    init(name: String, studentID: String) {
        self.studentID = studentID
        super.init(name: name)
        print("Student Init")
    }
}

let person = Person(name: "Adam")
print()
let student = Student(name: "Student 1", studentID: "1")
print(person.name)
