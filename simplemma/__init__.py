from pythonforandroid.recipe import PyProjectRecipe


class SimplemmaRecipe(PyProjectRecipe):
    version = "main"
    url = "https://github.com/Krozark/simplemma/archive/refs/heads/{version}.tar.gz"
    name = "simplemma"
    depends = [
        "liblzma",
    ]


recipe = SimplemmaRecipe()
