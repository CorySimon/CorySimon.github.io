---
layout: post
title: Nested loops via recursion
excerpt: "An example of recursion"
comments: true
categories: articles
share: true
tags: [programming]
---

I encountered a problem where I needed to program a nested loop and wanted to share (code is in Julia).

*Problem:* We have a lattice with `n` ordered lattice sites, each of which are in state `-1` or `1`. There are thus $$2^n$$ distinct lattice states. My goal is to exhaustively enumerate each of these lattice states.

We can store the state of the lattice in an `n`-dimensional array of integers, `lattice_state`. For `n=2`, we can use a nested for loop to enumerate all lattice states. Each for loop represents a particular lattice site, or entry of `lattice_state`.

```Julia
n = 2
lattice_state = zeros(Int, n)
for i = [-1, 1]
    lattice_state[1] = i
    for j = [-1, 1]
        lattice_state[2] = j
        println(lattice_state)
    end
end
 # =>
 # [-1,-1]
 # [-1,1]
 # [1,-1]
 # [1,1]
```

When `n` gets large, this looks ugly because we need to write `n` nested loops:

```Julia
n = 4
lattice_state = zeros(Int, n)
for i = [-1, 1]
    lattice_state[1] = i
    for j = [-1, 1]
        lattice_state[2] = j
        for k = [-1, 1]
            lattice_state[3] = k
            for l = [-1, 1]
                lattice_state[4] = l
                println(lattice_state)
            end
        end
    end
end
 # =>
 # [-1,-1,-1,-1]
 # [-1,-1,-1,1]
 # [-1,-1,1,-1]
 # [-1,-1,1,1]
 # [-1,1,-1,-1]
 # [-1,1,-1,1]
 # [-1,1,1,-1]
 # [-1,1,1,1]
 # [1,-1,-1,-1]
 # [1,-1,-1,1]
 # [1,-1,1,-1]
 # [1,-1,1,1]
 # [1,1,-1,-1]
 # [1,1,-1,1]
 # [1,1,1,-1]
 # [1,1,1,1]
```

We can use a recursive algorithm instead to write a function for a general `n`:

```Julia
n = 8
lattice_state = zeros(Int, n)
function nested_loop(loop_level::Int)
    """
    Recursive algorithm to perform nested loop:
    for i = [-1, 1]
        lattice_state[1] = i
        for j = [-1, 1]
            lattice_state[2] = j
            .... n times
        end
    end

    Prints all possible lattice_state arrays.
    Parameters:
        loop_level, Int: level of nested loop we are in. Nested loop `loop_level` modifies entry `loop_level` in `lattice_state`. 
    """
    # if we are the last loop, print the array and return (do not go on)
    if (loop_level > n)
        println(lattice_state)
        return
    end
    # if we made it past this point, we need to continue going in the nested loop
    for i = [-1, 1]
        # modify entry loop_level
        lattice_state[loop_level] = i
        # with entry 1, 2, ..., loop_level fixed, call function again to go to next level in nested loop
        nested_loop(loop_level + 1)
    end
end
```

Now, I call the `nested_loop` function with `loop_level=1` to start at the first loop in the nest. It will then print all $$2^n$$ configurations of the lattice of length `n=8`, represented by unique `lattice_state` arrays:

```Julia
nested_loop(1)
```
