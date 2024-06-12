
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

//정지윤 정렬 코드 테스트

// Sorting
function changeSelect_so(obj) {
    document.getElementById("so").value = obj.value
    document.getElementById("searchForm").submit()
}

function changeSelect_end(obj) {
    document.getElementById("end").value = obj.value
    document.getElementById("searchForm").submit()
}

function changeSelect_place(obj) {
    document.getElementById("place").value = obj.value
    document.getElementById("searchForm").submit()
}

function changeSelect_income(obj) {
    document.getElementById("income").value = obj.value
    document.getElementById("searchForm").submit()
}

// Search
document.getElementById('search').onkeydown = function(e) {
    // e.key를 사용하여 'Enter' 키를 확인합니다.
    if (e.key === 'Enter') {
        // ID가 "kw"인 요소의 값을 ID가 "inputSearch"인 요소의 값으로 설정
        document.getElementById("kw").value = document.getElementById("inputSearch").value;
        
        // ID가 "searchForm"인 폼을 제출
        document.getElementById("searchForm").submit();
    }
};
/*
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
*/