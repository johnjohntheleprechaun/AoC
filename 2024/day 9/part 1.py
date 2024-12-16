import itertools

input_text = open("input.txt").read()
data = []

for i, batch in enumerate(itertools.batched(input_text, 2)):
    data.append([i, int(batch[0]), 0 if batch[1] == "\n" else int(batch[1])])

def stringify(data_to_log, readable=True):
    if readable:
        return "".join((f"[{batch[0]}]" * batch[1]) + "[.]" * batch[2] for batch in data_to_log)
    else:
        return "".join((f"{batch[0]}" * batch[1]) + "." * batch[2] for batch in data_to_log)

i = 0
while True:
    if i >= len(data):
        break
    batch = data[i]
    last = data[-1]
    if batch[2] == 0:
        i += 1
        continue

    # empty > full
    if batch[2] > last[1]:
        # [ index, count]
        data.insert(i+1, [last[0], last[1], batch[2] - last[1]])
        data[i][2] = 0
        del data[-1]
    elif batch[2] < last[1]:
        data.insert(i+1, [last[0], batch[2], 0])
        data[-1][1] = last[1] - batch[2]
        data[i][2] = 0
    else:
        data.insert(i+1, [last[0], last[1], 0])
        del data[-1]
        data[i][2] = 0

    i += 1

# now to calc checksum
checksum = 0
for i, num in enumerate(stringify(data)[1:-1].split("][")):
    checksum += i * int(num)

print(f"checksum: {checksum}")
