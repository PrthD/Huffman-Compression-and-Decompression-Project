
# Huffman Compression and Decompression Project

## Overview
This project implements Huffman compression and decompression. It includes a web server that allows users to view compressed files through a browser. The compressed files are served by the web server, and the web interface allows them to be accessed locally.

## Project Structure
The project is organized into the following directories:

- **/src/**:
   - `bitio.py` - Handles bitwise reading and writing
   - `compress.py` - Contains the logic to compress files
   - `decompress.py` - Contains the logic to decompress files
   - `huffman.py` - Used to create Huffman trees and encode/decode messages
   - `util.py` - Contains helper functions used for compression and decompression
   - `webserver.py` - Web server to display compressed files in a browser
   - `version.py` - Version information for the project
- `README.md` - Documentation for the project

## Installation and Setup
To set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/huffman-compression.git
   cd huffman-compression
   ```

2. Install required dependencies:
   The project runs on Python 3 and does not require any external dependencies, apart from standard libraries.

3. Run the web server:
   Run the web server from the root of the project:
   ```bash
   python3 src/webserver.py
   ```

   The server will start, and you can view the compressed files in your browser at:
   ```
   http://localhost:8000
   ```

   To change the port, modify the `port` variable in `src/webserver.py`.

## Running the Code

### Compress a File
To compress a file, use the following command:
```bash
python3 src/compress.py yourfile.ext
```
Where `yourfile.ext` is the name of the file you wish to compress.

### Decompress a File
To view a decompressed file, navigate to the following URL in your browser:
```
http://localhost:8000/yourfile.ext
```

The file will be displayed or downloaded depending on the file type.
