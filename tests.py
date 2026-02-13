import os

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    # working_dir = "calculator"
    # root_contents = get_files_info(working_dir)
    # print(root_contents)
    # pkg_contents = get_files_info(working_dir,"pkg")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir,"/bin")
    # print(pkg_contents)
    # pkg_contents = get_files_info(working_dir,"../")
    # print(pkg_contents)
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "pkg/notexists.py"))
    # print(get_file_content(working_dir, "/bin/cat"))
    working_directory = "calculator"
    # print(write_file(working_directory, "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file(working_directory, "pkg/morelorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file(working_directory, "pkg2/temp.txt", "this should be  allowed"))


if __name__ == "__main__":
    main()
