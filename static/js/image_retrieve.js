function openLightbox(element) {
    var modal = document.getElementById("lightbox-modal");
    var modalImg = document.getElementById("lightbox-img");
    modal.style.display = "block";
    modalImg.src = element.src;
}

function closeLightbox() {
    var modal = document.getElementById("lightbox-modal");
    modal.style.display = "none";
}
