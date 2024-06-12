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

//세부사항 추가 버튼
function add_detail(){
    let detailsContainer = document.getElementById('details');
    let detailTemplate = document.querySelector('.detail'); // 기존 detail 요소를 템플릿으로 사용
    
    // 새로운 detail 요소 생성 및 복사
    let newDetail = detailTemplate.cloneNode(true);
    
    console.log(newDetail);

    // form 태그 안에 새로운 detail 추가
    detailsContainer.appendChild(newDetail);
}

//세부사항 삭제 버튼
function delete_detail(selected){
    let parent_detail = selected.parentNode;
    let grand_detail = parent_detail.parentNode;
    let detailsContainer = document.getElementById('details');
    let detailTemplate = document.querySelector('.detail');
    let newDetail = detailTemplate.cloneNode(true);

    parent_detail.remove();
    console.log(grand_detail.querySelectorAll('.detail')[0]);
    if(grand_detail.querySelectorAll('.detail')[0]==undefined){ //첫 요소가 삭제되면
        console.log(newDetail);
        detailsContainer.appendChild(newDetail); //새로운 템플릿 생성
    }
} 



//교직원 맨 아래 +버튼
document.getElementById('add_question').addEventListener('click', function() {
    let obj = document.getElementById('main3');
    let qborder = document.querySelector('.q_border'); // 첫 번째 q_border 요소 선택
    let newDiv = qborder.cloneNode(true); // 전체 내용을 복사
    
    // 새로운 질문 번호 설정
    let questionNumber = obj.querySelectorAll('.q_border').length + 1;
    newDiv.querySelector('.orange').textContent = questionNumber + '.';

    // 새로운 form 요소의 name 속성 설정
    let newForm = newDiv.querySelector('form[name="question1"]');
    newForm.setAttribute('name', 'question' + questionNumber);

    obj.insertBefore(newDiv, document.getElementById('add_question'));
});
