@echo off
set output_dir="../.build_and_dist/"
set package_name="ffmpeg_normalize"
set exe_name="ffmpeg-normalize"

@echo on
cd %~dp0
call update_requirements.bat
cd ..\
pip install -r requirements.txt
cd scripts
nuitka "../%package_name:~1,-1%" --standalone -o "%exe_name%" --output-dir "%output_dir%" --show-progress --show-scons --show-modules --recurse-to=multiprocessing --plugin-enable=multiprocessing --lto --assume-yes-for-downloads