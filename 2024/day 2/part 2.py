input_text = open("input.txt").readlines()

reports = [[int(num) for num in report.split(" ")] for report in input_text]

print(reports)

safe = 0
other_safe = 0
for report in reports:
    increasing = (report[0] - report[1]) < 0
    saveable_count = 0
    skip = False
    for i in range(len(report)-1):
        if skip:
            skip = False
            continue
        diff = report[i] - report[i+1]
        increasing_local = (report[i] - report[i+1]) < 0

        if (1 <= abs(diff) <= 3) and (increasing == increasing_local):
            continue
        elif abs(diff) == 0:
            saveable_count += 1
            if i == 0:
                increasing = (report[0] - report[2]) < 0
        elif i+2 == len(report) or 1 <= abs(report[i] - report[i+2]) <= 3 and (report[i] - report[i+2] < 0) == increasing:
            saveable_count += 1
            skip = True
        else:
            break
    else:
        if saveable_count == 0:
            safe += 1
        elif saveable_count == 1:
            other_safe += 1
            print(report, saveable_count)

print(safe)
print(other_safe)
print(safe + other_safe)
