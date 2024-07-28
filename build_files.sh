echo "Executing build_files.sh"
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic
echo "Installed dependencies. Exiting build_files.sh"