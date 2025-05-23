from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class SpacyRecipe(CompiledComponentsPythonRecipe):
    version = "3.3.0"
    url = "https://pypi.python.org/packages/source/s/spacy/spacy-{version}.tar.gz"
    site_packages_name = "spacy"
    depends = [
        "setuptools",
        "cython",
        # Explosion-provided dependencies
        "spacy-legacy",
        "spacy-loggers",
        "cymem",
        "click",
        "preshed",
        "thinc",
        "blis",
        "markupsafe",
        "ml_datasets",
        "murmurhash",
        "wasabi",
        "srsly",
        "catalogue",
        "typer",
        "pathy",
        # Third party dependencies
        "numpy",
        "requests",
        "urllib3",
        "tqdm",
        "pydantic",
        "jinja2",
        "langcodes",
        # Official Python utilities
        "packaging",
        # # Required for Russian language
        # "pymorphy2",
        # "pymorphy2_dicts_ru",
        # "DAWG-Python",
        # "appdirs",
        # "pyparsing",
    ]
    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch=None, with_flags_in_cc=True):
        env = super().get_recipe_env(arch, with_flags_in_cc)
        env["CXXFLAGS"] = env["CFLAGS"] + " -frtti -fexceptions"

        if with_flags_in_cc:
            env["CXX"] += " -frtti -fexceptions"

        env["LDFLAGS"] += f" -L{self.get_stl_library(arch)}"
        env["LIBS"] = env.get("LIBS", "") + f" -l{self.stl_lib_name}"
        return env

    def postbuild_arch(self, arch):
        super().postbuild_arch(arch)
        self.install_stl_lib(arch)


recipe = SpacyRecipe()
