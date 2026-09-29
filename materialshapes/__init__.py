from pythonforandroid.recipe import PythonRecipe


class MaterialShapesRecipe(PythonRecipe):
    version = "0.3"
    url = "https://pypi.org/packages/source/m/materialshapes/materialshapes-{version}.tar.gz"
    depends = ["pillow"]
    site_packages_name = "materialshapes"
    call_hostpython_via_targetpython = False
    install_in_hostpython = True
    setup_extra_args = ["--no-deps"]


recipe = MaterialShapesRecipe()
