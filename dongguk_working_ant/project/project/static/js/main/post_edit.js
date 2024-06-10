selectors = document.querySelectorAll('select');
function makescroll(selector){
    selector.setAttribute('onfocus', 'this.size=5');
    selector.setAttribute('onblur', 'this.size=1');
    selector.setAttribute('onchange', 'this.size=1');
}
selectors.forEach((selector) =>{
    selector.addEventListener("click", () => {
        console.log(selector);
        makescroll(selector);
    })
})