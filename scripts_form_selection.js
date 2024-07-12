function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.querySelector('.upload-preview');
            preview.style.backgroundImage = `url(${e.target.result})`;
            document.querySelector('.main-container').classList.add('uploaded');
        };
        reader.readAsDataURL(file);
    }
}
