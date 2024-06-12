//정지윤 정렬 코드 테스트

// Sorting
function changeSelect_so(obj) {
    document.getElementById("so").value = obj.value
    document.getElementById("searchForm").submit()
}

function changeSelect_end(obj) {
    document.getElementById("en").value = obj.value
    document.getElementById("searchForm").submit()
}

function changeSelect_place(obj) {
    console.log("장소값"+document.getElementById("pl").value)
    document.getElementById("pl").value = obj.value
    document.getElementById("searchForm").submit()
}

function changeSelect_income(obj) {
    document.getElementById("inc").value = obj.value
    document.getElementById("searchForm").submit()
}