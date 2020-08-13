# Elevator Call 
 
## ■ Intro
엘리베이터 호출 및 호출 당시의 층수, 도착시 알림을 TTS로 제공 합니다.<br>
EW11로 신형 코콤 월패드와 연동 하여 엘리베이터 층수 패킷 수신 가능 시에만 사용하실 수 있습니다.<br>
 
## ■ How to Install
(1) config 폴더 내에 command_python 폴더 추가 <br>
(2) command_python 폴더 내에 Elevator_Call_TTS.py를 복사 해주세요. <br>
(3) Elevator_Call.py을 수정 해야 합니다. 아래 항목에 대해 값을 기입 해주세요.<br>
```python
bearer_token = "" # 여기에 Home Assiant에서 받은(HA에서 아이디 클릭 -> "장기 액세스 토큰 추가") "장기 액세스 토큰 값"을 넣어주세요.
ew11_ip = "" # EW11의 IP를 넣어 주세요. 예) 192.168.0.10
entity_id = "" # 여기에 TTS에 사용 할 media_player의 entity_id를 넣어주세요. 예) "media_player.hom_geurub"
url = "" # HA의 주소를 넣어 주세요. 예) https://ha.test.duckdns.org
```
(4) configuration.yaml에 아래 내용 추가 <br> 
```yaml
shell_command:
  elevator_call: python3 /config/command_python/Elevator_Call_TTS.py
```
(5) HA 재부팅 후 개발자 도구 -> 서비스 -> shell_command.elevator_call 실행
