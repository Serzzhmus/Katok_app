from cx_Freeze import setup, Executable


options = {'build.exe':
           {'icludes': ['Gui', 'BL', 'Abstract', 'Text']}}


setup(
    name = "Каток",
    version = "1.0",
    description = "Расчет стоимости билета на каток",
    options = options,
    executables = [Executable("Katok_app.py", base = "Win32GUI")]
    )
