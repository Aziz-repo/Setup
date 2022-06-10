from typing import Any
import os

def build_hiarchy(path: str, dirs: list, makefile: str, verbose:bool)-> int:
    try:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"{path} is created")
    except OSError as error:
        print("Direcotory '%s' cannot be created...")
        return 1
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
                return 1
        # Change the directory
        os.chdir(path)
        # Create the Makefile 
        try:
            open(makefile, 'a').close()
            if verbose:
                print("Makefile is created")
        except OSError as error_1:
            print("Makefile cannot be created...")
            return 1
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
        f"SRCS=$(wildcard $(SRC)/*.{lang}",
        f"OBJS=$(patsubt $(SRC)/%*.{lang}, $(OBJ)/%.o, $(SRCS))",
        "BIN=bin/"
        "BINDIR=bin"
    ]
    
    # try to write to the makefile
    try:
        with open("Makefile", "w") as fw:
            for instruction in instructions :
                fw.write(instruction)
    except :
        print("An error has occured! Please try again")
        return 1
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
            return 1
    return 0


            
            


    
        
        

        

