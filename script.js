// Gallery Lightbox Popup
document.addEventListener("DOMContentLoaded", function () {
  const images = document.querySelectorAll(".gallery-grid img, .achievement-gallery img");
  
  // Create modal
  const modal = document.createElement("div");
  modal.classList.add("popup-modal");
  modal.innerHTML = `
    <span class="close">&times;</span>
    <img class="popup-content" id="popupImage">
  `;
  document.body.appendChild(modal);

  const popupImg = modal.querySelector("#popupImage");
  const closeBtn = modal.querySelector(".close");

  images.forEach(img => {
    img.addEventListener("click", () => {
      popupImg.src = img.src;
      modal.style.display = "block";
    });
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  modal.addEventListener("click", (e) => {
    if (e.target === modal) modal.style.display = "none";
  });
});
