
# Simple DNA Analyzer

# List of valid DNA bases
sequence=["A", "T", "G", "C"]

# Flag used for DNA validation and loop control
valid = True

while valid:

    # Take DNA sequence as input
    dna=input("DNA sequence: ")

    # Check whether every character is a valid DNA base
    for i in dna:
        if i.upper() not in sequence:
            valid=False
            break

    # Analyze the sequence if it is valid and non-empty
    if valid and len(dna)>0:

        # Calculate and display the total sequence length
        print("length of", dna,"is",len(dna))

        # Count individual DNA bases (case-insensitive)
        print("count of A is",dna.upper().count("A"))
        print("count of T is",dna.upper().count("T"))
        print("count of G is",dna.upper().count("G"))
        print("count of C is",dna.upper().count("C"))

        # Calculate GC percentage: (G + C) / total bases × 100
        print("GC percentage in sequence is",((dna.upper().count("G") + dna.upper().count("C"))/ len(dna))*100)

        # Prompt the user to enter another sequence
        print("enter new sequence")

    # Handle empty input
    elif len(dna)<=0:
        print("no sequence detected")

    # Handle invalid DNA characters
    else:
        valid=True
        print("invalid input!")
        print("enter new sequence")
