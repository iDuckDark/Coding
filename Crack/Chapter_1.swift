// ============ 1.1 ============
func is_unique(s: String) -> Bool {
    if s.count > 128 {
        return false
    }
    let characters = repeatElement(0, count: 128)

    for char in s  {
        // if characters[ord(char)]:
            // return false
        // characters[ord(char)] = true
    }
    return true
}

// is_unique(s: "abcd")

print(Int("A"))