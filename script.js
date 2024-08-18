document.getElementById('fileInput').addEventListener('change', function(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
        var img = document.createElement('img');
        img.src = e.target.result;
        document.getElementById('preview').innerHTML = '';
        document.getElementById('preview').appendChild(img);
    }
    reader.readAsDataURL(file);
});
