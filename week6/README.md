# Introduction to Git

## Create a new Git Repo

```
git init
```

## check the status of your repo
```
git status
```

## To add files to Git, to the staging area

```
git add <filename1><filename2>

```
## To commit current staging area
```
git commit -m 'Add README file about Git'
```

```
git log
```
## Link your local repo to the remote repo
```
git remote add origin https://github.com/sky-story/techin509-au24-week6.git
```

## Check git remote

```
git remote show origin
fetch: to pull the files from remote repo to local repo
push: to push the files from local repo to remote repo
```

## Push local branch to remote repo

```
# git push <remote name> <branch name>
for win: git push origin master
for mac: git push origin main
```