var someDict: [Int: String] = [1: "One", 2: "Two", 3: "Three"]

var cities = ["Delhi", "Bangalore", "Hyderabad"]
var Distance = [2000, 10, 620]
let cityDistanceDict = Dictionary(uniqueKeysWithValues: zip(cities, Distance))
print(cityDistanceDict)

var closeCities = cityDistanceDict.filter { $0.value < 1000 }
print(closeCities)


// https://stackoverflow.com/questions/28129401/determining-if-swift-dictionary-contains-key-and-obtaining-any-of-its-values
let keyExists = cityDistanceDict["Delhi..."] != nil
print(keyExists)
