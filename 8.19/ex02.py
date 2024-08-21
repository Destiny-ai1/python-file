# 언어를 실행하면 모든기능을 로딩하지 않는다.
# visual basic  모든기능을 다불러온다 

# 서로 관련된 데이터 함수를 모아서 만든 클래스다
# 클래스는 개체를 만드는 설계도다
# 관련된 클래스들을 모아서 모듈을 만든다.
import datetime
print(datetime.datetime.now())
    # 앞에오는 datetime 모듈이고 ,뒤에오는 datetime은 클래스이다
    # 다른사람이 만들어둔 라이브러리를 사용해라
    # 라이브러리를 사용하더라도 너무 믿지말고 의존해라

# pip로 requests 에 대한 의존성을 관리했다.
# pip로 라이브러리를 설치했으면 import로 가져와라
# 작업이 끝나고난후엔 uninstall로 삭제할수있다.

import requests
response = requests.get("https://api.bithumb.com/public/ticker/")
print(response.json)
