# -
신규 에이아이

## 3D 야구게임 빠른 실행
외부 CDN 없이 동작하므로 인터넷 차단 환경에서도 실행됩니다.

### Windows (더블클릭 실행)
1. `start.bat` 더블클릭
2. 브라우저가 자동으로 열리거나, 주소 `http://127.0.0.1:8000/index.html` 접속

### macOS / Linux
```bash
./run.sh
```

- 자동으로 브라우저 열기를 시도합니다.
- 브라우저가 자동으로 안 열리면 출력되는 주소(기본: `http://127.0.0.1:8000/index.html`)를 복사해서 접속하세요.
- 종료: `Ctrl + C`

포트 변경:

```bash
./run.sh --port 9000
# 또는
python3 run_game.py --port 9000
```
