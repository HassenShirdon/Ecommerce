(function ($) {
  "use strict";

  // Dropdown on mouse hover
  $(document).ready(function () {
    function toggleNavbarMethod() {
      if ($(window).width() > 992) {
        $(".navbar .dropdown")
          .on("mouseover", function () {
            $(".dropdown-toggle", this).trigger("click");
          })
          .on("mouseout", function () {
            $(".dropdown-toggle", this).trigger("click").blur();
          });
      } else {
        $(".navbar .dropdown").off("mouseover").off("mouseout");
      }
    }
    toggleNavbarMethod();
    $(window).resize(toggleNavbarMethod);
  });
});
// Back to top button

function change_image(image) {
  var container = document.getElementById("main-image");

  container.src = image.src;
}

document.addEventListener("DOMContentLoaded", function (event) {});

document.addEventListener("DOMContentLoaded", function () {
  const addToCartButtons = document.querySelectorAll(".btn-add-to-cart");

  addToCartButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const itemId = this.getAttribute("data-item-id");
      addToCart(itemId);
    });
  });

  function addToCart(itemId) {
    fetch(`/add-to-cart/${itemId}/`)
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("Item added to cart successfully!");
        } else {
          alert("Failed to add item to cart.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const addToCartButtons = document.querySelectorAll(".btn-add-to-cart");
  const cartIcon = document.querySelector(".cart-icon"); // Assuming you have a cart icon element

  // Function to update the cart icon with the item count
  function updateCartIcon(count) {
    cartIcon.innerHTML = `<i class="fas fa-shopping-cart"></i> (${count})`;
  }

  // Initialize the cart count
  let cartCount = 0;

  addToCartButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const itemId = button.getAttribute("data-item-id");
      // Send a request to the server to add the item to the cart (you can use AJAX for this)

      // Assuming the item is successfully added to the cart
      cartCount++;
      updateCartIcon(cartCount);
    });
  });
});
