/* jshint esversion: 6 */
/* global Stripe */

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

  if (track && btnLeft && btnRight && slides.length > 0){
    let currentIndex = 0;
    
    const updateCarousel = function () {
     const offset = -currentIndex * 100;
     track.style.transform = `translateX(${offset}%)`;
   };

   btnLeft.addEventListener("click", function () {
     currentIndex = (currentIndex - 1 + slides.length) % slides.length;
     updateCarousel();
   });

   btnRight.addEventListener("click", function () {
     currentIndex = (currentIndex + 1) % slides.length;
     updateCarousel();
   });

   updateCarousel();
  }

});



// Stripe checkout

document.addEventListener('DOMContentLoaded', function(){
  const publicKeyElement = document.getElementById('id_stripe_public_key');
  const clientSecretElement = document.getElementById('id_client_secret');

  if (publicKeyElement && clientSecretElement){
    const stripePublicKey = publicKeyElement.textContent.trim();
    const clientSecret = clientSecretElement.value.trim();
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

  const form = document.getElementById("payment-form");
  const submitButton = form.querySelector("button");

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      const overlay = document.getElementById("loading-overlay");
      if (overlay) overlay.classList.remove("d-none");
      
      card.update({ 'disabled': true });
      submitButton.disabled = true;

      const fullName = document.querySelector('input[name="full_name"]').value;
      const email = document.querySelector('input[name="email"]').value;
      const phone = document.querySelector('input[name="phone_number"]').value;
      const addressLine1 = document.querySelector('input[name="street_address1"]').value;
      const addressLine2 = document.querySelector('input[name="street_address2"]').value;
      const city = document.querySelector('input[name="town_or_city"]').value;
      const state = document.querySelector('input[name="county"]').value;
      const postalCode = document.querySelector('input[name="postcode"]').value;
      const country = document.querySelector('select[name="country"]').value;

      stripe.confirmCardPayment(clientSecret, {
        payment_method: {
          card: card,
          billing_details: {
            name: fullName,
            email: email,
            phone: phone,
            address: {
              line1: addressLine1,
              line2: addressLine2,
              city: city,
              state: state,
              postal_code: postalCode,
              country: country,
            }
          }
        },
        shipping: {
          name: fullName,
          phone: phone,
          address: {
            line1: addressLine1,
            line2: addressLine2,
            city: city,
            state: state,
            postal_code: postalCode,
            country: country,
          }
        }
    }).then(function (result) {
      if (result.error) {
        const errorDiv = document.getElementById("card-errors");
        errorDiv.innerHTML = `
          <span class="icon" role="alert">
            <i class="fas fa-times"></i>
          </span>
          <span>${result.error.message}</span>
        `;

        if (overlay) overlay.classList.add("d-none");
        card.update({ 'disabled': false });
        submitButton.disabled = false;
  
      } else {
          if (result.paymentIntent.status === "succeeded") {
            const overlay = document.getElementById("loading-overlay");
            if (overlay) overlay.classList.remove("d-none");
            setTimeout(function (){
              window.location.href = `/checkout/checkout_success/${result.paymentIntent.id}/`;
            }, 3000);
          }
      }
    });
  });
  }
});

// subscribe to newsletter message (this will not send actual email)

document.addEventListener('DOMContentLoaded', function (){
  const form = document.querySelector('.footer-form form');
  const emailInput = document.getElementById('email');
  const messageBox = document.getElementById('newsletter-message');

  form.addEventListener('submit', function (e){
    e.preventDefault();

    if (emailInput.value.trim() !== '') {
      messageBox.textContent = "You're now subscribed to our newsletter!";
      messageBox.style.color = "black";
      emailInput.value = '';
    } else{
      messageBox.textContent = "Please enter a valid email address.";
      messageBox.style.color = "red";
      }
  });
});
