# Brainstorming

Maybe multiply until `current > target`, then backtrack one, add until `current > target` or you reach the end and `current == target`. If either of those happen then... Backtrack again? Maybe?

Another possibility is to find target numbers along the way? I could do that by getting factors of `target`. Then you filter the list to find the ones that are factors. (Actually do that the other way around. Divide `target` by `num` and check if it's a whole number.)

I think working backwards is actually the best way to go. Check if the number at the end is a factor of target and if it's not then you subtract from target, and new target is the result. Then you like... Keep going? I guess?

Ok but how do I find *all* the solutions?

Ok what about factors, then factors of factors?

## Constructing A Binary Tree?

Let's say left branch is multiplication, that branch is invalid if current * left branch > target
