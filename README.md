#
# GitManager
# 

Commands and examples:

1. Git CLI help menu

	./gitcli.py -h

2. Clone repo to the directory

	./gitcli.py -clone --repourl <SSH/HTTPS repo URL> --repodir <repo_name>
	
	./gitcli.py -clone --repourl https://github.com/h0st/test_git_repo.git --repodir test_repo2
	
3. Create branch by name

	./gitcli.py -createbranch --branchname develop
	
4. Switch to the branch by name

	./gitcli.py -switchbranch --branchname develop

5. Commit all changes

	./gitcli.py -commit --commitmsg "commit message"

6. Push changes to the branch

	./gitcli.py -push --branchname develop

7. Repo status info

	./gitcli.py -status
