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
│  │      admin_login.html
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

## 실행방법
### MAC OS

1. Clone repo
```yaml
git clone repo
cd path_to_dir
```

2. Install MySQL and Config
```yaml
Address : localhost
Port : 3306
Username : root
password : 123123
Database Name : simritest
```

```sql
// open mysql workbench, run below command
create database simritest;
```

3. Generate python virtual environment, Activate
```yaml
python3 -m venv .venv
source ./.venv/bin/activate
```

4. Install Poetry and Dependencies
```yaml
pip install poetry

poetry install // install dependencies
poetry env use path_to_project/.venv/bin/python // set interpreter
```

5. Flask-migrate
```yaml
1. flask db init
or
1. path_to_project/.venv/bin/python -m flask db init
// if cryptography error occurs
// pip install cryptography

2. flask db migrate
or
2. path_to_project/.venv/bin/python -m flask db migrate
// if this command occurs 'Error : Can't locate revision identified by 'blabla'',
// open mysql workbench and drop table 'alembic_version'
// and type flask db migrate again.

3. flask db upgrade
or
3. path_to_project/.venv/bin/python -m flask db upgrade
```

6. Run
```yaml
1. path_to_project/.venv/bin/python -m flask run
or
1. flask run

// open your web browser, connect to 127.0.0.1:5000/
// admin page route : 127.0.0.1/admin
// go to admin page, in question tab, add new at least 5 questions
```

### Windows (추가 예정)

### 프로젝트 수행하면서 생각해볼 사항
1. 프로젝트 플로우 차트 그리는게 매우 좋은 경험이 될 수 있다.
플로우 차트를 이용해서 일정 관리, 프로젝트 관리를 무조건 해야한다!!! (소프트웨어 공학)

2. 동작 과정 캡쳐 및 gif로 보여주는게 좋을 듯

3. 웹페이지 호스팅

4. 코드리팩토링, 코드 진도 빼는거중 뭘 먼저해야하는가? 하나를 먼저 집중해서 해야함 (N모 회사는 코드 리팩토링을 2주에 1회 날을 잡고 실행한다고 한다)

5. 인증과 인가란???

6. 면접때 해당 라이브러리를 왜 사용했는지 정확하게 말해야한다 
예를 들어 flask-login을 왜 사용했는지? 그냥 flask route로 간단하게 구현하면 되지 않을까?

7. API Reverse Refactoring에 대해서 찾아보도록 하자.

### 버그 내역
1. admin page question_list
set deactivate 버튼을 클릭하면 false로 바뀌어야 하는데, 반영되지 않음. 수정 필요

