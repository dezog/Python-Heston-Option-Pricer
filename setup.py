from distutils.core import setup, Extension

module = Extension(
    'PyHeston',
    sources=['PyHeston.cpp', 'BSLib.cpp'],
    include_dirs=['/usr/lib/gsl/lib', '/usr/local/include', 'usr/local/Library/include'],
    library_dirs=['/usr/local/lib', 'usr/local/Library/include'],
    libraries=['gsl', 'gslcblas']
)

setup(
    name='PyHeston',
    version='2.0',
    description='This is a professional package for option pricing',
    author='Junyan Paul Xu',
    author_email='junyanxu5513@gmail.com',
    ext_modules=[module])
