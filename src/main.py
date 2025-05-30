import shutil
import os
import sys

# from generate_page import generate_page
from copystatic import copy_files_recursive
from generate_page_recursive_fn import generate_pages_recursive

dir_path_static = "./static"
# dir_path_public = "./public"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    # generate_page(
    #     os.path.join(dir_path_content, "index.md"),
    #     template_path,
    #     os.path.join(dir_path_public, "index.html"),
    # )

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()
