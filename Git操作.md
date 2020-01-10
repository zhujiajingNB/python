## Git操作

####  提交操作

1. git init 初始化git仓库
2. git add . 添加文件至暂存区
3. git commit -m'xxx' 添加修改至本地仓库
4. git remote add origin https://github.com/zhujiajingNB/learn_git.git 关联本地仓库与远程仓库 （远程库名需要与本地仓库名一致）
5. git status 查看git 状态
6. git diff 查看修改内容
7. git push 提交远程仓库

#### 版本管理

1. git log 查看提交日志
2. git log --pretty=oneline 查看提交日志的id
3. git reset --hard HEAD^ 回退上一次提交本地仓库的版本
4. git reset --hard id(版本id号) 回退对应的本地仓库版本
5. git reflog 记录命令，可用来寻找版本id
6. git reset HEAD <file> 回退提交到暂存区的修改文件
7. git reset  checkout -- <file> 回退未提交到暂存区的文件

#### 分支操作

1. git branch 查看所有分支
2. git branch <name> 创建分支  git checkout -b <name> 创建并切换分支
3. git checkout <name> 切换分支
4. git merge <name> 合并分支到当前分支（合并后无需再提交至本地仓库）（不过合并分支前双方都要先提交至本地仓库）