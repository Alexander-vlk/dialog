const btn = document.getElementById("scrollToTopBtn");
const footer = document.querySelector("footer");

window.addEventListener("scroll", () => {
  const scrollY = window.scrollY;
  const windowHeight = window.innerHeight;
  const docHeight = document.documentElement.scrollHeight;
  const footerHeight = footer.offsetHeight;

  if (scrollY > 150) {
    btn.classList.remove("hidden");
  } else {
    btn.classList.add("hidden");
  }

  const bottomOffset = 24;
  const distanceFromBottom = docHeight - (scrollY + windowHeight);

  if (distanceFromBottom < footerHeight) {
    btn.style.bottom = `${footerHeight - distanceFromBottom + bottomOffset}px`;
  } else {
    btn.style.bottom = "1.5rem";
  }
});

btn.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
