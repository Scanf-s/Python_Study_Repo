# 기초적인 설문조사 WEB개발 프로젝트

이 프로젝트는, 사용자 정보를 입력받고, 해당 사용자가 주어진 설문 또는 테스트에 대한 답변을 기록하여 결과를 표시해주는 프로젝트 입니다.

> 추후, 결과 표시 기능을 pandas를 이용하여 업그레이드 할 예정입니다.

## 주요 기능
- 사용자 정보 입력: 설문 참여자 정보를 입력할 수 있습니다.
- 설문(테스트): Database에 저장한 설문 5문항을 보여줍니다.
- 결과: 사용자가 답변한 내용을 보여줍니다. (추후, 결과 표시 기능을 업그레이드 할 예정입니다.)
- 어드민 페이지: 각 사용자의 답변에 대한 기록, Database Model, 등을 확인할 수 있는 페이지 입니다.

## 개발 환경
![](https://img.shields.io/badge/AMD-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
![](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)

## 사용 기술
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![](https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=Jinja&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/Sqlalchemy-D71F00?style=for-the-badge&logo=SQLalchemy&logoColor=white)

## 프로젝트 구조
```yaml
Project_SIMRITEST
│  .gitignore
│  app.py
│  poetry.lock
│  pyproject.toml
│  README.md
│  requirements.txt
│
├─.idea
│  │  .gitignore
│  │  encodings.xml
│  │  material_theme_project_new.xml
│  │  misc.xml
│  │  modules.xml
│  │  poetry.xml
│  │  Project_SIMRITEST.iml
│  │  vcs.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│
├─config
│  │  db.py
│  │  __init__.py
│  │
│  └─__pycache__
│          db.cpython-312.pyc
│          __init__.cpython-312.pyc
│
├─forms
│      Answerform.py
│      Userform.py
│      __init__.py
│
├─migrations
│  │  alembic.ini
│  │  env.py
│  │  README
│  │  script.py.mako
│  │
│  ├─versions
│  │  │  51f5c927dbbc_.py
│  │  │  be5e349d24f1_.py
│  │  │  cabd2c25fca7_.py
│  │  │  f71bfd336e46_.py
│  │  │
│  │  └─__pycache__
│  │          be5e349d24f1_.cpython-312.pyc
│  │
│  └─__pycache__
│          env.cpython-312.pyc
│
├─models
│  │  model_definitions.py
│  │  __init__.py
│  │
│  └─__pycache__
│          model_definitions.cpython-312.pyc
│          __init__.cpython-312.pyc
│
├─templates
│  │  base.html
│  │
│  ├─admin
│  │      admin_home.html
│  │      answer_list.html
│  │      login.html
│  │      question_list.html
│  │      register.html
│  │
│  ├─home
│  │      index.html
│  │      result.html
│  │      userinfo.html
│  │
│  └─question
│          question_detail.html
│
├─views
│  │  admin_views.py
│  │  main_views.py
│  │  question_views.py
│  │  __init__.py
│  │
│  └─__pycache__
│          admin_views.cpython-312.pyc
│          main_views.cpython-312.pyc
│          question_views.cpython-312.pyc
│          __init__.cpython-312.pyc
│
└─__pycache__
        app.cpython-312.pyc
```

## 설치 및 실행 방법 (업데이트 예정)
1. 자신의 로컬 드라이브로 프로젝트 clone
2. MySQL 설치 및 설정, database 생성
   ![MySQL Install](https://dev.mysql.com/downloads/installer/)
   > 추후, MySQL 연결 설정 및 Database 생성에 대해 업데이트 할 예정입니다.
3. 의존성 설치 및 가상환경 접속
   ```sh
   pip install poetry
   poetry install
   poetry shell
   ```
4. Flask-migrate 사용
   ```sh
   flask db init
   flask db migrate
   flask db uprade
   ```
5. Flask App 실행
   ```sh
   flask run
   ```

## 사용법
> 추후 자세한 사용방법에 대해 업데이트할 예정입니다.
1. 사용자 정보 입력
2. 설문 진행
3. 결과 확인
4. Admin 페이지
