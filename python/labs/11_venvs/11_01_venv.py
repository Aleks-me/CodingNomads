'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from
   the requirements.txt file.

'''

"""
CLI commands:

$ python -m venv env_1 && source env_1/bin/activate
$ pip install django numpy pytest
$ pip freeze > ../requirements.txt && deactivate
$ rm -rf env_1
$ python -m venv env_2 && source env_2/bin/activate
$ pip install -r ../requirements.txt && deactivate

"""
