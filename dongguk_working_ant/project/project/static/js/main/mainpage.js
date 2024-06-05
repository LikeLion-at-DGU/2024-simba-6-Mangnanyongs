document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.slideUl');
    const slides = document.querySelectorAll('.slideCard');
    const prevBtn = document.querySelector('.btnPrev');
    const nextBtn = document.querySelector('.btnNext');
    const totalSlides = slides.length;
    let currentIndex = 0;

    function updateSlidePosition() {
        slides.forEach((slide, index) => {
            slide.classList.remove('active');
            slide.style.transform = `translateX(-${currentIndex * 100}%)`;
            if (index === currentIndex) {
                slide.classList.add('active');
            }
        });
        updateActiveCards();
    }

    function updateActiveCards() {
        slides.forEach((slide, index) => {
            slide.style.opacity = 0.5;
            if (index === currentIndex || 
                index === (currentIndex + 1) % totalSlides || 
                index === (currentIndex + 2) % totalSlides) {
                slide.style.opacity = 1;
            }
        });
    }

    prevBtn.addEventListener('click', function() {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        updateSlidePosition();
    });

    nextBtn.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateSlidePosition();
    });

    updateSlidePosition();
});
