# Readme 추가 예정입니다 ㅇㅇ
- 아마 깔끔하게 모듈화, 객체지향으로 싹다 바꿔버리고 Readme.md 업데이트 할 예정

# 개발기간
2024.04.07 ~ 2024.04.08 (~ing)

# 실행파일
1. test폴더의 game.py 실행시키면 됩니다
2. main.py 실행해도 되는데, 텍스트 배치랑 그리드 생성 문제가 있어서 깔끔하지는 않습니다;; 

# 프로젝트 구조
```yaml
[Project] Onepiece Game
│  .DS_Store
│  main.py
│  readme.md
│
├─class_obj
│  │  GameSettings.py
│  │
│  └─__pycache__
│          GameSettings.cpython-312.pyc
│
├─images
│      Background.jpg
│      Luffy.png
│      Treasure.png
│
├─module
│  │  calculate_distance.py
│  │  draw_text.py
│  │  initialize_entities.py
│  │  keyboard_input_handler.py
│  │  settings_menu.py
│  │
│  └─__pycache__
│          calculate_distance.cpython-312.pyc
│          draw_text.cpython-312.pyc
│          initialize_entities.cpython-312.pyc
│          keyboard_input_handler.cpython-312.pyc
│          settings_menu.cpython-312.pyc
│
├─test
│      game.py
│
└─__pycache__
```
