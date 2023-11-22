
document.getElementById('reset-btn').addEventListener('click', () => { // reset button
    document.getElementById('second-part').innerHTML = ''
})


const form = document.getElementById('main-form') //
form.addEventListener('submit', (e) => {
    if(document.getElementById('page').checked) {
        e.preventDefault()

        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/hello', true);
        xhr.onload = function () {
        if (xhr.status === 200) {
          document.getElementById('second-part').innerHTML = xhr.responseText;
        }
            };
        xhr.send(formData);

    }
})