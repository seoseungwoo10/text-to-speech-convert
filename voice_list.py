from google.cloud import texttospeech

def list_voices():
    client = texttospeech.TextToSpeechClient()

    # 사용 가능한 모든 보이스 가져오기
    response = client.list_voices()
    voices = response.voices

    print(f"총 {len(voices)}개의 보이스를 찾았습니다.\n")

    # 보기 좋게 출력 (en-US 만 필터링 예시)
    for voice in voices:
        # 영어(미국) 보이스만 출력하려면 아래 조건문 사용
        if "en-US" in voice.language_codes[0]: 
            # Chirp 모델 등 이름 확인
            print(f"Name: {voice.name}")
            print(f"  Gender: {texttospeech.SsmlVoiceGender(voice.ssml_gender).name}")
            print(f"  Rate: {voice.natural_sample_rate_hertz} Hz")
            print("-" * 20)

if __name__ == "__main__":
    list_voices()

    