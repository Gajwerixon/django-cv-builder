// Navbar

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 10);
});


// Testemonios

const trustedTrack = document.querySelector(".trusted-by-track");
const trustedGroup = document.querySelector(".trusted-by-group");

if (trustedTrack && trustedGroup) {
    const updateAnimation = () => {
        const width = trustedGroup.offsetWidth;

        trustedTrack.style.setProperty("--scroll-width", `${width}px`);
    };

    updateAnimation();
    window.addEventListener("resize", updateAnimation);
}


// Template Gallery

const galleryTrack = document.querySelector(".gallery-track");
const galleryPrevBtn = document.querySelector(".gallery-prev");
const galleryNextBtn = document.querySelector(".gallery-next");
const galleryCards = document.querySelectorAll(".cv");

let galleryTrackPos = -145;
let currentGalleryIdx = 2;

galleryPrevBtn.addEventListener("click", () => {
    
    if (currentGalleryIdx > 0) {

        currentGalleryIdx -= 1;
        galleryTrackPos += 270;

        galleryTrack.style.transform = `translateX(${galleryTrackPos}px)`;
    }

});

galleryNextBtn.addEventListener("click", () => {

    if (currentGalleryIdx < 4) {

        currentGalleryIdx += 1;
        galleryTrackPos -= 270;

        galleryTrack.style.transform = `translateX(${galleryTrackPos}px)`;
    }

});

galleryCards.forEach((card, index) => {
    
    card.addEventListener("click", () => {

        currentGalleryIdx = index;

        galleryTrackPos = -145 - (index - 2) * 270;

        galleryTrack.style.transform = `translateX(${galleryTrackPos}px)`;


    });

});