input_text = open("input.txt").readlines()

reports = [[int(num) for num in report.split(" ")] for report in input_text]

print(reports)

safe = 0
for report in reports:
    increasing = (report[0] - report[1]) < 0
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        increasing_local = (report[i] - report[i+1]) < 0

        if (1 <= abs(diff) <= 3) and (increasing == increasing_local):
            continue
        else:
            break
    else:
        safe += 1

print(safe)
