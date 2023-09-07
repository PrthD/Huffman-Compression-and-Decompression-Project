import sys
import util


def run_decompressor (filename):
    with open(filename, 'rb') as compressed:
        with open(filename+'.decomp', 'wb') as uncompressed:
                util.decompress(compressed, uncompressed)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <file1> <file2> ...".format(sys.argv[0]))
    else:
        for filename in sys.argv[1:]:
            print ("Decompressing '{0}' to '{0}.decomp'".format(filename))
            run_decompressor(filename)
