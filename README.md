# ClassHelper

## Make Exe

윈도우 검색창에서 `cmd` 를 실행하여 **"명령 프롬프트"** 를 실행한다.

> (`powershell`에서는 동작하지 않음)

```bash
$ python -m venv venv
$ ./venv/Scripts/activate.bat
(venv) $ pip install python-dev-tools
(venv) $ pip install pyinstaller
(venv) $ pyinstaller proto.py
```

> powershell에서 사용하려면 관리자 권한으로 실행한 후 최초 1회 `Set-ExecutionPolicy RemoteSigned`를 입력해주어야 함.
>
> 그리고 `./venv/Scripts/activate.bat` 대신에 `./venv/Scripts/activate.ps1` 을 사용

참고: https://www.pyinstaller.org/