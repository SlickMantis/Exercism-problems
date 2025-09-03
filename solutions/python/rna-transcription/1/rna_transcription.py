def to_rna(dna_strand):
    DNA = ["A","C","G","T"]
    RNA = ["A","C","G","U"]
    transcribed_RNA = []

    for nucleotide in dna_strand.upper():
        if nucleotide == DNA[0]:
            transcribed_RNA.append(RNA[3])
        elif nucleotide == DNA[1]:
            transcribed_RNA.append(RNA[2])
        elif nucleotide == DNA[2]:
            transcribed_RNA.append(RNA[1])
        elif nucleotide == DNA[3]:
            transcribed_RNA.append(RNA[0])
    return "".join(transcribed_RNA)
