import re

input_data = open("twelve.txt", "r").read()
matches = re.finditer(r"([.#?]+) ((?:\d+,?)+)", input_data)
def can_fit(match: str, groups: 'list[int]', offsets: 'list[int]'):
    chunks = [item for item in re.finditer(r"[#?]+", match)]

    print(groups)
    print(offsets)
    group = -1
    for chunk in reversed(chunks):
        i = 1
        search_start = chunk.end()
        while search_start - i >= chunk.start():
            if abs(group) > len(groups):
                break
            if match[search_start - i] == "#":
                # find the other side of the active group
                while match[search_start - i] == "#":
                    i += 1
                i -= 1

            
            if i > groups[group]: # you overshot
                #invalid!
                print("overshot")
                search_start = search_start - 1
                i = 0
                continue
            elif i == groups[group]:
                
                if search_start-i-1 >= 0 and match[search_start - i - 1] == "#":
                    print("oh fuckaroni you fucked up, gotta shift ur shit over")
                    search_start = search_start - 1
                    i = 0
                    continue
                print("matched")
                print("range:", search_start - i, search_start, "\n\n\n")
                # Yay! A valid match!
                search_start = search_start-i-1 # separation
                i = 0
                group -= 1
                continue
            i += 1
    if abs(group) < len(group):
        return 
            

for match in matches:
    offsetTarget = 2
    while True:
        groups = [int(num) for num in match.group(2).split(",")]
        for i, group in enumerate(groups):
            # set this group to target, then go through everything after it
            offsets = [offsetTarget if j == i else 0 for j in range(len(groups))]
            print(offsets)
        break
            
        
        offsets = [0 for group in groups]
        can_fit(match.group(1), groups, [0 for group in groups])