document.addEventListener('DOMContentLoaded', function() {
    const shutterSlider = document.getElementById('shutterSlider');
    const resultDisplay = document.getElementById('result');
    const shutterImage = document.getElementById('shutterImage');
    const shutterValues = ["60", "125", "250", "500", "1000", "2000"];

    function updateShutterImage(sliderIndex) {
        shutterImage.src = `/static/images/quiz2_${shutterValues[sliderIndex]}.png`;
    }

    shutterSlider.addEventListener('input', function() {
        updateShutterImage(this.value);
    });

    document.getElementById('submit').addEventListener('click', function() {
        if (shutterSlider.value === '1') {  // Assuming 1/125 is the correct answer at index 1
            resultDisplay.textContent = 'Correct!';
            resultDisplay.style.color = 'green';
            localStorage.setItem('quiz_shutter', '1');

        } else {
            resultDisplay.textContent = 'Incorrect :(';
            resultDisplay.style.color = 'red';
            localStorage.setItem('quiz_shutter', '0');
        }
    });
});
