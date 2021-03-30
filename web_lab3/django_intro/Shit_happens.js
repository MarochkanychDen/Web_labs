const requestURL = 'http://127.0.0.1:8000/api/example'

function sendRes(method, url,) {
    var body = {
        input_value: document.getElementById('vvod').value
    }

    const xhr = new XMLHttpRequest()

    xhr.open(method, url)

    xhr.onload = function() {
        console.log(JSON.parse(xhr.response))
        document.getElementById('vivod').innerHTML = JSON.parse(xhr.response).output_value
    }

    xhr.send(JSON.stringify(body))
}
