import itertools

input_text = open("input.txt").read()
data = []

for i in range(0, len(input_text), 2):
    batch = input_text[i:i+2]
    data.append([int(i / 2), int(batch[0]), 0 if batch[1] == "\n" else int(batch[1])])

def stringify(data_to_log, readable=True):
    if readable:
        return "".join((f"[{batch[0]}]" * batch[1]) + "[.]" * batch[2] for batch in data_to_log)
    else:
        return "".join((f"{batch[0]}" * batch[1]) + "." * batch[2] for batch in data_to_log)

#print(stringify(data, False))

target = 9999

while target >= 0:
    index = next((i for i, x in enumerate(data) if x[0] == target))
    file = data[index]
    j = 0
    while data[j][0] != target:
        if data[j][2] >= file[1]:
            data.insert(j+1, [file[0], file[1], data[j][2] - file[1]])
            data[j][2] = 0
            data[index][2] += file[1] + file[2]
            del data[index+1]
            #print(stringify(data, False))
            break
        j += 1
    target -= 1

# now to calc checksum
#print(stringify(data))
checksum = 0
file = open("out2.txt", "w")
for i, num in enumerate(stringify(data)[1:-1].split("][")):
    if num == ".":
        continue
    checksum += i * int(num)
    file.write(f"{num} * {i} => {checksum}\n")

print(f"checksum: {checksum}")
