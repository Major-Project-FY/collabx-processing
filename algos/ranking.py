def get_total_user_commits_from_repo_data(repo_data, gh_username):
    sum = 0
    for i in repo_data:
        if 'contributors' in i:
            for j in i['contributors']:
                if j['contributorGitHubUserName'] == gh_username:
                    sum = sum + j['contributions']
    print("total contributions", sum)
    return sum


def get_total_languages_from_repo_data(repo_data):
    languages = []
    for i in repo_data:
        if 'languages' in i:
            combined_set = set(languages).union(set(i['languages']))
            languages = list(combined_set)
    print('all languages', languages)
    return {'languages': languages, 'total_languages': len(languages)}


def calculate_level_on_gh_data(data, repo_data):
    repo_data = list(repo_data)
    total_repos = data['publicRepos'] + data['ownedPrivateRepos']
    commits = get_total_user_commits_from_repo_data(
        repo_data, gh_username=data['gitHubUsername'])
    languages = get_total_languages_from_repo_data(list(repo_data))
    followers = data['followers']
    print('total languages', languages)
    if (total_repos >= 15):
        if (commits >= 50):
            if (languages['total_languages'] >= 10):
                if (followers >= 10):
                    return {
                        'userLevel': 'Intermediate',
                        'totalCommits': commits,
                        'totalFollowers': followers,
                        'codeLanguages': languages['languages'],
                        'totalPublicRepos': data['publicRepos'],
                        'totalPrivateRepos': data['totalPrivateRepos'],
                        'totalPublicGists': data['publicGists'],
                        'gitHubAvatarUrl': data['gitHubAvatarUrl'],
                        'totalCollaborators': data['collaborators'],
                        'gitHubUsername': data['gitHubUsername']
                    }
    return {
        'userLevel': 'Beginner',
        'totalCommits': commits,
        'totalFollowers': followers,
        'codeLanguages': languages,
        'totalPublicRepos': data['publicRepos'],
        'totalPrivateRepos': data['totalPrivateRepos'],
        'totalPublicGists': data['publicGists'],
        'gitHubAvatarUrl': data['gitHubAvatarUrl'],
        'totalCollaborators': data['collaborators']
    }
