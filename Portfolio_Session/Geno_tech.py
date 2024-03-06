'''
Challenge: Your task is to develop a DNA Sequence Analyser
Using advanced string functions, the program should identify
specific patterns, match them to known genetic markers, and even predict
possible traits based on these sequences
Allow the program to be capable of reading long DNA sequences, which
are essentially strings of nucleotides represented by the letters A, T, C,
and G.
○ Identify specific patterns, match them to known genetic markers, and
predict possible traits based on these sequences.
○ Additionally, the program should offer functionalities like converting the
entire sequence to uppercase for uniformity, replacing specific
nucleotide patterns, and splitting sequences based on certain markers

'''
# User input of the DNA sequence to investigate

dna_sequence = dna_sequence = str(input("Please input a DNA sequence:"))

# Change all the sequence to upper case
uppercase_sequence = dna_sequence.upper()

# Replace A with T
replace_sequence = uppercase_sequence.replace("A", "T")

print(f"""
        Original : {dna_sequence}
        Upper : {uppercase_sequence}
        Replaced : {replace_sequence}
        """
      )

# Genetic marker to investigate 
genetic_marker = input("Select the genetic marker you would to find: ").upper()
if genetic_marker in uppercase_sequence:
    print("Genetic marker found:", genetic_marker)
else: print("Marker not found")

# Splitting the sequence 
split_segment = input("Select the letter you would like to split by: ").upper()

segments = uppercase_sequence.split(split_segment)
print(f"Segments split by '{split_segment}'", segments)



trait_sequence = input("Select the trait sequence you would like to find: ").upper()
if trait_sequence in segments:
    print(f"Trait for sequence {trait_sequence} likely present.")
else: print(f"No trait sequence {trait_sequence} found")