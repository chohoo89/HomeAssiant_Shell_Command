# Elevator Call 
 
## ■ Intro
EW11로 신형 코콤 월패드와 연동 하여 엘리베이터 층수 패킷 수신 가능 시에만 사용하실 수 있습니다.<br>
 
## ■ How to Install
(1) config 폴더 내에 command_python 폴더 추가 <br>
(2) command_python 폴더 내에 Elevator_Call_TTS.py를 복사 해주세요. <br>
(3) configuration.yaml에 아래 내용 추가 <br> 
```yaml
shell_command:
  elevator_call: python3 /config/command_python/Elevator_Call_TTS.py
```
(4) HA 재부팅 후 개발자 도구 -> 서비스 -> shell_command.elevator_call 실행
