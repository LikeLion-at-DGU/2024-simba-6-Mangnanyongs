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
