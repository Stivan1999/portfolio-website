let menuButton = document.querySelector(".menu-button");
let cancelButton = document.querySelector(".cancel-button");
let navBar = document.querySelector(".navbar");
let aboutMeTitle = document.querySelector(".title");
menuButton.onclick = function () {
  menuButton.style.opacity = "0";
  menuButton.style.pointerEvents = "none";
  navBar.classList.add("active");
};
cancelButton.onclick = function () {
  menuButton.style.opacity = "1";
  menuButton.style.pointerEvents = "auto";
  navBar.classList.remove("active");
};
