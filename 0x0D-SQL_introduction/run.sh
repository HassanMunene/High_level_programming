# This is a script that I have created to automate the process of git add, commit and push
# The commit message is written inside double quotes at the command line
# To run the script type at the command line the following
# ./run.sh "Your commit message" press enter

git add .
git commit -m "$1"
git push
