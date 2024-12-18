input_text = open("input.txt").readlines()

reports = [[int(num) for num in report.split(" ")] for report in input_text]

print(reports)

def is_safe(report):
    increasing = (report[0] - report[1]) < 0
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        increasing_local = (report[i] - report[i+1]) < 0

        if (1 <= abs(diff) <= 3) and (increasing == increasing_local):
            continue
        else:
            break
    else:
        return True
    return False

safe = 0
other_safe = 0
for report in reports:
    if is_safe(report):
        safe += 1
    else:
        for i in range(len(report)):
            copy = report.copy()
            del copy[i]
            if is_safe(copy):
                print(report)
                other_safe += 1
                break

print(safe)
print(other_safe)
print(safe + other_safe)
