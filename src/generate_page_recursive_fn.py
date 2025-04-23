import os

from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for filename in files:
            if filename.endswith(".md"):
                # for each markdown file found
                # generate a new .html file using the same
                # template.html
                # the generated pages should be written to the public
                # directory in the same directory structure
                source_path = os.path.join(root, filename)
                rel_path = os.path.relpath(source_path, dir_path_content)
                rel_html_path = rel_path.replace(".md", ".html")
                dest_path = os.path.join(dest_dir_path, rel_html_path)

                print(f"Generating: {source_path} -> {dest_path}")

                generate_page(source_path, template_path, dest_path)
