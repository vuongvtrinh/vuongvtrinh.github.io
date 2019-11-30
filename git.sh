cd code
hugo
cd ..
python update_files.py
git add .
git commit -m "Commit time: `date +'%Y-%m-%d %H:%M:%S'`"
git push -f origin master
cd public
git add .
git commit -m "Commit time: `date +'%Y-%m-%d %H:%M:%S'`"
git push -f origin master