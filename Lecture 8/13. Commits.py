import re


class Commit:
    def __init__(self, hex_str, message, additions, deletions):
        self.hex_str = hex_str
        self.message = message
        self.additions = int(additions)
        self.deletions = int(deletions)


pattern = r'https://github\.com/(?P<user>[A-Za-z\d-]+)/(?P<repo>[A-Za-z_-]+)/commit/(?P<hex>[a-f\d]{40}),(?P<message>[^\n,]+),(?P<addition>\d+),(?P<deletion>\d+)'
regex = re.compile(pattern)
username_repo = {}
while True:
    temp_arr = []
    repo_data = {}
    input_data = input()
    if input_data == "git push":
        break
    url_raw = regex.finditer(input_data)
    for url in url_raw:
        username = url.group('user')
        repo_in = url.group('repo')
        hex_str_in = url.group('hex')
        message_in = url.group('message')
        addition_in = url.group('addition')
        deletion_in = url.group('deletion')
        data_class = Commit(hex_str=hex_str_in, message=message_in, additions=addition_in, deletions=deletion_in)
        if username in username_repo:
            repo_data = username_repo[username]
        if repo_in in repo_data:
            temp_arr = repo_data[repo_in]
        temp_arr.append(data_class)
        repo_data[repo_in] = temp_arr
        username_repo[username] = repo_data
for item in sorted(username_repo):
    print(item + ":")
    repos = username_repo[item]
    for repo in sorted(repos):
        print(f'  {repo}:')
        commits = repos[repo]
        total_additions = 0
        total_deletions = 0
        for commit in commits:
            print(
                f'    commit {commit.hex_str}: {commit.message} ({commit.additions} additions, '
                f'{commit.deletions} deletions)')
            total_additions += commit.additions
            total_deletions += commit.deletions
        print(f'    Total: {total_additions} additions, {total_deletions} deletions')
