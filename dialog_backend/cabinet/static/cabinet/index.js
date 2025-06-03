document.addEventListener("DOMContentLoaded", function(e) {
    const swiper = new Swiper('.swiper', {
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
    const advantageSwiper = new Swiper('.advantage-swiper', {
        spaceBetween: 20,
        initialSlide: 1,
        slidesPerView: 1,
        slidesPerGroup: 1,
        pagination: {
            el: '.advantage-swiper-pagination',
            clickable: true,
        },
    });
})
