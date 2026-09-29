from pythonforandroid.recipe import PyProjectRecipe


class PydanticRecipe(PyProjectRecipe):
    version = "2.12.2"
    url = "https://pypi.python.org/packages/source/p/pydantic/pydantic-{version}.tar.gz"
    site_packages_name = "pydantic"
    depends = [
        "setuptools",
        "cython",
        "annotated-types",
        "pydantic_core",
        "typing_extensions",
        "typing-inspection",
    ]
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = PydanticRecipe()
