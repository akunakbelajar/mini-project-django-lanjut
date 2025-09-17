function togglePassword() {
    const passwordField = document.getElementById("password");
    const toggleBtn = document.getElementById("toggleBtn");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        toggleBtn.textContent = "🙈";
    } else {
        passwordField.type = "password";
        toggleBtn.textContent = "👁️";
    }
}

document.getElementById('year-2').textContent = new Date().getFullYear();

function checkoutAlert(productName) {
    alert("Pesanan anda telah di checkout, tunggu pesanannya.\nBarang: " + productName);
    return true; // biar form tetap submit ke server
  }

