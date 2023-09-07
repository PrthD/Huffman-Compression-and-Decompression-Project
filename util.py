"""
--------------------------------------------
Name: Parth Dadhania
SID: 1722612
CCID: pdadhani
AnonID: 1000330704
CMPUT 274, Fall 2022
Assessment: Assignment #2: Huffman Coding
--------------------------------------------
"""

import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    # using pickle module to load the huffman tree object
    return(pickle.load(tree_stream))


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    # iterating until 'tree' is object of class TreeLeaf and not TreeBranch
    while isinstance(tree, huffman.TreeBranch):
        # If bit = 1, go to the right from branch node
        if bitreader.readbit():
            tree = tree.getRight()
        # Else (when bit = 0), go to the left from branch node
        else:
            tree = tree.getLeft()
    return(tree.getValue())


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''

    tree = read_tree(compressed)

    # Instance to read bits from the "compressed" file
    comp_bits = bitio.BitReader(compressed)
    # Instance to write bits to the "uncompressed" file
    uncomp_bits = bitio.BitWriter(uncompressed)

    # check for End of file
    EOF = False
    while not EOF:
        decoded_bits = decode_byte(tree, comp_bits)
        if decoded_bits is None:
            EOF = True
        else:
            uncomp_bits.writebits(decoded_bits, 8)
    # forcing any bits waiting in buffer to output stream
    uncomp_bits.flush()


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    # using pickle module to write (dump) the huffman tree to a binary file
    pickle.dump(tree, tree_stream)


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''

    write_tree(tree, compressed)

    # creating instance to read bits from the "uncompressed" file
    read_bits = bitio.BitReader(uncompressed)
    # creating instance to write bits to the "compressed" file
    write_bits = bitio.BitWriter(compressed)

    # generating an encoding table which will mapping each leaf node
    # to its corresponding bit sequence in the tree
    encoding_table = huffman.make_encoding_table(tree)

    # check for End of file
    EOF = False
    while not EOF:
        try:
            read_byte = read_bits.readbits(8)
            encoded_byte = encoding_table[read_byte]
            # iterates through the encoded byte made from encoding table
            for bit in encoded_byte:
                write_bits.writebit(bit)
    # handles End of file error and flips EOF to True
        except EOFError:
            EOF = True
    # once EOFError has occured, corresponding encoded bits for None
    # are wrote at the last of file
    encoded_byte = encoding_table[None]
    for bit in encoded_byte:
        write_bits.writebit(bit)

    # forcing any bits waiting in buffer to output stream
    write_bits.flush()
