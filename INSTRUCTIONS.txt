HUFFMAN ASSIGNMENT: VERSION FOR FALL 2022

*** NOTE:  To avoid using symbolic links, there may be multiple copies
	of the same file, but with different names.

Included Files:
- Makefile: automatically start web server, various tests
- bitio.py: Contains the classs BitWriter and BitReader
- compress.py: Runs the code to compress a file.
- decompress.py: Runs the code to decompress a file.
- huffman.py: Used to create huffman trees as well as encode and decode messages.
- webserver.py: The file that allows viewing of the compressed files as they are being sent to the web browser
- test.1.txt, arrow.png, oval.png, etc: various test files that should compress
- wwwroot directory: contains compressed versions of the webpage (index.html.huf) and the image of Huffman (huffman.bmp.huf)

Modified Files:
- util.py: Contains the five functions read_tree(), decode_byte(), write_tree(), compress(), and decompress() which students must implement.

Running the code:
Go to the wwwroot directory. Open a bash terminal and open the web server using "python3 ../webserver.py". You can then go to the url "http://localhost:8000" to view the webpage and image of Huffman that will appear if the decompressor is functioning properly. Note that the port can be changed by modifying the variable port in webserver.py.

To compress a file, first copy that file over to the wwwroot directory and then move to that directory and type "python3 ../compress.py somefile.ext" where somefile is the name of the file you wish to compress and ext is the extension. Then go to the url "http://localhost:8000/somefile.ext" to view and/or download the decompressed file.
