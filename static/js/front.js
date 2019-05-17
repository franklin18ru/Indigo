$("ul").click(function(event){
  event.stopPropagation();
});

var toggler = document.getElementsByClassName("toggle");
var i;
for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

onclick