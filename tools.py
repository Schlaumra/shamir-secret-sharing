def format_poly(poly: list[int]):
    tmp = [*poly]
    msg = f"{tmp[0]}"
    for i in range(1, len(tmp)):
        msg = f"{tmp[i]}x^{i} + {msg}"
    return f"f(x) = {msg}"

def print_keys(keys):
    for i, x in keys:
        print(f"Secret {i}: {x} \t ({i}:{x})")

def print_hidden_step(step: int, *args):
    print(f"{step}: (HIDDEN) \t", *args)

def print_step(step: int, *args):
    print(f"{step}: \t\t", *args)
