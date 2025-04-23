import os
import shutil


def test():
    # testing
    path = "/Users/msanjayachar/Desktop/workspace/boot-dot-dev/static_site_generator/static"
    result = os.path.exists(path)
    print("result: ", result)
    # returns True

    # returns a list containing the names of the entries in the directory
    result_list = os.listdir(path)
    print("result_list: ", result_list)
    # returns [".DS_Store", "images", "index.css"]

    # join one or more path segments intelligently
    # the result value is the concatenation of path and all members of *paths
    # example usage os.path.join(path, *paths) -> *paths is a variadic argument
    # (a tuple of arguments). it means you can pass multiple path segments, like this
    # os.path.join("home", "user", "documents", "file.txt")
    # is equivalent to
    # os.path.join("home", *["user", "documents", "file.txt"])
    path1 = "home"
    path_join = os.path.join(path1, *["sanjay", "projects", "clarityboard"])
    print("path_join: ", path_join)
    # returns home/sanjay/projects/clarityboard

    # returns true if path is an existing regular file
    path_to_file = "/Users/msanjayachar/Desktop/workspace/boot-dot-dev/static_site_generator/static/images/tolkien.png"
    path_isfile_result = os.path.isfile(path_to_file)
    print("path_isfile_result: ", path_isfile_result)
    # returns True

    # creates a directory named path with numeric mode mode
    # if the directory already exists, fileExistsError is raised.
    # If a parent directory in the path does not exist, FileNotFoundError is raised
    # FYI: to create nested folders use os.makedirs() instead
    # / output_dir = "public"
    #
    # if not os.path.exists(output_dir):
    #     os.mkdir(output_dir)
    #
    # target_path = "public/assets/images"
    # os.makedirs("public/assets/images", exist_ok=True)
    # print(f"Created or confirmed existing directory: {target_path}")

    # target = "public/assets"
    #
    # if os.path.exists(target):
    #     shutil.rmtree(target)
    #     print(f"Deleted existing directory: {target}")

    # shutil.copy(src, dst, *, follow_symlinks=True)
    # shutil.copytree(src, dst, dirs_exist_ok=True)
    # copies all files and sub-directories from src to dst
    src = "/Users/msanjayachar/Desktop/workspace/boot-dot-dev/static_site_generator/static/index.css"
    dst = "/Users/msanjayachar/Desktop/workspace/boot-dot-dev/static_site_generator/public"

    shutil.copy(src, dst, follow_symlinks=True)

    path_to_public = "/Users/msanjayachar/Desktop/workspace/boot-dot-dev/static_site_generator/public"

    # shutil.rmtree
    if os.path.exists(path_to_public):
        shutil.rmtree(path_to_public)
        print(f"Deleted directory: {path_to_public}")
    else:
        print(f"Directory does not exist: {path_to_public}")


test()
