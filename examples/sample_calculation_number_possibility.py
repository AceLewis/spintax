from spintax.spincalc import calculate_possibilities

if __name__ == "__main__":
    spin_example = "{{{A|B}|{C|D}{E|F|G}}|{H|I|{J|K|L}{M|N|O}}}"
    print(calculate_possibilities(spin_example))
