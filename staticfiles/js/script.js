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

  let currentIndex = 0;

  function updateCarousel() {
    const offset = -currentIndex * 100;
    track.style.transform = `translateX(${offset}%)`;
  }
  btnLeft.addEventListener("click", function () {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateCarousel();
  });

  btnRight.addEventListener("click", function () {
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
  });


});



// Stripe checkout

document.addEventListener('DOMContentLoaded', function(){
  const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.trim();
  const clientSecret = document.getElementById('id_client_secret').textContent.trim();
  const stripe = Stripe(stripePublicKey);
  const elements = stripe.elements();

  const style = {
    base: {
      color: "#000",
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSize: "16px",
      "::placeholder": { color: "#aab7c4" }
    },
    invalid: {
      color: "#fa755a",
      iconColor: "#fa755a"
    }
  };
  const card = elements.create("card", { style: style });
  card.mount("#card-element");

   card.on("change", function (event) {
        const errorDiv = document.getElementById("card-errors");
        if (event.error) {
            errorDiv.textContent = event.error.message;
        } else {
            errorDiv.textContent = "";
        }
    });
});