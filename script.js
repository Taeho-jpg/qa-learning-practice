const name = "เรา เต๋าเองนะ";
const greeting = `สวัสดี ${name}!`;
const ul = document.querySelector('ul')
const btn = document.querySelector('#add-btn')
const delBtn = document.querySelector('#del-btn')
const deletedSkills = []

function showGreeting() {
  const h1 = document.querySelector('h1')
  
  if (h1.textContent === greeting) {
    // ถ้าเป็น greeting อยู่แล้ว → กลับไปเป็นชื่อเดิม
    h1.textContent = name
  } else {
    // ถ้าเป็นชื่อเดิม → เปลี่ยนเป็น greeting
    h1.textContent = greeting
  }
}
function addskill() {
  const li = document.createElement('li')
  if (deletedSkills.length > 0) {
    // ถ้ามีของที่เคยลบไป → เอากลับมา
    li.textContent = deletedSkills.pop()
  } else {
    // ถ้าไม่มี → เพิ่ม React Coming Soon
    li.textContent = 'React — Coming Soon'
  }
  ul.appendChild(li)
}

function deleteskill() {
  const lastLi = ul.querySelector('li:last-child')
  if (lastLi) {
    deletedSkills.push(lastLi.textContent)  // เก็บข้อความไว้ก่อน
    ul.removeChild(lastLi)                  // แล้วค่อยลบ
  }
}

delBtn.addEventListener('click', deleteskill)
btn.addEventListener('click', addskill)

document.querySelector('h1').addEventListener('click', showGreeting)

console.log(greeting);