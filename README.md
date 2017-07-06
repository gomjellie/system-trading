# system-trading
머신러닝을 활용한 주식 투자

# requirements
설치
```
pip install -r requirements.txt
```
새로운 패키지를 설치하면
```
pip freeze > requirements.txt
```
# 사용된 라이브러리 설명
zip-line
```
back-testing 을 위해 설치
```
ipython, jupyter
```
프로젝트돌리는 환경에서는 없어도됨, 코드 테스트용
```
pandas_datareader
```
yahoo, google에서 csv파일을 가져오기 위해 사용
```
<a href='https://github.com/ranaroussi/fix-yahoo-finance'>fix_yahoo_finance</a>
```
pandas_datareader 에서 야후 데이터를 가져오지 못하는 버그를 고쳐줌
```
matplotlib
```
visualize dataframe
```
