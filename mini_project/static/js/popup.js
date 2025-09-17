function openPopup() {
  document.getElementById("popup").style.display = "flex";
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
}

function openProductPopup(id, name, desc, price, img) {
  document.getElementById("popup-title").innerText = name;
  document.getElementById("popup-desc").innerText = desc;
  document.getElementById("popup-price").innerText = "Rp " + price;
  document.getElementById("popup-img").src = img;

  // Update form checkout dengan product.id
  const form = document.getElementById("popup-form");
  if (form) {
    form.action = "/checkout/" + id + "/";
  }

  document.getElementById("product-popup").style.display = "flex";
}

function closeProductPopup() {
  document.getElementById("product-popup").style.display = "none";
}
