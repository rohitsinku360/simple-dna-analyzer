
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
        print("length of sequence is",len(dna))

        # Count individual DNA bases (case-insensitive)
        A_count=dna.upper().count("A")
        T_count=dna.upper().count("T")
        G_count=dna.upper().count("G")
        C_count=dna.upper().count("C")
        print("count of A is",A_count)
        print("count of T is",T_count)
        print("count of G is",G_count)
        print("count of C is",C_count)
        
        # Relative frequency (%): (nucleotide count/total length of sequence)*100
        per="%"
        A_per=round((A_count/len(dna))*100,2)
        T_per=round((T_count/len(dna))*100,2)
        G_per=round((G_count/len(dna))*100,2)
        C_per=round((C_count/len(dna))*100,2)
        print(f"percentage of A is: {A_per}{per}")
        print(f"percentage of T is: {T_per}{per}")
        print(f"percentage of G is: {G_per}{per}")
        print(f"percentage of C is: {C_per}{per}")

        # Calculate GC percentage: (G + C) / total bases × 100
        gc_per=round(((dna.upper().count("G")+dna.upper().count("C"))/len(dna))*100,2)        
        print(f"GC content in sequence is: {gc_per}{per}")
                                                         
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
        
