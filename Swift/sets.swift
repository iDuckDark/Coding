var someSet = Set<Character>()

print(someSet.count, someSet.isEmpty, someSet.contains("c"), someSet)
someSet.insert("c")
someSet.insert("c")
print(someSet.count, someSet.isEmpty, someSet.contains("c"), someSet)
someSet.remove("c")
print(someSet.count, someSet.isEmpty, someSet.contains("c"), someSet)

let evens: Set = [10, 12, 14, 16, 18]
let odds: Set = [5, 7, 9, 11, 13]
let primes = [2, 3, 5, 7]
var output = odds.union(evens).sorted()
print(output)
// [5,7,9,10,11,12,13,14,16,18]
output = odds.intersection(evens).sorted()
print(output)
// []
output = odds.subtracting(primes).sorted()
print(output)
// [9, 11, 13]
