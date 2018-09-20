from cx_Freeze import setup, Executable

executables = [
    Executable('program_upload.py')
]

setup(name='upload',
      version='0.1',
      description='Upload sequence',
      executables=executables
      )