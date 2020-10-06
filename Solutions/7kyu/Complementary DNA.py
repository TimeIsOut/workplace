def DNA_strand(dna):
    dic = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return ''.join([dic[i] for i in dna])