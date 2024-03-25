const todaySpan = document.querySelector('#today');
const numbersDiv = document.querySelector('.numbers');
const drawButton = document.querySelector('#draw');
const resetButton = document.querySelector('#reset');

let lottoNumbers = []
let today = new Date()
let year = today.getFullYear()
let month = today.getMonth() + 1
let date = today.getDate()
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `

function printNumber(number){
  const eachNumber = document.createElement("span")
  eachNumber.classList.add("eachNumber")
  eachNumber.textContent = number + ' '
  numbersDiv.appendChild(eachNumber)
}

//랜덤 숫자 생성
drawButton.addEventListener('click', () => {
  if (lottoNumbers.length === 6 || lottoNumbers.length === 0) {
    lottoNumbers = []
    numbersDiv.innerHTML = ''
    while(lottoNumbers.length < 6) {
      let number = Math.floor(Math.random() * 45) + 1; // 1 ~ 45까지 랜덤 정수 생성
      if(!lottoNumbers.includes(number)) {
        lottoNumbers.push(number);
        printNumber(number);
      }
    }
  }
});

resetButton.addEventListener('click', () => {
  lottoNumbers = [];
  numbersDiv.innerHTML = '';
});
