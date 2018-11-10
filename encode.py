def main():
    file = open(file) #not really how this is done
    for char in file:
        bools_list = Huffman::encode(char)
        for bool in bools_list:
            BitIO::output_bit(bool)
    EOF_asboollist = Huffman::encode(Huffman::HEOF)
    for bool in EOF_asboollist:
        BitIO::output_bit(bool)

