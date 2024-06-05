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



//정렬, 마감 공고, 근로 장소, 소득분위 선택
filter = document.querySelectorAll('#selector label')
console.log(filter[0].value);

console.log(document.querySelectorAll('.card'));

//스크랩 기능
function scrap(card){
    console.log(card);
    let star_img = document.querySelector(".star img");

    if(card.value == "none"){//value가 scraped로 바뀜
        card.value="scraped";          
        star_img.src = "http://127.0.0.1:8000/static/images/icons/blink_star.svg"
    } else{
        card.value="none";
        star_img.src = "http://127.0.0.1:8000/static/images/icons/star.svg"
    }   
}