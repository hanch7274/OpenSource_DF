import hashlib
import sys

hasher = hashlib.md5()
BLOCKSIZE = 1024
with open(sys.argv[1],'rb') as file:
	buf = file.read(BLOCKSIZE)
	while buf:
		hasher.update(buf)
		buf = file.read(BLOCKSIZE)
print("file name: {}		MD5 sum value: {}".format(sys.argv[1],hasher.hexdigest()))
