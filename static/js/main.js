const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 10);
});

const track = document.querySelector(".trusted-by-track");
const group = document.querySelector(".trusted-by-group");

if (track && group) {
    const updateAnimation = () => {
        const width = group.offsetWidth;

        track.style.setProperty("--scroll-width", `${width}px`);
    };

    updateAnimation();
    window.addEventListener("resize", updateAnimation);
}