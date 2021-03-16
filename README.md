# ClassHelper

## System Environment

- Windows 10
- Python 3.8

## Make Exe

### Requirements

- http://python.org 에서 다운로드 받아야함 (`Microsoft Store`에서 다운로드 받은 python은 동작 안함)
    - https://www.python.org/ftp/python/3.8.8/python-3.8.8-amd64.exe
-`pyinstaller`를 사용하여 exe를 만들수 있는데, 이때는 반드시 `python 가상환경`을 사용해야 함. (아래 스크립트 참조)



### STEP1. Python virtual environment 구성

```bash
$ python -m venv venv
```
> powershell에서 `activate.ps1` 스크립트를 사용하려면 관리자 권한으로 실행한 후 최초 1회 `Set-ExecutionPolicy RemoteSigned`를 입력해주어야 함.

```bash
$ ./venv/Scripts/activate.ps1
```

> `venv/pyvenv.cfg`파일을 열고 `include-system-site-packages` 필드를 `true`로 바꾸어 주어야 함. (`python-dev-tools`설치를 위해.)



### STEP2. 필요한 dependency 설치

```bash
(venv) $ pip install pyinstaller
```



### STEP3. exe 파일 만들기

아래의 스크립트 실행하면 `dist` 폴더에 exe파일이 생성됨 

```bash
(venv) $ pyinstaller --onefile --noconsole --clean proto.py
```



### STEP4. data 옮기기

파일 실행에 필요한 `subject_zoom_url.txt`, `time_slot.txt`, `time_table.txt` 파일을
exe 파일이 있는 `dist` 파일에 복사하기

참고: https://www.pyinstaller.org/