import re

# load data
data = open("five.txt", "r").read()
seeds = [int(num) for num in re.match(r"seeds: ((?:\d+ ?)+)", data).group(1).split(" ")]

print(seeds)
map_regex = r"(.+)-to-(.+) map:\n((?:(?:\d+ ?)+\n?)+)"
maps_data = re.finditer(map_regex, data, re.MULTILINE)
maps = []
for map in maps_data:
    ranges = [[int(num) for num in item.split(" ")] for item in filter(lambda a: a != "", re.split(r"\n+", map.group(3)))]

    maps.append({
        "from": map.group(1),
        "to": map.group(2),
        "ranges": ranges
    })
print(maps)


# use data
def get_map(source):
    for map in maps:
        if map["from"] == source:
            return map

def convert(source, target, value):
    if source == target:
        return value
    # find start
    start_map = get_map(source)

    # find the range to use
    converted = value
    for range in start_map["ranges"]:
        if value >= range[1] and value < range[1] + range[2]:
            converted = range[0] + value - range[1]
    
    return convert(start_map["to"], target, converted)

converted = []
for seed in seeds:
    converted.append(convert("seed", "location", seed))

print(min(converted))