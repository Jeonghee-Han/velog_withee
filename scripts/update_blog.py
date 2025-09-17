import feedparser
import os
import re

# 벨로그 RSS 피드 URL
RSS_URL = 'https://api.velog.io/rss/@heerang'

# 게시물을 저장할 디렉토리 경로
POSTS_DIR = 'velog-posts'

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(POSTS_DIR):
    os.makedirs(POSTS_DIR)

# RSS 피드 파싱
feed = feedparser.parse(RSS_URL)

# 각 게시물을 파일로 저장
for entry in feed.entries:
    # 파일명으로 사용할 수 없는 문자 제거 또는 변경
    file_name = re.sub(r'[\\/*?:"<>|]', "", entry.title) + '.md'
    file_path = os.path.join(POSTS_DIR, file_name)
    
    # 글 내용 (HTML 태그 포함)
    content = entry.description
    
    # 파일에 내용 작성 (항상 덮어쓰기)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f'# {entry.title}\n\n')
        f.write(f'**Published:** {entry.published}\n')
        f.write(f'**Link:** {entry.link}\n\n')
        f.write('---\n\n')
        f.write(content)

print(f"총 {len(feed.entries)}개의 포스트를 확인하고 업데이트했습니다.")
