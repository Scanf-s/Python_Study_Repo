const userSelectedCategory = document.getElementById('inlineFormSelectPref');
const deleteButton = document.getElementById('delete_button');
//현재 구현한 기능에서 searchButton은 딱히 필요 없음
const searchButton = document.getElementById('search_button');
const dataTable = document.getElementById('data-table');
const todaySpan = document.getElementById('today');

// 예시 데이터 (추후 크롤링으로 변경 예정)
const data = [
  {category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', gender: 'Common', price: '390,000'},
  {category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', gender: 'Men', price: '188,000'},
  {category: "신발", brand: 'Nike', product: '에어포스 1', gender: 'Common', price: '137,000'},
  {category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', gender: 'Women', price: '29,000'},
  // ...
];

/**
 * 검색 Event 감지 및 필터링 셋업 함수
 */
function search() {
  document.getElementById('merchant_search_bar').addEventListener('input', function () {
    const searchText = this.value;
    const selectedCategory = userSelectedCategory.value;
    filterDataByProductName(selectedCategory, searchText);
  });
}

/**
 * Gender Cell 생성 시, button element 생성해주는 함수
 * @param gender
 * @returns {HTMLButtonElement}
 */
function createGenderCell(gender) {
  const button = document.createElement('button');
  button.textContent = gender;
  if (gender === 'Men') {
    button.className = 'btn btn-light forMen';
  } else if (gender === 'Women') {
    button.className = 'btn btn-light forWomen';
  } else if (gender === 'Common') {
    button.className = 'btn btn-light';
  } else {
    button.className = 'btn btn-light';
  }
  return button;
}

/**
 * Product Cell 생성 시, mouseover, mouseleave event 추가해주는 함수
 */
function createProductCell(product) {
  const productCell = document.createElement('span');
  productCell.innerHTML = product;
  productCell.onmouseover = function () {
    productCell.style.color = 'red';
  }
  productCell.onmouseleave = function () {
    productCell.style.color = 'black';
  }
  return productCell;
}

/**
 * 테이블 생성 함수
 * @param item
 */
function createTableRow(item){
  const row = dataTable.insertRow();
  const checkboxCell = row.insertCell(0);
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkboxCell.appendChild(checkbox);

  row.insertCell(1).innerHTML = item.category;
  row.insertCell(2).innerHTML = item.brand;
  const productCell = row.insertCell(3);
  productCell.appendChild(createProductCell(item.product));
  const genderCell = row.insertCell(4);
  genderCell.appendChild(createGenderCell(item.gender));
  row.insertCell(5).innerHTML = item.price;
}

/**
 * 테이블 최초 초기화 함수
 */
function initializeTable() {
  data.forEach((item) => {
    createTableRow(item)
  });
}

/**
 * 카테고리 기준 필터링 함수
 * @param selectedCategory
 */
function filterData(selectedCategory) {
  //필터링 하기 전에, 테이블 초기화
  while (dataTable.rows.length > 0) {
    dataTable.deleteRow(0);
  }

  let categoryString;
  switch (selectedCategory) {
    case 'tops':
      categoryString = '상의';
      break;
    case 'bottoms':
      categoryString = '하의';
      break;
    case 'shoes':
      categoryString = '신발';
      break;
    case 'accessories':
      categoryString = '패션잡화';
      break;
    default:
      categoryString = '';
      break;
  }

  data.forEach((item) => {
    if (item.category === categoryString || categoryString === '') {
      createTableRow(item);
    }
  });
}

/**
 * 상품명 기준 필터링 함수
 * @param selectedCategory
 * @param searchText
 */
function filterDataByProductName(selectedCategory, searchText) {
  //필터링 하기 전에, 테이블 초기화
  while (dataTable.rows.length > 0) {
    dataTable.deleteRow(0);
  }

  data.forEach((item) => {
    console.log(item.product.includes(searchText), selectedCategory, item.category, searchText);
    //카테고리 상태가 전체 or 사용자가 선택한 카테고리에 대해서,
    //검색어가 포함된 상품명을 가진 상품만 테이블에 추가해줌
    if ((selectedCategory === item.category || selectedCategory === 'all') && item.product.includes(searchText)) {
      createTableRow(item);
    }
  });
}

/**
 * 현재 시간 설정 함수
 */
function setTime() {
  let today = new Date();
  let year = today.getFullYear();
  let month = today.getMonth() + 1;
  let date = today.getDate();
  todaySpan.innerHTML = `( ${year}년 ${month}월 ${date}일 )`;
}

/**
 * 메인 함수
 */
function main() {
  if (dataTable.rows.length === 0) {
    initializeTable()
  }

  setTime();
  search();

  /**
   * 사용자가 필터를 선택하면, eventListener가 감지해서 상품 필터링 수행
   */
  userSelectedCategory.addEventListener('change', (event) => {
    const selectedCategory = event.target.value;
    console.log(selectedCategory);
    filterData(selectedCategory);
  });

  searchButton.addEventListener('click', () => {
    alert('[조회] 버튼은 성능 저하 및 소스코드 개선 필요시 추가할 예정입니다. 현재는 구현되어 있지 않습니다.')
  });

  /**
   * 사용자가 체크박스를 선택하고, 삭제 버튼을 누르는 event 발생 시, 체크된 row를 삭제
   */
  deleteButton.addEventListener('click', () => {
    // row를 js를 통해 삽입하므로, tr tag로 일단 모든 row를 가져와야함
    const rows = dataTable.getElementsByTagName('tr');
    for (let i = rows.length - 1; i >= 0; i--) {
      const row = rows[i];
      // 체크박스는 첫번째 cell에 위치하므로, 체크박스가 체크되어 있는지 확인
      const checkbox = row.getElementsByTagName('input')[0];
      if (checkbox && checkbox.checked) {
        dataTable.deleteRow(i);
      }
    }
  });
}

//js 실행
main()

