# import library for the Hash manipulation
# import library for system argument input

# define the blocksize for the chunk of input
# create a hash object with sha1 constructor

# open the argv 1 file with read-only & binary file options, creating a file handle
# read a block and save it to the buffer
# create a routine to calculate the hash value of the buffer and read another block until it reaches to the end of the file

# print file name and its SHA1 hash values
import hashlib
import sys

BLOCKSIZE = 1024
hasher = hashlib.sha1()

with open(sys.argv[1],'rb') as file:
	buf = file.read(BLOCKSIZE)
	while buf:
		hasher.update(buf)
		buf = file.read(BLOCKSIZE)
print("file name :{}		SHA1:{}".format(sys.argv[1],hasher.hexdigest()))
