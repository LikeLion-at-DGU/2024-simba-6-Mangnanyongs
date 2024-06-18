
document.addEventListener('DOMContentLoaded', (event) => {
    const btnPrev = document.querySelector('.btnPrev');
    const btnNext = document.querySelector('.btnNext');
    const slideFrame = document.querySelector('.slideFrame');
    const slideCards = document.querySelector('.slideCards');
    const slides = document.querySelectorAll('.slide');
    const slideWidth = 295;
    const slideGap = 100;
    const moveDistance = slideWidth + slideGap;

    let currentIndex = 0;
    const slideCount = slides.length;

    // 슬라이드를 3번 복사하여 붙이기
    for (let i = 0; i < 3; i++) {
        slides.forEach(slide => {
            const cloneSlide = slide.cloneNode(true);
            slideCards.appendChild(cloneSlide);
        });
    }

    // 슬라이드 카드 갯수 갱신
    const allSlides = document.querySelectorAll('.slide');
    const newSlideCount = allSlides.length;

    // 슬라이드 카드의 전체 너비를 동적으로 설정
    slideCards.style.width = `${newSlideCount * moveDistance - slideGap}px`;

    // 초기 위치 설정
    slideCards.style.transition = 'none';
    slideCards.style.transform = `translateX(${-moveDistance}px)`;
    currentIndex = slideCount;

    function updateSlidePosition() {
        const newTransformValue = -currentIndex * moveDistance;
        slideCards.style.transition = 'transform 0.5s ease-in-out';
        slideCards.style.transform = `translateX(${newTransformValue}px)`;
        
        // 모든 슬라이드의 불투명도 설정
        allSlides.forEach(slide => slide.classList.remove('active'));
        
        // 가운데 슬라이드의 인덱스를 계산하고 활성화
        const centerIndex = (currentIndex + Math.floor(slideCount / 2)) % newSlideCount;
        allSlides[centerIndex].classList.add('active');
    }

    slideCards.addEventListener('transitionend', () => {
        if (currentIndex === 0) {
            slideCards.style.transition = 'none';
            currentIndex = slideCount;
            slideCards.style.transform = `translateX(${-currentIndex * moveDistance}px)`;
        } else if (currentIndex >= newSlideCount - slideCount) {
            slideCards.style.transition = 'none';
            currentIndex = currentIndex % slideCount;
            slideCards.style.transform = `translateX(${-currentIndex * moveDistance}px)`;
        }
    });

    btnPrev.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateSlidePosition();
        } else {
            currentIndex = newSlideCount - slideCount;
            slideCards.style.transition = 'none';
            slideCards.style.transform = `translateX(${-currentIndex * moveDistance}px)`;
            setTimeout(() => {
                currentIndex--;
                updateSlidePosition();
            }, 50);
        }
    });

    btnNext.addEventListener('click', () => {
        if (currentIndex < newSlideCount - 1) {
            currentIndex++;
            updateSlidePosition();
        } else {
            currentIndex = slideCount;
            slideCards.style.transition = 'none';
            slideCards.style.transform = `translateX(${-currentIndex * moveDistance}px)`;
            setTimeout(() => {
                currentIndex++;
                updateSlidePosition();
            }, 50);
        }
    });

    // 초기 불투명도 설정
    setTimeout(() => {
        updateSlidePosition(); // 초기 상태 설정
    }, 50);
});