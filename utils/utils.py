from typing import Tuple
import os
from enums.cflags import Cflags
from enums.compiler import Compiler


def build_hiarchy(path: str, dirs: list, makefile: str, verbose:bool)-> int:
    try:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"{path} is created")
    except OSError as error:
        print("Direcotory '%s' cannot be created...")
        raise 1
    else:
        # Create the src, obj, bin subdirectories
        for dir in dirs:
            sub_path = os.path.join(path,dir)
            try:
                os.makedirs(sub_path)
                if verbose:
                    print(f"subdirectories is created")
            except OSError as error_2:
                print("Sub directories cannot be created...")
                raise 1
        # Change the directory
        os.chdir(path)
        # Create the Makefile 
        try:
            open(makefile, 'a').close()
            if verbose:
                print("Makefile is created")
        except OSError as error_1:
            print("Makefile cannot be created...")
            raise 1
    return 0

def write_to_makefile(lang_code: int) -> int:
    if lang_code == 0:
        lang = 'c'
    else:
        lang = 'cpp'
    
    instructions = ["CC=\n",
        "CFLAGS=\n",
        "SRC=src\n",
        "OBJ=obj\n",
        f"SRCS=$(wildcard $(SRC)/*.{lang}\n",
        f"OBJS=$(patsubt $(SRC)/%*.{lang}, $(OBJ)/%.o, $(SRCS))\n",
        "BIN=bin/\n"
        "BINDIR=bin\n"
    ]
    
    # try to write to the makefile
    try:
        with open("Makefile", "w") as fw:
            for instruction in instructions :
                fw.write(instruction)
    except :
        print("An error has occured! Please try again")
        raise 1
    return 0
    


def create_main(lang: int) -> int:
    c = ["#include <stdlib.h>\n", 
        "#include <stdio.h>\n", 
        "\n\n", 
        "int main(int argc, char** argv) {",
        "\n\n",
        "return 0\n;",
        "}"]
    
    cpp = ["#include <iostream.h>\n",
          "#include <string.h\n",
          "\n\n",
          "int main(int argc, char** argv) {",
          "\n\n",
          "return 0;\n",
          "}"]

    if lang == 0: 
        # create C file and write to it
        try:
            with open("main.c", 'w') as fw:
                for instruction in c:
                    fw.write(instruction)
        except :
            print("An error has occured! Please try again...\n")
            return 1
    else:
        # create Cpp file and write to it
        try:
            with open("main.cpp", 'w') as fw:
                for instruction in cpp:
                    fw.write(instruction)
        except :
            print("An error has occured! Please try again...\n")
            raise 1
    return 0

def makefile_debug(compiler: Compiler, cflags: Cflags) -> int:
    try:
        with open("Makefile", "r") as f:
            lines = [line.rstrip for line in open("Makefile", 'r')]
        
        lines[0] = lines[0] +  str(compiler.value)
        lines[1] = lines[1] + str(cflags.value)

        with open("Makefile", "w") as f:
            for line in lines:
                f.write(line+"\n")
    except:
        print("An error occured writting to the Makefile")
        raise 1
    return 0

def add_header_file(path: str,header_file : Tuple[str,str,str]) -> int:
    # changing to the main path
    os.chdir(os.path.join(path, "/src"))
    # check if files have .h in them -> if not add the extention
    for i,header in enumerate(header_file):
        if header[-2:] != ".h":
            header = str(header) + ".h"
            header_file[i] = header 
    # create the files provided
    for header in header_file :
        try:
            open(header, 'a').close()
        except:
            return 1
        else:
            return 0

def add_source_file(path: str, source_file: Tuple[str,str,str], lang_code: int) -> int:
    lang_code_dict = {0: ".c", 1: ".cpp"}
    # changing to the main path
    os.chdir(os.path.join(path, "/src"))
    # check if files have .c in them -> if not add the extention
    for i, source in enumerate(source_file):
        if source[-2:] !=  lang_code_dict[lang_code] :
            source = str(source) + str(lang_code_dict[lang_code])
            source_file[i] = source
    # create the files provided
    for source in source_file:
        try:
            open(source, 'a').close()
        except:
            return 1
        else:
            return 0

              
            


    
        
        

        

