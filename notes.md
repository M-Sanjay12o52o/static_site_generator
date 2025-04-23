os.path.exists(path)

Return True if path refers to an existing path or an open file descriptor.
Return False for broken symbolic links.
FYI: On some platforms, this function may return False if permission
is not granted to execute os.stat() on the requested file,
even if the path physically exists.

os.listdir(path='.')

Returns a list containing the names of the entries in the directory given by path.
the list is in arbitrary order, and does not include the special entries
'.' and '..' even if they are present in the directory.
