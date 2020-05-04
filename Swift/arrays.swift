
var someInts1 = [Int](repeating: 10, count: 3)
var someInts2: [Int] = [0, 1, 2, 3]

var someInts = someInts1
print("Value of first element is \(someInts[0])")
print("Value of second element is \(someInts[1])")
print("Value of third element is \(someInts[2])")

typealias someType = Int
var someArray = [someType]()
someArray.append(20)
someArray.append(30)
someArray += [40]
print(someArray)

var someStrs = [String]()
let strings = ["Apple", "Amazon", "Google"]
someStrs += strings
// https://stackoverflow.com/questions/24028421/swift-for-loop-for-index-element-in-array
for (index, element) in someStrs.enumerated() {
  print("Item \(index): \(element)")
}
