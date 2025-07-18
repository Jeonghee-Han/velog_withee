<p>필기의 대부분은 그때그때 노션으로 하지만, 개인적인 공부나, SSAFY의 전반적인 생활 내용 또는 복습한 내용들을 velog에 정리해서 올릴 계획이다.
velog에 올린 내용들이 자동으로 github에 md 형식으로 올라갔으면 해서 이 둘을 연동시켰다.</p>
<h3 id="1-github-repository">1. github repository</h3>
<p><img alt="" src="https://velog.velcdn.com/images/heerang/post/b8f021ee-b7ea-4eeb-8943-eda955eb5919/image.png" />
✅ public으로 <strong>새 레포지토리</strong>를 만들어주고, 아래와 같은 <strong>폴더 구조</strong>를 구성해준다. (난 VSCode에서 뚝딱!)
<img alt="" src="https://velog.velcdn.com/images/heerang/post/829cbe12-5c7e-487f-b4d1-ef44854b8c08/image.png" /><img alt="" src="https://velog.velcdn.com/images/heerang/post/d0581717-7d4c-445e-8bef-9838c0eaa5f1/image.png" /></p>
<h3 id="2-github-action--python-scipt">2. github action / python scipt</h3>
<p>아래 ⭐표시 된 부분만 각자 브랜치, 토근명, 벨로그 아이디, 주소 등등으로 수정해주면 된다.</p>
<p>✅<code>update_blog.yml</code></p>
<pre><code class="language-yml">name: Update Blog Posts


on:
  push:
      branches:
        - main  # ⭐ 또는 워크플로우를 트리거하고 싶은 브랜치 이름
  schedule:
    - cron: '0 0 * * *'  # 매일 자정에 실행

jobs:
  update_blog:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Push changes
      run: |
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'
        git push https://${{ secrets.GH_PAT_WITHEE }}@github.com/Jeonghee-Han/velog_withee.git 
       # ⭐ git push https:// + ${{ secrets.본인 토큰명 }} + 본인 github repo 주소

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install feedparser gitpython

    - name: Run script
      run: python scripts/update_blog.py
</code></pre>
<p>✅<code>update_blog.py</code></p>
<pre><code class="language-python">import feedparser
import git
import os

# 벨로그 RSS 피드 URL
# example : rss_url = 'https://api.velog.io/rss/@heerang'
rss_url = 'https://api.velog.io/rss/@[벨로그 아이디]' #⭐

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
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    # 필요에 따라 추가 문자 대체
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # 글 내용을 파일에 작성

        # 깃허브 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# 변경 사항을 깃허브에 푸시
repo.git.push()</code></pre>
<h3 id="pat-권한">PAT 권한</h3>
<p><code>github 계정</code> → <code>Settings</code> → <code>Developer Settings</code> → <code>Personal access tokens (classic)</code> → <code>Generate New Token</code>
<img alt="" src="https://velog.velcdn.com/images/heerang/post/099db1e0-23f2-4585-8c0d-3ef08e26e171/image.png" />✅ <code>Note</code>: 본인 토큰명 → <code>repo</code>, <code>workflow</code> 체크 → <code>Generate new token</code> <img alt="" src="https://velog.velcdn.com/images/heerang/post/23fcda77-0bd1-4c32-9a01-623935d44071/image.png" />
⚠️ 생성된 토큰은 한 번 밖에 볼 수 없으니 반드시 복사해둬야 한다.</p>
<p>이제 생성된 레포지토리로 들어가서 새로운 레포지토리 시크릿을 생성해준다.
✅ <code>Settings</code> → <code>Actions secrets and variables</code> → <code>Actions</code> → <code>New Repository Secret</code></p>
<p>✅ Name에는 <code>update_blog.yml</code> 에 들어갈 본인 토큰명을 작성해주고, Secret은 아까 복사해둔 토큰을 넣어준다.</p>
<h3 id="commit--push">Commit &amp; Push</h3>
<p>✅ 레포지토리에 push하면 github action이 발동되어 <code>velog-posts</code> 폴더가 자동 생성된다. 해당 폴더 안에는 velog 글들이 .md 파일로 저장되어 있을 것이다.
<img alt="" src="https://velog.velcdn.com/images/heerang/post/83d29dda-6fb6-409f-8702-77f9da027077/image.png" /><img alt="" src="https://velog.velcdn.com/images/heerang/post/7d8a794c-b0f4-4835-b4a8-2791fc40063c/image.png" /></p>