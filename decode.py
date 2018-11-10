def main():
    while True:
        curr_symbol = -1
        while curr_symbol == -1:
            bool = BitIO::input_bit()
            curr_symbol = Huffman::decode(bool)
        file.write(curr_symbol)
        if curr_symbol == HEOF: # Wait. Do we need to do ascii translations??
            break