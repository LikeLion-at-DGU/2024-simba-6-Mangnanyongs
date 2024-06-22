/*document.addEventListener('DOMContentLoaded', function(){
    var selectElements = document.querySelectorAll('select');
    selectElements.forEach(selectElement => {
        selectElement.addEventListener('focus', function(){
            this.size=5;
        });
        selectElement.addEventListener('blur', function(){
            this.size = 1;
        });
        selectElement.addEventListener('change', function(){
            this.size = 1;
            this.blur();
        });
    });
});*/

//모집인원 직접 입력 버튼
const topElement = document.querySelector('#contents .top');
const selectElement = document.getElementById('recruit_count');
const directInputSpan = document.createElement('span');
directInputSpan.style = 'width: 200px; height: 30px; display:flex; align-items: center; flex-shrink: 0; border-radius: 20px; background: #FFF; border: 1px solid gray; box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.08)'

const directInput = document.createElement('input'); //directInputSpan 정의
directInput.type = 'number';
directInput.name = 'recruitment';
directInput.style = 'Input_space'
directInput.id = 'selboxDirect';
directInput.style = 'border:none; width:160px; margin-left: 7px; height: 17px;'

selectElement.addEventListener('change', function(){
  const selectedValue = selectElement.value;
  
  if(selectedValue == 'direct'){
    selectElement.remove();
    topElement.appendChild(directInputSpan)
    directInputSpan.appendChild(directInput);
  } 
});


//새로운 detail 만들기

let detailsContainer = document.getElementById("details");
let detailTemplate = document.querySelector(".detail"); // 기존 detail 요소를 템플릿으로 사용

// 새로운 detail 요소 생성 및 복사
const newDetail = detailTemplate.cloneNode(true);

//세부사항 추가 버튼
function add_detail() {
  // form 태그 안에 새로운 detail 추가
  detailsContainer.appendChild(newDetail);
}

//세부사항 삭제 버튼
function delete_detail(selected) {
  let parent_detail = selected.parentNode;
  let grand_detail = parent_detail.parentNode;

  parent_detail.remove();
  console.log(grand_detail.querySelectorAll(".detail")[0]);
  if (grand_detail.querySelectorAll(".detail")[0] == undefined) {
    //첫 요소가 삭제되면
    console.log(newDetail);
    detailsContainer.appendChild(newDetail); //새로운 템플릿 생성
  }
}

//교직원 맨 아래 +버튼
document
  .querySelector("#add_question img")
  .addEventListener("click", function () {
    let obj = document.getElementById("main3");
    let qborder = document.querySelector(".q_border:last-of-type"); // 마지막 q_border 요소 선택
    let newDiv = qborder.cloneNode(true); // 전체 내용을 복사

    // 새로운 질문 번호 설정
    let questionNumber = obj.querySelectorAll(".q_border").length + 1;
    newDiv.querySelector(".orange").textContent = questionNumber + ".";

    // 질문 개수 저장
    document.getElementById("question_count").value = questionNumber;
    console.log(document.getElementById("question_count").value);

    // 새로운 input 요소의 name 속성 설정
    let newInput = newDiv.querySelector('input[name^="question"]'); // question으로 시작하는 첫 번째 input 요소 선택
    if (newInput) {
      // input 요소가 존재하는 경우에만 name 속성을 변경
      newInput.setAttribute("name", "question" + questionNumber);
    }

    // 새로운 input 요소의 value 초기화 (필요한 경우)
    newInput.value = "";

    // obj 내의 q_border 요소들 중 마지막 요소의 다음에 newDiv를 삽입
    obj.insertBefore(newDiv, qborder.nextElementSibling);
  });
