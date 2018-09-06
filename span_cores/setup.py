from distutils.core import setup
from distutils.extension import Extension
from shutil import copyfile

if __name__ == '__main__':
    # files to be included in the extensions
    paths = [
        'decomposition/decomposition',
        'decomposition/naive_decomposition',
        'decomposition/subroutines/commons',
        'decomposition/subroutines/subroutine',
        'maximal/naive_maximal',
        'maximal/maximal',
        'maximal/subroutines/subroutine',
        'temporal_graph/temporal_graph',
        'utilities/memory_measure',
        'utilities/print_console',
        'utilities/print_file',
        'utilities/time_measure'
    ]

    # import Cython if available
    USE_CYTHON = True
    try:
        from Cython.Build import cythonize
    except ImportError:
        cythonize = None
        USE_CYTHON = False

    # if Cython is available
    if USE_CYTHON:
        # set the .pyx extension
        ext = '.pyx'

        # create the new .pyx files
        for path in paths:
            copyfile(path + '.py', path + ext)
    # otherwise
    else:
        # set the .c extension
        ext = '.c'

    # build the extensions list
    extensions = [Extension(path.replace('/', '.'), [path + ext]) for path in paths]

    # if Cython is available
    if USE_CYTHON:
        # cythonize the extensions
        extensions = cythonize(extensions)

    # run the setup
    setup(
         ext_modules=extensions
    )
