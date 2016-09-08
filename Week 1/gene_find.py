geneString = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA";

def extractGenes(gene):
    output = [];
    geneStart = gene.split("ATG");
    for genepart in geneStart:
        if("TAG" in genepart):
            output.append(genepart.split("TAG"));
        elif "TAA" in genepart:
            output.append(genepart.split("TAA"));
        elif "TGA" in genepart:
            output.append(genepart.split("TGA"));

    length = len(output);
    index = 0;
    while index < length:
        if("ATG" not in output[index] or "TAG" not in output[index] or "TAA" not in output[index] or "TGA" not in output[index] and float(len(output[index]) / 3).is_integer()):
            del output[index];
            length = length - 1;
        index = index + 1;

    return output;


print(extractGenes(geneString));