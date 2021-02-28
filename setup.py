from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['keyboard', 'json']}

setup(name="Stelian Keyboard",
      version="1.0",
      description="Stelian Keyboard made by Sch",
      options={"build_exe": build_exe_options},
      executables=[Executable("__main__.py", target_name='StelianKeyboard')])
