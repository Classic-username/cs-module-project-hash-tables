# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

def crack_caesar(file):
    l_letters = {}
    frequency = {}

    frequency["E"] = 11.53
    frequency["T"] = 9.75
    frequency["A"] = 8.46
    frequency["O"] = 8.08
    frequency["H"] = 7.71
    frequency["N"] = 6.73
    frequency["R"] = 6.29
    frequency["I"] = 5.84
    frequency["S"] = 5.56
    frequency["D"] = 4.74
    frequency["L"] = 3.92
    frequency["W"] = 3.08
    frequency["U"] = 2.59
    frequency["G"] = 2.48
    frequency["F"] = 2.42
    frequency["B"] = 2.19
    frequency["M"] = 2.18
    frequency["Y"] = 2.02
    frequency["C"] = 1.58
    frequency["P"] = 1.08
    frequency["K"] = 0.84
    frequency["V"] = 0.59
    frequency["Q"] = 0.17
    frequency["J"] = 0.07
    frequency["X"] = 0.07
    frequency["Z"] = 0.03

    with open(file) as f:
        data = f.read()
    
    total_no_of_letters = 0

    for c in data:
        if c.isalpha() and c in l_letters:
            l_letters[c] += 1
            total_no_of_letters += 1
        elif c.isalpha():
            l_letters[c] = 1
            total_no_of_letters += 1

    for letter in l_letters:
        l_letters[letter] = round(((l_letters[letter]/total_no_of_letters) * 100), 2)

    encrypted_letter_frequency = list(l_letters.items())
    provided_letter_frequency = list(frequency.items())

    encrypted_letter_frequency.sort(key=lambda x: x[1], reverse=True)
    provided_letter_frequency.sort(key=lambda x: x[1], reverse=True)

    encrypted_array = []
    provided_array = []

    for i, (x, z) in enumerate(encrypted_letter_frequency):
        encrypted_array.append(x)

    for i, (x, z) in enumerate(provided_letter_frequency):
        provided_array.append(x)

    dict_map = dict(zip(encrypted_array, provided_array))

    content = ''

    for i in range(len(data)):
        if data[i].isalpha() and data[i] in dict_map:
            content += dict_map[data[i]]
        else:
            content += data[i]

    print(content)


print(crack_caesar('applications/crack_caesar/ciphertext.txt'))