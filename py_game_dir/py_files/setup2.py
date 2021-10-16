
import cx_Freeze

executables = [cx_Freeze.Executable("py_game_try1.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame", "numpy", "time"],
                           "include_files":[]}},
    executables = executables

    )