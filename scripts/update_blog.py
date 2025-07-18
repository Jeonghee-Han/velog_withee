import feedparser
import git
import os

# 벨로그 RSS 피드 URL
# example : rss_url = 'https://api.velog.io/rss/@soozi'
rss_url = 'https://api.velog.io/rss/@heerang'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 제목 → 파일명으로 (슬래시 제거 등)
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 글 내용을 파일에 항상 덮어쓰기 (새로 쓴 글이든 수정이든)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(entry.description)

    # 변경사항이 있으면 커밋
    repo.git.add(file_path)
    try:
        repo.git.commit('-m', f'Update post: {entry.title}')
    except git.GitCommandError:
        # 이미 최신 상태면 커밋 생략 (변경 없음)
        pass

# 최종 push
repo.git.push()
