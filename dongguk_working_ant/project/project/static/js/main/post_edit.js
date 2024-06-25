//모달 동작
const modal_button = document.querySelector("#day_time img");
const modal = document.getElementById('modal');
const submit = document.getElementById('submit_time');
const cancel = document.getElementById('cancel_time');

modal_button.addEventListener('click', function(){
  modal.style.display='block';
});

submit.addEventListener('click', function(){
  d_day = document.querySelector('input[name="discussion_day"]:checked').value;
  d_time = document.querySelector('input[name="discussion_time"]:checked').value;

  if(d_day == "지정"){
    work_day = document.getElementById('work_day').value;
    console.log(work_day);
    if(work_day==""){
      alert("요일을 입력해주세요");
      return;
    }
    day_option = document.querySelectorAll('#work_day option');
    day_option.forEach( option => {
      if(work_day == option.value){
        day = option.textContent;
      }
    });
  } else{
    day = "요일협의";
  }

  if(d_time == "지정"){
    time_option = document.querySelectorAll('#select_start_time option');
    start_time = document.getElementById('select_start_time').value;
    end_time = document.getElementById('select_end_time').value;
    
    if(start_time == "" || end_time == ""){
      alert("시간을 입력해주세요");
      return;
    }
    if(parseInt(start_time) >= parseInt(end_time)){
      alert("시작 시간이 종료 시간보다 늦을 수는 없습니다.");
      return;
    }
    time_option.forEach(option =>{
      if(start_time == option.value){
        start_time_ = option.textContent;
      }
    });
    time_option.forEach(option =>{
      if(end_time == option.value){
        end_time_ = option.textContent;
      }
    });
    time = start_time_ + '~' + end_time_;
  } else{
    time = "시간협의";
  }

  input = document.getElementById('input_day_time');
  input.value = day + ' '+ time;

  console.log(input.value);
  modal.style.display="none";
});

//취소버튼
cancel.addEventListener('click', function(){
  modal.style.display="none";
})


//모집인원 직접 입력 버튼
const topElement = document.querySelector("#contents .top");
const selectElement = document.getElementById("recruit_count");
const directInputSpan = document.createElement("span");
directInputSpan.style =
  "width: 201px; height: 31px; display:flex; align-items: center; flex-shrink: 0; border-radius: 20px; background: #FFF; border: 1px solid gray; box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.08)";

const directInput = document.createElement("input"); //directInputSpan 정의
directInput.type = "number";
directInput.name = "recruitment";
directInput.style = "Input_space";
directInput.id = "selboxDirect";
directInput.style = "border:none; width:160px; margin-left: 7px; height: 17px;";

selectElement.addEventListener("change", function () {
  const selectedValue = selectElement.value;

  if (selectedValue == "6") {
    selectElement.remove();
    topElement.appendChild(directInputSpan);
    directInputSpan.appendChild(directInput);
  }
});

//새로운 detail 만들기

let detailsContainer = document.getElementById("details");
let detailTemplate = document.querySelector(".detail"); // 기존 detail 요소를 템플릿으로 사용

//세부사항 추가 버튼
function add_detail() {
  // 새로운 detail 요소 생성 및 복사
  const newDetail = detailTemplate.cloneNode(true);
  newDetail.style.display = 'flex';

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
    detailsContainer.appendChild(add_detail()); //새로운 템플릿 생성
  }
}

//교직원 맨 아래 +버튼
document.querySelector("#add_question img").addEventListener("click", function () {
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

//페이지 로드 시 질문 개수만큼 칸 생성
document.addEventListener("DOMContentLoaded", function () {
  let questionNumber = document.getElementById("question_count").value;
  let questionsData = document.getElementById("questions_data").children;

  for (i = 2; i <= questionNumber; i++) {
  let obj = document.getElementById("main3");
  let qborder = document.querySelector(".q_border:last-of-type"); // 마지막 q_border 요소 선택
  let newDiv = qborder.cloneNode(true); // 전체 내용을 복사

  // 질문 개수 저장
  document.getElementById("question_count").value = questionNumber;
  console.log(document.getElementById("question_count").value);

  
    // 새로운 질문 번호 설정
    newDiv.querySelector(".orange").textContent = i + ".";
  
    // 새로운 input 요소의 name 속성 설정
    let newInput = newDiv.querySelector('input[name^="question"]'); // question으로 시작하는 첫 번째 input 요소 선택
    if (newInput) {
      // input 요소가 존재하는 경우에만 name 속성을 변경
      newInput.setAttribute("name", "question" + i);
      
      // 질문 데이터를 가져와서 value 속성에 설정
      let questionContent = questionsData[i - 1].getAttribute('data-question');
      newInput.setAttribute("value", questionContent);
    }

    // obj 내의 q_border 요소들 중 마지막 요소의 다음에 newDiv를 삽입
    obj.insertBefore(newDiv, qborder.nextElementSibling);
  }
});
