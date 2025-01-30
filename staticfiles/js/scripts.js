alert("فایل جاوااسکریپت متصل است!");
function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('active');
}

document.addEventListener("DOMContentLoaded", function () {
    let index = 0;
    const slides = document.querySelector(".slides");
    const totalSlides = document.querySelectorAll(".slide").length;

    if (!slides) {
        console.error("Slides element not found.");
        return;
    }

    if (totalSlides === 0) {
        console.error("No slides found.");
        return;
    }

    function nextSlide() {
        index = (index + 1) % totalSlides;
        slides.style.transform = `translateX(-${index * 100}%)`; // استفاده از template literals
    }

    setInterval(nextSlide, 5000);
});