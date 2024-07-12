document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.inspectorButton');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.accept = 'image/*';
            
            fileInput.onchange = function(event) {
                const file = event.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        const img = new Image();
                        img.src = e.target.result;
                        img.style.maxWidth = '100%';
                        img.style.maxHeight = '100%';

                        // You can customize this part to decide where to show the uploaded image
                        // const imgContainer = document.createElement('div');
                        // imgContainer.appendChild(img);
                        // document.body.appendChild(imgContainer); // Example: appending to body
                    };
                    reader.readAsDataURL(file);
                }
            };

            fileInput.click();
        });
    });
});
