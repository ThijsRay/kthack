from distutils.core import setup
from Cython.Build import cythonize


pyx_files = [
    "generator/mceditlib/nbt.pyx",
    "generator/mceditlib/relight/with_cython.pyx"
]

setup(
    ext_modules = cythonize(
        pyx_files,
        compile_time_env={'IS_PY2': sys.version_info[0] < 3})
)
