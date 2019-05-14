
PyQT5/PyInstaller.


Hey There! 

Purger is a small GUI that's gonna help you purge/delete your pycache and migrations.


As a Django Dev, i always break my database, which leads me to running a marathon of deleting files
and folders and re-running migrations.

so i made Purger to perform those actions on my behalf and save me some time.

Mind you, this was made on a linux machine and uses /bin/bash, so i am pretty sure it is not cross-plateform.
You can download the source code (.ui and .py files) and modify them, you can also change the UI with QtDesigner.

it is simple:
	1- Select your Django project folder or type in the full path
	2- Loop over that folder which will display the tree.
		NB: by default, manage.py, db.sqlite3 and .vscode are hidden (i use Vscode so...).
	3- Push targets to the console.
	4- Purge your Targets
		NB: running purge on non existing files and folders is fine, it won't break the GUI.
	5- Run migrations 
		NB0: if you are using a virtualenv, your django project has to be inside the virtualenv folder because ... i designed it that way.
		NB1: you can bypass virtualenv by choosing no, the GUI will add 'python3' to all the shell commands.
		NB3: The GUI can't output the shell commands errors, so it might be a good idea to check if those migrations were run correctly.
	6- Clear the console
		NB: using reset will clear out the whole GUI.

so that's it, i hope Purger comes in handy :D 
