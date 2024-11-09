document.addEventListener('DOMContentLoaded', function() {
    const apertureSlider = document.getElementById('apertureSlider');
    const resultDisplay = document.getElementById('result');
    const apertureImage = document.getElementById('apertureImage');
    const apertureValues = ["1", "2", "2_8", "4", "5", "8"];  // Suffix matches image file names

    function updateApertureImage(sliderIndex) {
        apertureImage.src = `/static/images/quiz3_${apertureValues[sliderIndex]}.png`;
    }

    apertureSlider.addEventListener('input', function() {
        updateApertureImage(this.value);
    });

    document.getElementById('submit').addEventListener('click', function() {
        if (apertureSlider.value === '0') {  // Assuming f/1.4 is the correct answer at index 0
            resultDisplay.textContent = 'Correct!';
            resultDisplay.style.color = 'green';
            localStorage.setItem('quiz_aperture', '1');

        } else {
            resultDisplay.textContent = 'Incorrect :(';
            resultDisplay.style.color = 'red';
            localStorage.setItem('quiz_aperture', '0');

        }
    });
});
