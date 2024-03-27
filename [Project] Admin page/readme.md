# Admin page practice
![image](https://github.com/Scanf-s/OZCoding_Backend/assets/105439069/d34201ec-b076-4134-a285-82901573e3bd)

<br>

## 프로젝트 소개

- 기초 프론트엔트 지식을 이용하여, 간단한 Admin page를 구성해보았습니다.
- 크롤링된 데이터의 카테고리별 조회, 상품명 조회, 상품명 검색, 선택 상품 삭제 기능 지원
- 현재 특정 웹사이트에서 크롤링한 데이터를 사용하여 상품을 자동으로 갱신하는 기능은 구현되어있지 않습니다.

<br>

## 개발 기간

- 2024-03-26 ~ 2024-03-27

<br>

## 기능

- **카테고리별 상품 조회** : 사용자는 상의, 하의, 신발, 패션잡화 등 카테고리를 선택하여 해당 카테고리의 상품 조회
- **상품명 검색** : 상품명을 입력하여 관련 상품 검색
- **선택한 상품 삭제** : 테이블의 체크박스를 사용하여 선택한 상품 삭제

<br>

## 기술 스택

- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
- ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

<br>

## 프로젝트 실행 및 사용 방법

1. 해당 GitHub 저장소를 Clone 합니다.
```bash
git clone https://github.com/your-github-username/your-project-repo.git
```

2. Clone이 저장된 디렉토리로 이동합니다.
```bash
cd clone저장경로
```

3. index.html 파일을 웹 브라우저에서 열어줍니다.
   - 상단의 Selector에서 카테고리를 선택하거나, 상단 input box에서 상품명을 검색하여 상품을 조회합니다.
   - 또는 조회된 항목에서, 체크박스로 원하는 상품을 선택 후, 우측 상단 선택항목 삭제 버튼을 눌러서 상품을 삭제해 줍니다.

<br>

## 프로젝트 구조
```yaml
Admin page
    │  .editorconfig
    │  .gitattributes
    │  .gitignore
    │  404.html
    │  favicon.ico
    │  icon.png
    │  icon.svg
    │  index.html
    │  LICENSE.txt
    │  package.json
    │  robots.txt
    │  site.webmanifest
    │  webpack.common.js
    │  webpack.config.dev.js
    │  webpack.config.prod.js
    │
    ├─.idea
    │  │  .gitignore
    │  │  jsLibraryMappings.xml
    │  │  misc.xml
    │  │  modules.xml
    │  │  vcs.xml
    │  │  workspace.xml
    │  │
    │  └─copilot
    │      └─chatSessions
    │          │  00000000000.xd
    │          │  xd.lck
    │          │
    │          └─blobs
    │                  version
    │
    ├─css
    │      style.css
    │
    ├─img
    │      .gitkeep
    │      github.png
    │
    └─js
        │  app.js
        │
        └─vendor
                .gitkeep
```
