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

                // 업로드 완료된 부위 수 업데이트
                const completedPhotos = document.getElementById('completedPhotos');
                completedPhotos.textContent = parseInt(completedPhotos.textContent) + 1;
                
                // 업로드 완료된 부위 이름 업데이트
                const partLabel = document.getElementById(`status-${partId}`);
                partLabel.classList.add('completed');
            };
            reader.readAsDataURL(file);
        }
    };
    input.click();
}
