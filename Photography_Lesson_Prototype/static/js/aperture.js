document.addEventListener('DOMContentLoaded', function() {
    const apertureValues = [
        "aperture_f16.png",
        "aperture_f11.png",
        "aperture_f8.png",
        "aperture_f5.png",
        "aperture_f4.png",
        "aperture_f2.png"
    ];

    const apertureSlider = document.getElementById('apertureRange');
    const apertureImage = document.getElementById('apertureImage');
    const submitBtn = document.getElementById('submitBtn');
    const resultDisplay = document.getElementById('result');

    apertureSlider.oninput = function() {
        apertureImage.src = `${window.location.origin}/static/images/${apertureValues[this.value]}`;
        console.log("Slider value: " + this.value);
        console.log("Image source set to: " + apertureImage.src);
    };

    submitBtn.addEventListener('click', function() {
        const selectedImageSrc = apertureImage.src.split('/').pop();
        const randomImageSrc = document.getElementById('randomImage').src.split('/').pop();

        if (selectedImageSrc === randomImageSrc) {
            resultDisplay.textContent = 'Correct!';
            resultDisplay.style.color = 'green'; 
        } else {
            resultDisplay.textContent = 'Incorrect :(';
            resultDisplay.style.color = 'red';

        }
    });
});
