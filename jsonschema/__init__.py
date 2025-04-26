from pythonforandroid.recipe import PythonRecipe


class JsonschemaRecipe(PythonRecipe):
    version = "4.23.0"
    url = "https://github.com/python-jsonschema/jsonschema/archive/refs/tags/v{version}.tar.gz"
    name = "jsonschema"
    install_in_hostpython = True

    depends = [
        "jsonschema-specifications",
        "rpds-py",
        "attrs",
        "referencing",
        "typing_extensions",
    ]

    def build_arch(self, arch):
        super().build_arch(arch)
        # Trick pour installer proprement un package avec pyproject
        # hostpython = self.get_hostpython(arch)
        # env = self.get_recipe_env(arch)
        # build_dir = self.get_build_dir(arch)
        # self.ctx.create_hostpython_virtualenv()
        # self.ctx.hostpython_virtualenv_pip_install(build_dir)


recipe = JsonschemaRecipe()
