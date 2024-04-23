const form = document.getElementById('form');
form.addEventListener("submit", function(event){
  event.preventDefault(); //새로고침 차단 (기존 기능 차단)
  let userId = event.target.id.value;
  let password = event.target.password.value;
  let confirmPassword = event.target.confirm_password.value;
  let email = event.target.email.value;
  let name = event.target.name.value;
  let job = event.target.job.value;
  let gender = event.target.gender.value;
  let extraInfo = event.target.extra_info.value;

  if(!userId){
    alert('아이디를 입력해주세요.');
    return;
  }
  if(!password){
    alert('비밀번호를 입력해주세요.');
    return;
  }
  if(!confirmPassword){
    alert('비밀번호 확인을 입력해주세요.');
    return;
  }
  if(userId.length < 6){
    alert('아이디는 6자 이상 입력해주세요.');
    return;
  }
  if(password !== confirmPassword){
    alert('확인 비밀번호가 일치하지 않습니다.');
    return;
  }

  // 가입 완료 시
  document.body.innerHTML = "";
  document.write(`<p>${userId}님 가입을 환영합니다.</p>`);
  document.write(`<p>회원 가입 시 입력한 내역은 다음과 같습니다.</p>`);
  document.write(`<p>아이디: ${userId}</p>`);
  document.write(`<p>이름: ${name}</p>`);
  document.write(`<p>이메일 : ${email}</p>`);
  document.write(`<p>직업: ${job}</p>`);
})
