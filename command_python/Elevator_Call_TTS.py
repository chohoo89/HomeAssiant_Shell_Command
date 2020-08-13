import socket
import binascii
import requests
#========== Main ==========

if __name__ == "__main__":     
    bearer_token = "" # 여기에 Home Assiant에서 받은 "장기 액세스 토큰 값"을 넣어주세요.
    ew11_ip = "" # EW11의 IP를 넣어 주세요. 예) 192.168.0.10
    entity_id = "" # 여기에 TTS에 사용 할 media_player의 entity_id를 넣어주세요. 예) "media_player.hom_geurub"
    url = "" # HA의 주소를 넣어 주세요. 예) https://ha.test.duckdns.org

    def HA_GOOGLE_SAY(url, bearer_token, entity_id, message):
        head = {'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + bearer_token}
        data = {"entity_id" : entity_id, "message" : message}

        url = url + "/api/services/tts/google_say"
        response = requests.post(url, json=data, headers=head)
        print(message)

    def HA_NAVER_SAY(url, bearer_token, entity_id, message):
        head = {'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + bearer_token}
        data = {"entity_id" : entity_id, "message" : message}

        url = url + "/api/services/tts/naver_premium_say"
        response = requests.post(url, json=data, headers=head)
        print(message)
    
    kocom_client = socket.socket()
    kocom_client.connect((ew11_ip, 8899))

    #엘리베이터 호출
    data = "aa5530bc0001004400010000000000000000320d0d"
    kocom_client.send(binascii.unhexlify(data))

    first_anounce = False

    while True:
        data = kocom_client.recv(21)
        hex_data = data.hex()

        if first_anounce == False and hex_data[6:8] == "bc":
            floor = hex_data[22:24]
            if floor == "82":
                floor_message = "지하 1"
            else:
                floor_message = str(int("0x" + hex_data[22:24], 16))

            HA_NAVER_SAY(url, bearer_token, entity_id, "엘리베이터를 호출 하였습니다. 현재 엘리베이터는 " + floor_message + "층 입니다.")
            first_anounce = True
            
        
        if hex_data[20:22] == "03":
            HA_NAVER_SAY(url, bearer_token, entity_id, "엘리베이터가 도착 하였습니다. 안녕히 가세요")
            break
    
    kocom_client.close()
   
