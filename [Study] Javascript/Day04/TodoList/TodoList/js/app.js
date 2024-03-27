// 요소 선택 및 배열 선언
const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')
let todoArr = [];

/**
 * displayTodos 함수
 * todoArr 배열에 있는 데이터를 화면에 출력
 * todoItem은 li, todoDelBtn은 span으로 생성하며, 각 속성을 설정해줌.
 * 그리고 추가된 요소에 대해 event listener를 추가해줘서 클릭 시 삭제 및 todoDone 여부 변경
 */
function displayTodos(){
  todoList.innerHTML = ""
  //li, span 생성해서 todoList에 추가
  todoArr.forEach((aTodo) => {
    const todoItem = document.createElement('li')
    const todoDelBtn = document.createElement('span')
    todoDelBtn.innerText = 'x'
    todoDelBtn.title = '클릭시 삭제'
    todoItem.innerText = aTodo.todoText
    todoItem.title = '클릭시 완료'
    todoItem.classList.add(aTodo.todoDone ? 'done' : 'yet')
    todoItem.appendChild(todoDelBtn)
    todoDelBtn.addEventListener('click', function(){
      handleTodoDelBtnClick(aTodo.todoId)
    })
    todoItem.addEventListener('click', function(){
      handleTodoItemClick(aTodo.todoId)
    })
    todoList.appendChild(todoItem)
  });
}

/**
 * 배열메소드 filter 사용하여,
 * 사용자가 클릭한 todoId와 일치하는 todoId를 가진 요소를 제외한
 * 나머지 요소들(삭제 안한 요소들)만 남기고 새로운 배열을 반환
 * 이후, 나머지 요소들에 대해서 displayTodos 함수를 호출하여 화면에 출력
 * @param clickedId
 */
function handleTodoDelBtnClick(clickedId){
  todoArr = todoArr.filter(function(aTodo){
    return aTodo.todoId !== clickedId
  })
  displayTodos()
  saveTodos()
}

/**
 * 배열메소드 map 사용하여,
 * 사용자가 클릭한 todoId와 일치하는 todoId를 가진 요소만 찾아서
 * todoDone 속성을 반대로 변경 (해야할 일을 완료했다는 뜻)
 * @param clickedId
 */
function handleTodoItemClick(clickedId){
  todoArr = todoArr.map(function(aTodo){
    return aTodo.todoId !== clickedId ?
      aTodo : { ...aTodo, todoDone: !aTodo.todoDone }
  })
  displayTodos()
  saveTodos()
}

/**
 * saveTodos 함수
 * 사용자가 입력한 todo data를 JSON 형태로 localStorage에 저장
 */
function saveTodos(){
  const todoSting = JSON.stringify(todoArr)
  localStorage.setItem('myTodos', todoSting)
}

/**
 * loadTodos 함수
 * localStorage에 저장된 todo data를 불러와서 화면에 출력
 */
function loadTodos(){
  const myTodos = localStorage.getItem('myTodos')
  todoArr = myTodos !== null ? JSON.parse(myTodos) : todoArr
  displayTodos()
}

// 할일 입력 후 제출하면 발생하는 이벤트 핸들링
todoForm.addEventListener('submit', function(e){
  e.preventDefault()
  const toBeAdded = {
    todoText: todoForm.todo.value,
    todoId: new Date().getTime(),
    todoDone: false
  }
  todoForm.todo.value = ""
  todoArr.push(toBeAdded)
  displayTodos()
  saveTodos()
})

loadTodos() // 시작할 때 한번만!
