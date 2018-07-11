import hashlib
import sys

def multi_hash(filename):
	""" Calculates the md5 and sha256 hashes of the specified file and returns a list
		containing the hash sums as hex strings."""
	hash_md5 = hashlib.md5()
	hash_sha256 = hashlib.sha256()
	blocksize = 1024
	with open(filename,"rb") as file:
		buf = file.read(blocksize)
		while buf:
			hash_md5.update(buf)
			hash_sha256.update(buf)
			buf = file.read(blocksize)
	# Fill it up with codes
	return [hash_md5.hexdigest(), hash_sha256.hexdigest()]

if __name__ == '__main__':
	hashes = []
	hashes = multi_hash(sys.argv[1])
	print('---------- MD5 sums ----------')
	""" create for loop statement to get the file list from argument
		and calculate hash sums, store it to hashes array and
		print the MD5 hash sum with filename """
	print("{}\n".format(hashes[0]))
	print('---------- MD5 sums ----------')
	""" Create the for loop to get the value from hashes array
		and print SHA256 value with the argument(filename) """
	print("{}\n".format(hashes[1]))