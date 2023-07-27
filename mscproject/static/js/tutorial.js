const images = {{ images_json|safe }};
const tutorialImage = document.getElementById('tutorialImage');
let currentImageIndex = 0;

function updateImage() {
  tutorialImage.src = "{% static 'images/' %}" + images[currentImageIndex];
}

document.getElementById('btn-next').addEventListener('click', () => {
  currentImageIndex = (currentImageIndex + 1) % images.length;
  updateImage();
});

document.getElementById('btn-back').addEventListener('click', () => {
  currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
  updateImage();
});

updateImage();