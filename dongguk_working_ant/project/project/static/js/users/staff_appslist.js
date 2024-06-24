document.addEventListener('DOMContentLoaded', () => {
    const passBtn = document.getElementById('pass');
    const failBtn = document.getElementById('fail');
    const passModal = document.getElementById('passModal');
    const failModal = document.getElementById('failModal');
    const resultModal = document.getElementById('resultModal');
    const resultMessage = document.getElementById('resultMessage');
    const passConfirmBtn = document.getElementById('passConfirm');
    const failConfirmBtn = document.getElementById('failConfirm');
    const cancelBtns = document.querySelectorAll('#cancel');
    const resultCloseBtn = document.getElementById('resultClose');

    passBtn.addEventListener('click', () => {
        passModal.style.display = 'flex';
    });

    failBtn.addEventListener('click', () => {
        failModal.style.display = 'flex';
    });

    passConfirmBtn.addEventListener('click', () => {
        passModal.style.display = 'none';
        resultMessage.textContent = '합격 처리되었어요!';
        resultModal.style.display = 'flex';
    });

    failConfirmBtn.addEventListener('click', () => {
        failModal.style.display = 'none';
        resultMessage.textContent = '불합격 처리되었어요!';
        resultModal.style.display = 'flex';
    });

    cancelBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            passModal.style.display = 'none';
            failModal.style.display = 'none';
        });
    });

    resultCloseBtn.addEventListener('click', () => {
        resultModal.style.display = 'none';
    });
});