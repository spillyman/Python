# starting with a DNA sequence
# the DNA sequence will be coded into an RNA strand
import re
import string

dna = input("Input DNA strand: ")

# To properly display the dna sequence formatting needs to be applied
# Special characters and numbers must also be taken out, because they cannot be transcribed/translated

dna = re.sub('[^A-Za-z]+', '', str(dna)).upper()
redna = ' '.join([dna[i:i+3] for i in range(0, len(dna), 3)])
print("DNA strand to be transcribed: " + str(redna))

# Transcribing dna will now occur by iterating through dna
rna = ""
for i in dna:
    if i == 'A':
        rna += 'U'
    elif i == 'T':
        rna +=  'A'
    elif i == 'C':
        rna +=  'G'
    elif i == 'G':
        rna += 'C'

# complete name form
mapC = {"UUU":"Phenyl-alinine", "UUC":"Phenyl-alinine", "UUA":"Leucine", "UUG":"Leucine",
       "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine",
       "UAU":"Tyrosine", "UAC":"Tyrosine", "UAA":"STOP Codon", "UAG":"STOP Codon",
       "UGU":"Cysteine", "UGC":"Cysteine", "UGA":"STOP Codon", "UGG":"Tryptophan",
       "CUU":"Leucine", "CUC":"Leucine", "CUA":"Leucine", "CUG":"Leucine",
       "CCU":"Proline", "CCC":"Proline", "CCA":"Proline", "CCG":"Proline",
       "CAU":"Histidine", "CAC":"Histidine", "CAA":"Glutamine", "CAG":"Glutamine",
       "CGU":"Arginine", "CGC":"Arginine", "CGA":"Arginine", "CGG":"Arginine",
       "AUU":"Isoleucine", "AUC":"Isoleucine", "AUA":"Isoleucine", "AUG":"Methionine (Start Codon)",
       "ACU":"Threonine", "ACC":"Threonine", "ACA":"Threonine", "ACG":"Threonine",
       "AAU":"Asparagine", "AAC":"Asparagine", "AAA":"Lysine", "AAG":"Lysine",
       "AGU":"Serine", "AGC":"Serine", "AGA":"Arginine", "AGG":"Arginine",
       "GUU":"Valine", "GUC":"Valine", "GUA":"Valine", "GUG":"Valine",
       "GCU":"Alanine", "GCC":"Alanine", "GCA":"Alanine", "GCG":"Alanine",
       "GAU":"Aspartic Acid", "GAC":"Aspartic Acid", "GAA":"Glutamic Acid", "GAG":"Glutamic Acid",
       "GGU":"Glycine", "GGC":"Glycine", "GGA":"Glycine", "GGG":"Glycine",}

# symbol name form
mapS = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

# Again properly formatting the sequence for display
printrna = ' '.join(rna[i:i+3] for i in range(0, len(dna), 3))
print("Transcribed mRNA sequence: " + printrna)

t = "AUG"
# start codon defined
start = rna.find(t)

# -1 will occur if there is no start codon in the sequence
if start == -1:
    print("No Start Codon")
else:
    print("Position: " + str(int(rna.find(t) + 1)))

# symbol or name choice
mapPoly = input("Type S (Symbol nucleotide form) or C (Complete nucleotide name form): ").upper()


if mapPoly == 'S' :
    mapP = mapS
else:
    mapP = mapC

print("Translation to polypeptide chain...")

if start != -1:
    x = 1
    print("Translated mRNA to polypeptide sequences beginning at start codon: ")
    while start+2 < len(dna): #if strand is larger than 3
        codon = rna[start: start + 3]
        print(str(x) + ': ' + str(mapP[codon]))
        if codon == "UAA" or codon == "UAG" or codon == "UGA" :
            break
        start += 3
        x += 1
else:
    i = 0
    x = 1
    print("Translated RNA protein sequences:")
    while i+2 < len(dna):
        codon = rna[i: i+3]
        print(str(x) + ': ' + str(mapP[codon]))
        i += 3
        x += 1

if start != -1:
    whole_strand = input('Would you like the whole strand transcribed also? Y/N: ')
    if whole_strand == 'Y':
        i = 0
        x = 1
        while i+2 < len(dna):
            codon = rna[i: i+3]
            print(str(x) + ': ' + str(mapP[codon]))
            i += 3
            x += 1