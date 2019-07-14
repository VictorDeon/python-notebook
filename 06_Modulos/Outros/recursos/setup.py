from distutils.core import setup, Extension

module = Extension('c_code', sources = ['fibonacci.c'])

setup(
    name = 'PackageName',
    version = '1.0',
    description = 'Pacote para o modulo',
    ext_modules = [module]
)