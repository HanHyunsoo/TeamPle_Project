# TeamPle

U임승차(팀플에서 필요한 관리를 한번에!)

## 프로젝트 기본 설정

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

가상환경 생성후 활성화하고 requirements.txt에 있는 필요한 패키지들 설치(리눅스 기준)

## 설계

![DB](media/readme/db.png)

![ERD](media/readme/erd.jpg)

![FlowChart](media/readme/flowchart.jpg)

## 개발 체크리스트

### 현수

- [x] 회원가입, 로그인, 로그아웃 구현(account 앱)
- [ ] 시간표는 2진데이터로, 시간표 끼리 비교는 views.py에서, 프론트는 2진데이터를 읽어 표형식으로 구현
- [ ] 초대코드로 팀에 들어가는 방식 구현(랜덤으로 아스키코드를 뽑아내서 구현한다.)

### 수현

- [ ] 프론트엔드 구성(부모 템플릿, 팀)
- [ ] 팀 생성, 팀원 추가 기능 구현

### 해철

- [x] 플로우차트 구성
- [ ] 메일 앱 구현
- [ ] 받는 사람 어떻게 추가할지 구상

### 태현

- [x] 팀 생성, 초대 기능(team 앱)
- [ ] 팀 글, 댓글 구현
- [ ] 파일, 이미지 여러개 추가하는 방식 구현

## 팁

- 마이그레이션 오류

```bash
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
```

마이그레이션 파일들(__init__.py 제외)을 삭제하고 다시 마이그레이션한다.

- manage.py 관련 오류

```bash
pip3 uninstall django
pip3 install django==2.2.3
```
