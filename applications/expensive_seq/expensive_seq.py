# Your code here
import codecs

# ```
# exps(x, y, z) =
#      if x <= 0: y + z
#      if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
# ```

cache = {}

def expensive_seq(x, y, z):
    # Your code here
    key = f"({x}, {y}, {z}"

    if key not in cache:
        if x <= 0:
            result = y + z
        if x > 0:
            result = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        cache[key] = result

    return cache[key]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))



print(codecs.encode('Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr... vapyhqvat n ghcyr, and JavaScript', 'rot_13'))