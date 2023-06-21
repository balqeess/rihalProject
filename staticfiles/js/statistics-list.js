// JS code for toggling dark/light mode
let toggleDark = document.querySelector("#toggleDark");

toggleDark.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});
