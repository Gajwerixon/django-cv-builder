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

const startPos = -415;
const gallerySlideWidth = 270;
const originalCardsCount = galleryCards.length;

let galleryTrackPos = startPos;
let currentGalleryIdx = 0;
let isGalleryAnimating = false;

const setActiveCard = (index) => {
    galleryCards.forEach(card => {
        card.classList.remove("active")
    });

    const activeCard = document.querySelector(
        `.cv[data-index="${index}"]`
    );

    activeCard.classList.add("active")
}

const finishGalleryMove = (direction) => {

    galleryTrack.style.transition = "none";

    if (direction === "next") {
        galleryTrack.append(galleryTrack.firstElementChild);
        galleryTrackPos += gallerySlideWidth;
    } else {
        galleryTrack.prepend(galleryTrack.lastElementChild);
        galleryTrackPos -= gallerySlideWidth;
    }

    galleryTrack.style.transform =
        `translateX(${galleryTrackPos}px)`;

    requestAnimationFrame(() => {
        galleryTrack.style.transition = "transform 0.4s ease";
        isGalleryAnimating = false;
    });
};


/* 
    Previous Button
*/

galleryPrevBtn.addEventListener("click", () => {

    if (isGalleryAnimating) return;

    isGalleryAnimating = true;

    currentGalleryIdx--;

    if (currentGalleryIdx < 0) {
        currentGalleryIdx = originalCardsCount - 1;
    }

    setActiveCard(currentGalleryIdx);

    galleryTrackPos += gallerySlideWidth;

    galleryTrack.style.transform =
        `translateX(${galleryTrackPos}px)`;


    galleryTrack.addEventListener("transitionend", () => {
        finishGalleryMove("prev");
    }, { once: true });

});


/* 
    Next Button
*/

galleryNextBtn.addEventListener("click", () => {

    if (isGalleryAnimating) return;

    isGalleryAnimating = true;

    currentGalleryIdx++;

    if (currentGalleryIdx >= originalCardsCount) {
        currentGalleryIdx = 0;
    }

    setActiveCard(currentGalleryIdx);

    galleryTrackPos -= gallerySlideWidth;

    galleryTrack.style.transform = `translateX(${galleryTrackPos}px)`;


    galleryTrack.addEventListener("transitionend", () => {
        finishGalleryMove("next");
    }, { once: true });
});