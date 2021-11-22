function password_show_hide() {
  var x = document.getElementById("password");
  var show_eye = document.getElementById("show_eye");
  var hide_eye = document.getElementById("hide_eye");
  show_eye.classList.remove("d-none");
  if (x.type === "password") {
    x.type = "text";
    hide_eye.style.display = "none";
    show_eye.style.display = "block";
  } else {
    x.type = "password";
    hide_eye.style.display = "block";
    show_eye.style.display = "none";
  }
}