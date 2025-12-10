# Text-to-Speech Converter with Google Cloud

Google Cloud Text-to-Speech API를 이용하여 영문 텍스트를 음성으로 변환하는 Python 프로그램입니다.

## 기능

- `english.txt` 파일에서 영문 텍스트를 읽습니다
- Google Cloud Text-to-Speech API를 사용하여 고품질의 MP3 음성 파일을 생성합니다
- 출력 파일명에 타임스탬프(년월일시분초)를 포함합니다: `english_YYYYMMDDHHMMSS.mp3`
- 에러 처리 및 상세한 로깅 기능 포함

## 설치 및 설정

### 1. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. Google Cloud 인증 설정

Google Cloud Text-to-Speech API를 사용하려면 Google Cloud 프로젝트가 필요합니다.
첫 가입자는 90일간 $300 달러 무료로 사용이 가능합니다.  

**인증 방법:**

#### Option 1: Application Default Credentials (권장)
```bash
gcloud auth application-default login
```

#### Option 2: 서비스 계정 JSON 파일 사용
```bash
set GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json
```

또는 PowerShell에서:
```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
```

## 사용 방법

### 기본 사용법

1. `english.txt` 파일에 변환할 영문 텍스트를 작성합니다

2. 다음 명령어로 프로그램을 실행합니다:

```bash
python text_to_speech.py
```

3. 프로그램이 성공적으로 완료되면 `english_YYYYMMDDHHMMSS.mp3` 파일이 생성됩니다

### 예제

**english.txt 내용:**
```
Hello there. This is a sample text for speech synthesis using Google Cloud Text-to-Speech API.
```

**실행:**
```bash
python text_to_speech.py english.txt
```

**결과:**
```
============================================================
Google Cloud Text-to-Speech Converter
============================================================
Audio content written to file "english_20231215143022.mp3"

Conversion completed successfully!
Output file: english_20231215143022.mp3
```

## 파일 구조

- `text_to_speech.py` - 메인 프로그램
- `english.txt` - 입력 텍스트 파일
- `requirements.txt` - 필요한 Python 패키지 목록
- `README.md` - 이 문서

## 프로그램 기능 설명

### 음성 설정
- **언어**: en-US (미국 영어)
- **음성**: en-US-Chirp3-HD-Charon (고품질 음성)
- **음성 포맷**: MP3

다른 음성을 사용하려면 다음 명령어로 사용 가능한 음성을 확인할 수 있습니다:

```python
from google.cloud import texttospeech
client = texttospeech.TextToSpeechClient()
voices = client.list_voices()
for voice in voices.voices:
    print(f"Name: {voice.name}, Language Codes: {voice.language_codes}")
```
## Voice 모델정보  

- https://docs.cloud.google.com/text-to-speech/docs/list-voices-and-types?hl=ko  

## 주요 기능

1. **파일 읽기**: `english.txt`에서 UTF-8 인코딩으로 텍스트 읽기
2. **음성 합성**: Google Cloud API를 사용한 자연스러운 음성 생성
3. **타임스탬프 생성**: 파일명에 `YYYYMMDDHHMMSS` 형식의 타임스탬프 추가
4. **에러 처리**: 파일 읽기, API 호출, 파일 저장 시 발생하는 오류 처리

## 트러블슈팅

### Error: Google Cloud 인증 오류
- `GOOGLE_APPLICATION_CREDENTIALS` 환경 변수 확인
- `gcloud auth application-default login` 재실행

### Error: 입력 파일을 찾을 수 없음
- `english.txt` 파일이 프로그램과 같은 디렉토리에 있는지 확인

### Error: API 할당량 초과
- Google Cloud Console에서 프로젝트 할당량 확인

## gcloud CLI 버전 548.0.0 설치 

```powershell
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
& $env:Temp\GoogleCloudSDKInstaller.exe    
```

## 라이선스

MIT License

## 참고 자료

- [Google Cloud Text-to-Speech Documentation](https://cloud.google.com/text-to-speech/docs)
- [Python google-cloud-text-to-speech 패키지](https://pypi.org/project/google-cloud-text-to-speech/)
# text-to-speech-convert
