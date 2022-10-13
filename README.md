# 다이빙포인트 추출 프로젝트
아티슨앤오션과 기업협업으로 진행한 코드스테이츠 AI 부트캠프 프로젝트입니다
# 프로젝트 소개
다이빙포인트 관련 정보를 얻고자하는 지역명을 입력하면 해당 지역의 다이빙포인트 지도 이미지를 크롤링한 후 지도 이미지로부터 다이빙포인트 명칭과 GPS 정보를 얻는 프로젝트입니다
# 프로젝트 상세 설명
## 크롤링
지역명을 List 형태로 입력받으며 실행시 크롬 브라우저가 실행되어 List의 지역명들을 순회하며 지역명 + dive site map 키워드로 구글 이미지 검색
자동으로 스크롤을 내리고 이미지 더보기 버튼을 클릭하여 모든 검색 결과 이미지 다운로드
## OCR
앞서 크롤링으로 얻은 지도 이미지를 입력하면 BoundingBox로 감지된 문자를 시각적으로 보여주며 console에 인식된 문자와 BoundingBox 꼭짓점 좌표를 순차적으로 출력
## GPS 정보 획득
지역명 + OCR을 통해 얻은 다이빙포인트 명칭을 GoogleMaps API에 전달해 해당 지역의 위도와 경도 정보 획득 후 console에 출력
# 사용기술
- BeautifulSoup
- Selenium
- EasyOCR
- GoogleMaps API
