document.addEventListener('DOMContentLoaded', function() {
    const isoSlider = document.getElementById('isoSlider');
    const resultDisplay = document.getElementById('result');
    const isoImage = document.getElementById('isoImage');
    const isoValues = ["100", "200", "400", "800", "1600"];

    function updateISOImage(sliderIndex) {
        isoImage.src = `/static/images/Quiz1_${isoValues[sliderIndex]}.png`;
    }

    isoSlider.addEventListener('input', function() {
        updateISOImage(this.value);
    });

    document.getElementById('submit').addEventListener('click', function() {
        if (isoSlider.value === '0') {
            resultDisplay.textContent = 'Correct!';
            resultDisplay.style.color = 'green';
            localStorage.setItem('quiz_iso', '1');
        } else {
            resultDisplay.textContent = 'Incorrect :(';
            resultDisplay.style.color = 'red';
            localStorage.setItem('quiz_iso', '0');

        }
    });
});

document.getElementById('isoRange').addEventListener('input', function() {
    // Get the slider value
    var sliderValue = this.value;

    // Set the value of the CSS variable '--slider-value' to the slider value
    this.style.setProperty('--slider-value', sliderValue * 25 + '%');
});
