"""
This script reads `scrum/product_backlog.md` and creates GitHub issues for each unchecked item.
Use this manually during backlog grooming to push updates to GitHub.
"""
import os
import requests

REPO = 'sspirial/copilot-workflow-template'
TOKEN = os.getenv('GITHUB_TOKEN')
BACKLOG_FILE = 'scrum/product_backlog.md'
headers = {'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/vnd.github+json'}

def parse_backlog():
    with open(BACKLOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    issues = []
    current_section = ''
    for line in lines:
        if line.startswith('## '):
            current_section = line.strip('# \n')
        elif line.strip().startswith('- [ ]'):
            task = line.strip()[5:].strip()
            issues.append((current_section, task))
    return issues

def fetch_existing_titles():
    url = f'https://api.github.com/repos/{REPO}/issues'
    res = requests.get(url, headers=headers, params={'labels': 'backlog', 'state': 'open'})
    return [i['title'] for i in res.json()] if res.status_code == 200 else []

def create_issue(section, title):
    body = f"Imported from `{BACKLOG_FILE}`\n\n**Category:** {section}"
    res = requests.post(
        f'https://api.github.com/repos/{REPO}/issues',
        headers=headers,
        json={'title': title, 'body': body, 'labels': ['backlog']}
    )
    print(f"✅ Created: {title}" if res.status_code == 201 else f"❌ Failed: {title} => {res.text}")

def fetch_issues():
    res = requests.get(f'https://api.github.com/repos/{REPO}/issues', headers=headers, params={'labels': 'backlog', 'state': 'open'})
    return res.json() if res.status_code == 200 else []

def write_backlog(issues):
    with open(BACKLOG_FILE, 'w', encoding='utf-8') as f:
        f.write('# 🧱 Product Backlog (synced from GitHub issues)\n\n')
        sections = {}
        for issue in issues:
            section = 'General'
            if issue.get('body') and '**Category:**' in issue['body']:
                lines = [l for l in issue['body'].splitlines() if '**Category:**' in l]
                if lines:
                    section = lines[0].split('**Category:**')[-1].strip()
            sections.setdefault(section, []).append(issue['title'])
        for section, titles in sections.items():
            f.write(f'## {section}\n')
            for title in titles:
                f.write(f'- [ ] {title}\n')
            f.write('\n')

if __name__ == '__main__':
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else 'md-to-issues'
    if mode == 'md-to-issues':
        existing = fetch_existing_titles()
        for section, title in parse_backlog():
            if title not in existing:
                create_issue(section, title)
    elif mode == 'issues-to-md':
        write_backlog(fetch_issues())
    else:
        print('Usage: python sync_backlog_to_issues.py [md-to-issues|issues-to-md]')