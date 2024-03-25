const container = document.getElementById('gameContainer');
const h1 = document.createElement('h1');
h1.textContent = '게임 시작';
container.appendChild(h1);

let damage = parseInt(prompt("1회 공격 시 데미지는 얼마인가요? (양의 정수로 입력하세요)")); // 1회 공격 시 데미지
if (damage <= 0) {
  alert("양의 정수로 입력해주세요.");
  throw new Error("양의 정수로 입력해주세요.");
}
let hp = 100
let hitCount = 0

while(hp > 0) {
  hp -= damage;

  const p = document.createElement('p');
  p.textContent = `몬스터를 ${++hitCount}회 공격했습니다.`;
  container.appendChild(p);

  if(hp <= 0) {
    const strong = document.createElement('strong');
    strong.textContent = `몬스터의 남은 체력: 0`;
    container.appendChild(strong);

    const h2 = document.createElement('h2');
    h2.textContent = '게임 종료. 몬스터를 물리쳤습니다.';
    h2.style.color = 'blue';
    container.appendChild(h2);
  }
  else {
    const strong = document.createElement('strong');
    strong.textContent = `몬스터의 남은 체력: ${hp}`;
    container.appendChild(strong);
  }
}


