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


dna_sequence = dna_sequence = str(input("Please input a dna sequence:"))

uppercase_sequence = dna_sequence.upper()

replace_sequence = uppercase_sequence.replace("A", "T")

print(f"""
        Original : {dna_sequence}
        Upper : {uppercase_sequence}
        Replaced : {replace_sequence}
        """
      )

genetic_marker = input("Select the genetic marker you would to find: ").upper()
if genetic_marker in uppercase_sequence:
    print("Genetic marker found:", genetic_marker)
else: print("Marker not found")

split_segment = input("Select the letter you would like to split by: ").upper()

segments = uppercase_sequence.split(split_segment)
print(f"Segments split by '{split_segment}'", segments)


trait_sequence = "TAG"
if trait_sequence in segments:
    print(f"Trait for blue eyes {trait_sequence} likely present.")