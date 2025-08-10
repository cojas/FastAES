from setuptools import setup, Extension
from pathlib import Path
from Cython.Build import cythonize

ext = Extension(
    "fast_aes.fast_aes",
    sources=[
        "fast_aes/fast_aes.pyx",
        "fast_aes/secret_lib/md5.c",
        "fast_aes/secret_lib/aes.c",
        "fast_aes/secret_lib/base64.c"
    ],
    include_dirs=[str(Path(__file__).parent / "fast_aes" / "secret_lib")],
    extra_compile_args=["-O3"]
)

setup(name="fast_aes",
      version="1.0.1",
      author="万明珠",
      author_email="shiinamashiro163@gmail.com",
      packages=["fast_aes"],
      package_data={
          "fast_aes": ["*.pyi"]
      },
      ext_modules=cythonize([ext], language_level=3))
