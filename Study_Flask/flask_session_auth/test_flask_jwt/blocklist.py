# jSON 토큰을 관리하는 파일
BLOCKLIST = set()


def add_to_blocklist(jti):
    BLOCKLIST.add(jti)


def remove_from_blocklist(jti):
    BLOCKLIST.remove(jti)