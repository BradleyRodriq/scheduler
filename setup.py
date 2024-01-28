from cx_Freeze import setup, Executable

setup(
    name="Scheduler by Bradley Rodriguez",
    version="1.0",
    description="Create a random schedule",
    executables=[Executable("setup.py")],
)