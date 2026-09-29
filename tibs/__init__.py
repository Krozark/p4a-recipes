from pythonforandroid.recipe import PythonRecipe


class TibsRecipe(PythonRecipe):
    name = "tibs"
    version = "0.6.0"
    url = "https://pypi.python.org/packages/source/t/tibs/tibs-{version}.tar.gz"
    depends = ["setuptools"]
    call_hostpython_via_targetpython = False


recipe = TibsRecipe()
