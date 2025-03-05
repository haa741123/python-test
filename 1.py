import os
import time
import requests
import subprocess
from git import Repo

# GitHub 리포지토리 정보
REPO_OWNER = "haa741123"
REPO_NAME = "python-update"
BRANCH_NAME = "main"  # 또는 "master"
LOCAL_REPO_PATH = "/path/to/your/local/repo"

# GitHub API 엔드포인트
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits/{BRANCH_NAME}"

def get_latest_commit_sha():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()['sha']
    else:
        print(f"GitHub API 요청 실패: {response.status_code}")
        return None

def update_local_repo():
    repo = Repo(LOCAL_REPO_PATH)
    origin = repo.remotes.origin
    origin.pull()
    print("로컬 리포지토리가 업데이트되었습니다.")

def main():
    last_known_sha = None
    
    while True:
        current_sha = get_latest_commit_sha()
        
        if current_sha and current_sha != last_known_sha:
            print("새로운 커밋이 감지되었습니다. 업데이트를 시작합니다...")
            update_local_repo()
            last_known_sha = current_sha
            
            # 여기에 프로그램 재시작 로직을 추가할 수 있습니다.
            # 예: subprocess.run(["python", "your_main_script.py"])
        
        time.sleep(300)  # 5분마다 체크 (GitHub API 사용량 제한을 고려하여 조정)

if __name__ == "__main__":
    main()
