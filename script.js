function showHomeScreen() {
    document.getElementById('homeScreen').style.display = 'block';
    document.getElementById('photoScreen').style.display = 'none';
    document.getElementById('checklistScreen').style.display = 'none';
}

function showPhotoScreen() {
    document.getElementById('homeScreen').style.display = 'none';
    document.getElementById('photoScreen').style.display = 'block';
    document.getElementById('checklistScreen').style.display = 'none';
}

function showChecklistScreen() {
    document.getElementById('homeScreen').style.display = 'none';
    document.getElementById('photoScreen').style.display = 'none';
    document.getElementById('checklistScreen').style.display = 'block';
}

function uploadPhoto(partId) {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const uploadPhoto = document.querySelector(`.cell-upload-photo[data-id="${partId}"]`);
                uploadPhoto.style.backgroundImage = `url(${e.target.result})`;
                uploadPhoto.style.border = 'none';
                uploadPhoto.innerHTML = '';
                // 완료된 사진 수 업데이트
                const completedPhotos = document.getElementById('completedPhotos');
                completedPhotos.textContent = parseInt(completedPhotos.textContent) + 1;
            };
            reader.readAsDataURL(file);
        }
    };
    input.click();
}
