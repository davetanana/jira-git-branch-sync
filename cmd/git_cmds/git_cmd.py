from github import Github,Auth,Branch,Repository,AuthenticatedUser,GithubException


def github_create(repo, org, github_pat,user, extra_identifier, jira_info) -> str:
    auth_client = Auth.Token(github_pat)
    github_client = Github(base_url=f'https://github.com/{org}',auth=auth_client)
    try:
        user = github_client.get_user()
        repository = github_client.get_repo(repo)
        master_branch = repository.get_branch("master")
        if master_branch is None:
            master_branch = repository.get_branch("main")
            if master_branch is None:
                Exception(ValueError("No master branch"))
        master_branch_sha = master_branch.commit.sha
        user_name = user.login
        branch_name = f'{user_name}/{jira_info[0]['issue_id']}_{jira_info[0]}'
        git_ref = repository.create_git_ref(ref=f'refs/heads/{branch_name}', sha=master_branch_sha)
        return git_ref
    except:
        GithubException(message="Error with creating ref: ")
    pass