## Branch Management



1 check the remote branches

```
git branch -a
```



```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/ctsan005/coordinate_planning
  remotes/origin/ecui001/gym_env
  remotes/origin/master
  remotes/origin/seyeon

```



2 check local branch

```
git branch
```



3 create local branch

```
git branch ctsan005
```



4 

```
git checkout -b ctsan005/coordinate_planning origin/ctsan005/coordinate_planning

```



```
git branch -d <BranchName>
```



if I use checkout a branch, the files under the folder will change