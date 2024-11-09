document.addEventListener('DOMContentLoaded', function() {
    const isoValues = ["ISO100.png", "ISO200.png", "ISO400.png", "ISO800.png", "ISO1600.png"]; // Reordered array
    const slider = document.getElementById('isoRange');
    const dynamicImage = document.getElementById('dynamicImage');
    const submitBtn = document.getElementById('submitBtn');
    const result = document.getElementById('result');

    slider.oninput = function() {
        const selectedISO = isoValues[this.value];
        dynamicImage.src = `${window.location.origin}/static/images/${selectedISO}`;
        console.log("Slider value: " + this.value); // Debugging line
        console.log("Image source set to: " + dynamicImage.src); // Debugging line
    };

    submitBtn.addEventListener('click', function() {
        const dynamicSrc = dynamicImage.src.split('/').pop(); // Get only the filename
        const randomSrc = document.getElementById('randomImage').src.split('/').pop(); // Get only the filename

        if (dynamicSrc === randomSrc) {
            result.textContent = 'Correct!';
            result.style.color = 'green';  // Changed from resultDisplay to result

        } else {
            result.textContent = 'Incorrect :(';
            result.style.color = 'red';  // Changed from resultDisplay to result

        }
    });
});
