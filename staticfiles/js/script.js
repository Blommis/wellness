const toggleBtn = document.getElementById("hamburger-toggle");
const menu = document.getElementById("mobile-menu");
const searchToggle = document.getElementById("mobile-search-toggle");
const searchForm = document.getElementById("mobile-search-form");

// Add a click event to toggle menu visibility
if (toggleBtn && menu) {
    toggleBtn.addEventListener("click", () => {
        menu.style.display = menu.style.display === "flex" ? "none" : "flex";
    });
}
    
// If both the mobile search icon and the search form exist

if (searchToggle && searchForm) {
    searchToggle.addEventListener("click", () => {
        const isHidden = searchForm.style.display === "none" || searchForm.style.display === "";
        searchForm.style.display = isHidden ? "block" : "none";
        if (isHidden) {
            searchForm.querySelector("input").focus();
        }
    });
}

// event carousel function 

document.addEventListener("DOMContentLoaded", function () {
const track = document.querySelector(".carousel-track");
const slides = document.querySelectorAll(".event-slide");
const btnLeft = document.querySelector(".carousel-btn.left");
const btnRight = document.querySelector(".carousel-btn.right");
});
