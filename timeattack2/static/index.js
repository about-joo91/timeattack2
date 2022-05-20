const file = document.getElementById('file')
const file_name = document.getElementById('file_name')
var formData = new FormData

const upload_btn = document.getElementById('upload_btn')

upload_btn.addEventListener('click', function () {
    const selectedFile = file.files[0];
    var name_of_file = file_name.value
    formData.append(name_of_file, selectedFile)
    $.ajax({
        type: "POST",
        url: "/posts",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        },

    })
})


