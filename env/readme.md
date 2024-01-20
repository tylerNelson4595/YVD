Steps

1. Download a python virtual enviornment
pip3 install virtualenv

2. create the vm
python -m venv env

3. activate the vm
cd into scripts folder
./activate
env name will apear before name in cmd
to deactivate vm 
deactivate

5. install library in v env
pip3 install <package name>

6. list packages installed
pip3 list

7. maintain and lock packages in a folder now the package folder can be used to download all requirements
pip3 freeze > requirements.txt

8. create app.py
import required packages
customtkinter used to create combo box
pytube connect youtube
os used to run