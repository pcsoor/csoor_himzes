const thumbs = document.querySelector(".thumb-img").children;

function changeImage(event, attribute) {
  document.querySelector(".pro-img").src = event.children[0].src;

  for (let i = 0; i < thumbs.length; i++) {
    thumbs[i].classList.remove("active-color");
  }
  event.classList.add("active-color");
}

