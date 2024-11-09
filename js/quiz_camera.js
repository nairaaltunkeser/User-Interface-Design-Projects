document.addEventListener('DOMContentLoaded', function() {
    const draggables = document.querySelectorAll('.draggable');
    const dropZones = document.querySelectorAll('.drop-zone');
    const resultDisplay = document.getElementById('result');

    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart', function(event) {
            event.dataTransfer.setData("text/plain", event.target.id);
        });
    });

    dropZones.forEach(zone => {
        zone.addEventListener('dragover', function(event) {
            event.preventDefault(); // Necessary to allow drop
        });

        zone.addEventListener('drop', function(event) {
            event.preventDefault();
            const data = event.dataTransfer.getData("text/plain");
            const draggable = document.getElementById(data);
            if (!this.firstChild) { // Only allow one item per zone
                this.appendChild(draggable);
            }
        });
    });

    document.getElementById('submit').addEventListener('click', function() {
        let correct = 0;
        if (document.getElementById('shutterSpeedZone').contains(document.getElementById('shutterSpeed'))) correct++;
        if (document.getElementById('apertureZone').contains(document.getElementById('aperture'))) correct++;
        if (document.getElementById('isoZone').contains(document.getElementById('iso'))) correct++;

        if (correct === 3) {
            resultDisplay.textContent = 'Correct!';
            resultDisplay.style.color = 'green';
            localStorage.setItem('quiz_camera', '1');

        } else {
            resultDisplay.textContent = 'Incorrect :(';
            resultDisplay.style.color = 'red';
            localStorage.setItem('quiz_camera', '0');
        }
    });

    document.getElementById('reset').addEventListener('click', function() {
        draggables.forEach(draggable => {
            document.querySelector('.draggables').appendChild(draggable);
        });
        resultDisplay.textContent = '';
    });
});
