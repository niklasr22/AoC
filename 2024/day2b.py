from pathlib import Path
reports = Path("2024/inputs/day2.txt").read_text().strip().splitlines()

safe = 0
for report in reports:
    report_base = list(map(int, report.split(" ")))

    any_ok = False
    for i,_ in enumerate(report_base):
        report = report_base.copy()
        report.pop(i)

        if sorted(report) != report and sorted(report, reverse=True) != report:
            continue

        comp = report[0]
        dist_ok = True
        for num in report[1:]:
            if not(0 < abs(comp - num) < 4):
                dist_ok = False
                break
            comp = num
        if dist_ok:
            any_ok = True
            break

    if any_ok:
        safe += 1
print(safe)