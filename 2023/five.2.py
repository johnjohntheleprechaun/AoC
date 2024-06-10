import re

# load data
data = open("five.txt", "r").read()
seed_data = [int(num) for num in re.match(r"seeds: ((?:\d+ ?)+)", data).group(1).split(" ")]
seeds = []
# generate seed ranges
for i in range(0, len(seed_data), 2):
    seeds.append([seed_data[i], seed_data[i+1]])
map_regex = r"(.+)-to-(.+) map:\n((?:(?:\d+ ?)+\n?)+)"
maps_data = re.finditer(map_regex, data, re.MULTILINE)
maps = []
for map in maps_data:
    ranges = [[int(num) for num in item.split(" ")] for item in filter(lambda a: a != "", re.split(r"\n+", map.group(3)))]

    ranges.sort(key=lambda a: a[1])

    maps.append({
        "from": map.group(1),
        "to": map.group(2),
        "ranges": ranges
    })


# use data
def get_map(source):
    for map in maps:
        if map["from"] == source:
            return map

def convert(source, target, seed_range):
    if source == target:
        return seed_range[0]
    # find start
    start_map = get_map(source)

    # find the range to use
    next_ranges = []
    for range in start_map["ranges"]:
        if seed_range[0] >= range[1] and seed_range[0] < range[1] + range[2]:
            # start with this range
            if range[1] + range[2] < seed_range[0] + seed_range[1]: # end of range < end of seed range
                # the conversion range doesn't fully encompass the seed range
                # append the truncated range
                new_start = range[0] - range[1] + seed_range[0] # the difference between the source and destination, added to the seed start
                new_length = range[0] + range[2] - new_start # the original end, minus the new start
                next_ranges.append([
                    new_start,
                    new_length
                ])

                # edit seed range
                seed_start = range[1] + range[2] # the end of the range
                seed_length = seed_range[0] + seed_range[1] - seed_start
                seed_range[0] = seed_start
                seed_range[1] = seed_length
            
            elif range[1] + range[2] >= seed_range[0] + seed_range[1]:
                # fully encompassed
                next_ranges.append([
                    seed_range[0] + range[0] - range[1],
                    seed_range[1]
                ])
                break
    else:
        # not mapped, so no conversion
        next_ranges.append(seed_range)
        
    converted = []
    for range in next_ranges:
        converted.append(convert(start_map["to"], target, range))
    
    # do something with converted
    return min(converted)

lowest = []
for seed in seeds:
    lowest.append(convert("seed", "location", seed))
print(min(lowest))