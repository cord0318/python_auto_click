# AutoClick 📱
파이썬용 오토클릭 라이브러리입니다.

* https://pypi.org/project/auto-click/
- https://github.com/cord0318/python_auto_click

# 다운로드 📥
**이 모듈은 파이썬 모든 버젼에서 사용 가능합니다.**
윈도우나 리눅스에서 다음과 같이 입력합니다.
```
pip install auto-click
```
오류가 나는 경우, python -m pip install --upgrade pip 로 pip를 업데이트 해주세요.

# 사용법 🤖
```python
from auto import AutoClick
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

click_thread = AutoClick(0.05, Button.right)
click_thread.start()

def on_press(key):
    print(key)
    if key == KeyCode(char='1'):
        click_thread.start_clicker()
        print("AutoMouse Start!")
    elif key == KeyCode(char='2'):
        click_thread.stop_clicker()
        print("AutoMouse Stop!")
    elif key == KeyCode(char='3'):
        click_thread.exit()
        print("AutoMouse Exit!")
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
```

# Tip
**최대 cps는 78입니다!**
