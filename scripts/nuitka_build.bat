@echo off
set "output_dir=.build_and_dist/"
set "package_name=ffmpeg_normalize"

@echo on
cd %~dp0
cd ..\
pip install -r requirements.txt
nuitka "%package_name%" --standalone --output-dir "%output_dir%" --show-progress --show-scons --recurse-to=multiprocessing --plugin-enable=multiprocessing --assume-yes-for-downloads
pause