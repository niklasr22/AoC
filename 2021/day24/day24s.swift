import Darwin

struct Key : Hashable {
    let a: Int
    let b: Int
    func hash(into hasher: inout Hasher) {
        hasher.combine(a)
        hasher.combine(b)
    }
}
func ==(lhs: Key, rhs: Key) -> Bool {
    return lhs.a == rhs.a && lhs.b == rhs.b
}

let input = [
    (13,10,1),
    (11,16,1),
    (11,0,1),
    (10,13,1),
    (-14,7,26),
    (-4,11,26),
    (11,11,1),
    (-3,10,26),
    (12,16,1),
    (-12,8,26),
    (13,15,1),
    (-12,2,26),
    (-15,5,26),
    (-12,10,26)
]

var cache: [Key: [String]] = [:]

func routine(z: Int, d: Int, pos: Int) -> Int {
    var z = z
    let parameters = input[pos]
    let x = z % 26 + parameters.0
    z /= parameters.2
    if x != d {
        z = z * 26 + d + parameters.1
    }
    return z
}

func search(pos: Int, z: Int) -> [String] {
    if pos == 14 {
        if z == 0 {
            return [""]
        }
        return []
    }
    var searchresults: [String] = []
    for d in 1...9 {
        let newZ = routine(z: z,d: d, pos: pos)
        let key = Key(a: pos + 1, b: newZ)
        if cache.keys.contains(key) {
            for r in cache[key]! {
                searchresults.append("\(d)" + r)
            }
        } else {
            let res = search(pos: pos + 1, z: newZ)
            cache[key] = res
            for r in res {
                searchresults.append("\(d)" + r)
            }
        }
    }
    return searchresults
}

let mainres = search(pos: 0, z: 0)
var intlist: [Int] = []
for s in mainres {
    if let x = Int(s) {
        intlist.append(x)
    }
}
if intlist.count > 0 {
    print("a) \(intlist.max()!)")
    print("b) \(intlist.min()!)")
} else {
    print("no results \(mainres.count) \(mainres[0])")
}