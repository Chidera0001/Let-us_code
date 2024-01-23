// Additional script for entrance animation
document.addEventListener("DOMContentLoaded", function () {
  const logo = document.getElementById("netflix-logo");
  const loginContainer = document.getElementById("login-container");

  // Trigger entrance animation for logo
  logo.classList.add("show");

  // Add a delay before showing the login container
  setTimeout(function () {
    loginContainer.classList.add("show");
  }, 1000); // 1000ms delay (1s)
});
