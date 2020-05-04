func student(name: String) -> String {
    return name
}

print(student(name: "First Program"))
print(student(name: "About Functions"))

func ls(array: [Int]) -> (Int, Int) {
    var lar = array[0]
    var sma = array[0]

    for i in array[1 ..< array.count] {
        if i < sma {
            sma = i
        } else if i > lar {
            lar = i
        }
    }
    return (lar, sma)
}

let num = ls(array: [40, 12, -5, 78, 98])
print("Largest number is: \(num.0) and smallest number is: \(num.1)")
