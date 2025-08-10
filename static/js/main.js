// script.js
function classifyImage() {
    const input = document.getElementById("imageInput");
    const file = input.files[0];
    const imageDisplay = document.getElementById("uploadedImage");
    const result = document.getElementById("classificationResult");

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            imageDisplay.style.display = "block";
            imageDisplay.src = e.target.result;
            
            // Simulasi klasifikasi
            setTimeout(function() {
                // Anda bisa mengganti dengan API klasifikasi gambar atau model AI Anda
                result.textContent = "Bunga ini adalah jenis: Rose";
            }, 2000); // Simulasi delay 2 detik
        };
        reader.readAsDataURL(file);
    } else {
        result.textContent = "Silakan unggah gambar terlebih dahulu.";
    }
}