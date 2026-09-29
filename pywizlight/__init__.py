from pythonforandroid.recipe import PythonRecipe


class PywizlightRecipe(PythonRecipe):
    name = "pywizlight"
    version = "v0.6.3"
    url = 'https://github.com/sbidy/pywizlight/archive/{version}.tar.gz'
    depends = ["click",]
    call_hostpython_via_targetpython = False


recipe = PywizlightRecipe()
