def string():
    M = int(input("Введите количество строк: "))
    strings = [input(f"Введите строку {i + 1}: ") for i in range(M)]
    return strings

def get_max_strigs(strings):
    max_strigs = max(len(s) for s in strings)
    return max_strigs

def pad_strings(strings,max_strigs):
    padded_strings = []
    for s in strings:
        num_stars = max_strigs - len(s)
        padded_strings.append("*" * num_stars + s)
    return padded_strings
    
def main():
    strings = string()
    max_strigs = get_max_strigs(strings)
    padded_strings = pad_strings(strings,max_strigs)
    print("\nВыровниные строки: ")
    for s in padded_strings:
        print(s)
        

main()

