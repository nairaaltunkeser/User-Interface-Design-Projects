document.addEventListener('DOMContentLoaded', function() {
    const draggables = document.querySelectorAll('.draggable');
    const dropBoxes = document.querySelectorAll('.drop-box');
    const submitBtn = document.getElementById('submitBtn');

    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart', function(event) {
            event.dataTransfer.setData("text", event.target.id);
        });
    });

    dropBoxes.forEach(box => {
        box.addEventListener('dragover', function(event) {
            event.preventDefault();
        });

        box.addEventListener('drop', function(event) {
            event.preventDefault();
            const draggableId = event.dataTransfer.getData("text");
            const draggable = document.getElementById(draggableId);
            if (!this.firstChild) {
                this.appendChild(draggable);
            }
        });
    });

    window.clearDropZone = function(button) {
        const dropBox = button.previousElementSibling;
        if (dropBox.firstChild) {
            const draggable = dropBox.firstChild;
            document.getElementById('drag-container').appendChild(draggable);
            dropBox.innerHTML = '';
        }
    }

    submitBtn.addEventListener('click', function() {
        dropBoxes.forEach(box => {
            const boxShutterSpeed = box.parentNode.dataset.shutter;
            const draggable = box.firstChild;
            const feedback = box.parentNode.querySelector('.feedback');

            if (draggable && draggable.dataset.shutter === boxShutterSpeed) {
                feedback.textContent = 'Correct!';
                feedback.style.color = 'green';
            } else {
                feedback.textContent = 'Incorrect :(';
                feedback.style.color = 'red';
            }
        });
    });
});
