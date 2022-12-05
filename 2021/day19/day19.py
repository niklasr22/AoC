data = open("./2021/day19/input.txt").read()

scanners = list(
    map(
        lambda x: list(map(lambda y: list(map(int, y.split(","))), x.splitlines()[1:])),
        data.split("\n\n"),
    )
)
fixed_beacons = set()
for i in scanners[0]:
    fixed_beacons.add(tuple(i))

unknownScanners = scanners[1:]


def orientation(scanner):
    res = []
    for r in range(6):
        for o in [0, 90, 180, 270]:
            rotated = []
            for b in scanner:
                x, y, z = b
                if o == 180:
                    x = -x
                    y = -y
                elif o == 90:
                    x, y = y, -x
                elif o == 270:
                    x, y = -y, x

                xx = x
                yy = y
                zz = z
                if r == 0:
                    xx = x
                    yy = y
                    zz = z
                elif r == 1:  # 90 deg around x
                    xx = x
                    yy = -z
                    zz = y
                elif r == 2:  # 180 deg around x
                    xx = x
                    yy = -y
                    zz = -z
                elif r == 3:  # 270 deg around x
                    xx = x
                    yy = z
                    zz = -y
                elif r == 4:  # 90 deg around y
                    xx = z
                    yy = y
                    zz = -x
                elif r == 5:  # 270 deg around y
                    xx = -z
                    yy = y
                    zz = x
                rotated.append((xx, yy, zz))
            res.append(rotated)
    return res


scannerPositions = {(0, 0, 0)}

while unknownScanners:
    for beacon in fixed_beacons:
        for scanner in unknownScanners:
            found = False
            possible_scanner_rotations = orientation(scanner)
            for rotated_scan in possible_scanner_rotations:
                for rs_beacon in rotated_scan:
                    dx = beacon[0] - rs_beacon[0]
                    dy = beacon[1] - rs_beacon[1]
                    dz = beacon[2] - rs_beacon[2]
                    shifted_rotated_scan = {
                        (x + dx, y + dy, z + dz) for x, y, z in rotated_scan
                    }
                    intersection = shifted_rotated_scan.intersection(fixed_beacons)
                    if len(intersection) >= 12:
                        print("found ", dx, dy, dz)
                        fixed_beacons = fixed_beacons.union(shifted_rotated_scan)
                        unknownScanners.remove(scanner)
                        scannerPositions.add((dx, dy, dz))
                        found = True
                        break
                if found:
                    break

print("a)", len(fixed_beacons))

maxdist = 0
for s1 in scannerPositions:
    for s2 in scannerPositions:
        dist = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) + abs(s1[2] - s2[2])
        maxdist = max(dist, maxdist)
print("b)", maxdist)
