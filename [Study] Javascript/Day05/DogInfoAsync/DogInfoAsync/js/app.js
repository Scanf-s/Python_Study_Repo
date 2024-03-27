const apiRandomDogs = "https://dog.ceo/api/breeds/image/random/42";
const apiAllBreeds = "https://dog.ceo/api/breeds/list/all";
const requestForRandomDogs = new XMLHttpRequest();
const requestForAllBreeds = new XMLHttpRequest();

const header = document.getElementById("header");
const main = document.getElementById("main");
const input = document.getElementById("filter-text");
const button = document.getElementById("filter-button");
const select = document.getElementById("filter-select");
const tothetop = document.getElementById("tothetop");
const more = document.getElementById("more");
const dogImageRefresh = document.getElementById("refresh");

const currentDogs = [];

/**
 * 강아지 사진을 화면에 출력하는 함수
 * @param item
 */
function displayDogs(item){
  const dogImgDiv = document.createElement("div");
  dogImgDiv.classList.add("flex-item");
  dogImgDiv.innerHTML = `<img src="${item}" alt="dog">`;
  main.appendChild(dogImgDiv);
}

/**
 * 강아지 사진 불러오는 함수
 */
function fetchRandomDogs() {
  requestForRandomDogs.open("GET", apiRandomDogs);
  requestForRandomDogs.addEventListener("load", function () {
    const response = JSON.parse(requestForRandomDogs.response); //response로 강아지 사진이 담긴 배열을 받아옴
    response.message.forEach(function (dog) {
      currentDogs.push(dog); //currentDogs 배열에 강아지 사진을 하나씩 넣어줌
      displayDogs(dog);
    });
  });
  requestForRandomDogs.send();
}

/**
 * select 요소에 모든 견종 정보를 뿌려서 사용자가 선택할 수 있도록 만듬
 */
function fetchAllBreeds() {
  requestForAllBreeds.open("GET", apiAllBreeds);
  requestForAllBreeds.addEventListener("load", function () {
    const response = JSON.parse(requestForAllBreeds.response);
    //console.log("데이터를 가져왔습니다.", typeof response.message, response.message);
    //각 키에 견종이 있고, 그 값에는 견종의 세부 종류가 배열로 들어있는 형태
    //데이터로부터 키를 추출하는 방법 : Object.keys(받아온 데이터)
    Object.keys(response.message).forEach(function (breed) {
      const option = document.createElement("option");
      option.value = breed;
      option.innerText = breed;
      select.appendChild(option);
    });
  });
  requestForAllBreeds.send();
}

function whenStart() {
  window.addEventListener("load", function () {
    fetchAllBreeds();
    fetchRandomDogs();
  });

  button.addEventListener("click", function () {
    //필터링 전에 싹 지워줌
    main.innerHTML = "";

    let filteredDogs = currentDogs.filter(function (item) {
      // API로부터 받아온 견종 정보에 대해서 (item)
      // 각 item 정보에 사용자가 입력한 견종 정보가 포함되어 있으면 1을 반환
      // 포함되어 있지 않으면 -1을 반환
      // 아무것도 안써있으면 0을 반환 (전부 보여줌)
      return item.indexOf(input.value) !== -1;
    });

    filteredDogs.forEach(function (dog) {
      displayDogs(dog);
    });
  });

  select.addEventListener("change", function () {
    //필터링 전에 싹 지워줌
    main.innerHTML = "";

    let filteredDogs = currentDogs.filter(function (item) {
      // API로부터 받아온 견종 정보에 대해서 (item)
      // 각 item 정보에 사용자가 선택한 견종 정보가 포함되어 있으면 1을 반환
      // 포함되어 있지 않으면 -1을 반환
      // 아무것도 안써있으면 0을 반환 (전부 보여줌)
      return item.indexOf(select.value) !== -1;
    });

    filteredDogs.forEach(function (dog) {
      displayDogs(dog);
    });
  });

  tothetop.addEventListener("click", function () {
    window.scrollTo({top: 0});
  });

  more.addEventListener("click", function () {
    fetchRandomDogs();
  });

  dogImageRefresh.addEventListener("click", function () {
    main.innerHTML = "";
    fetchRandomDogs();
  });
}

// 스크립트 실행
whenStart();

