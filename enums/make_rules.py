from enum import Enum


class MakeRules(Enum):
    all = "all"
    compile = "compile"
    build = "build"
    submit = "submit"
    release = "release"
    clean = "clean"

