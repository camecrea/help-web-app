// Get the current URL
const currentUrl = window.location.pathname;

// Get the navbar links
const navbarLinks = document.querySelectorAll('#navbar a.nav-link');

// Loop through the links and add the active class to the current page link
navbarLinks.forEach(link => {
  if (link.getAttribute('href') === currentUrl) {
    link.classList.add('active');
  } else {
    link.classList.remove('active');
  }
});