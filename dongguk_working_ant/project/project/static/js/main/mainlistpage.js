//전체 교내 학과 선택
document.addEventListener("DOMContentLoaded", () => {
    buttons = document.querySelectorAll('#filter .button'); //버튼 지정 (배열)
    const defaultButton = document.getElementById('all'); // 기본값으로 지정할 버튼

    defaultButton.classList.replace("unchecked", "checked"); //초기에 표시
    if(defaultButton){console.log(1);} //django에서 값을 받아오면 완성

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            buttons.forEach(btn => btn.classList.replace("checked", "unchecked"));
            button.classList.replace("unchecked", "checked");
            if(button.value == '교내'){ //django에서 값을 받아오면 완성
                console.log(2);
            } else if(button.value == '학과'){
                console.log(3);
            } else{
                console.log(1);
            }
        })
    });
})

//검색 기능
textfield = document.getElementById('search');
submit = document.querySelector('#submit');

submit.addEventListener('click', () => {
    console.log(textfield.value);
})

//정렬, 마감 공고, 근로 장소, 소득분위 선택
selector = document.getElementById('selector');
selector.addEventListener('change', function(event) {
    event.preventDefault();

    selects = selector.querySelectorAll("select");
    
    selects.forEach((select) =>{
        console.log(select.value);
    })   
});

//스크랩 기능
function scrap(star) {
    let star_img = star.querySelector("img");

    if (star.value == "none") { // value가 scraped로 바뀜
        star.value = "scraped";          
        star_img.src = "http://127.0.0.1:8000/static/images/icons/blink_star.svg";
    } else {
        star.value = "none";
        star_img.src = "http://127.0.0.1:8000/static/images/icons/star.svg";
    }   
}