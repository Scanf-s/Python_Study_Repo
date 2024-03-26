const item = document.getElementById('item');
document.getElementById("set").addEventListener("click", function() {
  window.localStorage.setItem("익명사용자", item.textContent)
})
document.getElementById("get").addEventListener("click", function() {
  if(window.localStorage.getItem("익명사용자") === null) {
    alert("익명사용자가 없습니다.")
    return
  }
  alert(window.localStorage.getItem("익명사용자"))
})
document.getElementById("remove").addEventListener("click", function() {
  window.localStorage.removeItem("익명사용자")
})
document.getElementById("clear").addEventListener("click", function() {
  window.localStorage.clear()
})

window.localStorage.setItem("커피", JSON.stringify({
  name: "아메리카노",
  price: 3000,
  taste: "쓰다"
}))
