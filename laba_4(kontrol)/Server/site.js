const url = 'http://127.0.0.1:8000/cyberspryt'

function getAllList() {
	obj = new XMLHttpRequest()
	obj.open('GET', url, true)
	obj.responseType = 'json'
	obj.setRequestHeader('Content-Type', 'application/json')

	obj.onload = function() {
		if (obj.status >=400) {
			console.log(obj.response)
		} else {
			element = document.getElementById("list")
			data = obj.response
			text = ''
			for (let key of data.keys())
				text += data[key]['id']+'<br>'+data[key]['name']+'<br>'+data[key]['discipline']+'<br><br>'
			element.innerHTML = text
		}
	}
	obj.send()
}

function getOne() {
	element = document.getElementById('get_id').value
	obj = new XMLHttpRequest()
	obj.open('GET', url+'?id='+element, true)
	obj.responseType = 'json'
	obj.setRequestHeader('Content-Type', 'application/json')
	obj.onload = function() {
		if (obj.status >= 400) {
			console.log(obj.response)
		} else {
			console.log(obj.response)
			element = document.getElementById("blacklist")
			data = obj.response
			text = data['id']+'<br>'+data['name']+'<br>'+data['discipline']
			element.innerHTML=text
		}
	}
	obj.send()
}

function createOne() {
	name = document.getElementById('name').value
	discipline = document.getElementById('Discipline').value

	body = {
		discipline: discipline,
		name: name
	}

	obj = new XMLHttpRequest()
	obj.open('PUT', url, true)
	obj.responseType = 'json'
	obj.setRequestHeader('Content-Type', 'application/json')
	obj.onload = function() {
		if (obj.status >= 400) {
			console.log(obj.response)
		} else {
			console.log(obj.response)
		}
	}
	obj.send(JSON.stringify(body))
}

function updateOne() {
	name = document.getElementById('upName').value
	discipline = document.getElementById('upDiscipline').value
	id = document.getElementById('update_id').value
	body = {
		discipline:discipline,
		name: name,
		id: id
	}
	obj = new XMLHttpRequest()
	obj.open('POST', url, true)
	obj.responseType = 'json'
	obj.setRequestHeader('Content-Type', 'application/json')
	obj.onload = function() {
		if (obj.status >= 400) {
			console.log(obj.response)
		} else {
			console.log(obj.response)
		}
	}
	obj.send(JSON.stringify(body))
}

function deleteOne() {
	id = document.getElementById("delete_id").value

	body = {id: id}

	obj = new XMLHttpRequest()
	obj.open('DELETE', url, true)
	obj.responseType = 'json'
	obj.setRequestHeader('Content-Type', 'application/json')
	obj.onload = function() {
		if (obj.status >= 400) {
			console.log(obj.response)
		} else {
			console.log(obj.response)
		}
	}
	obj.send(JSON.stringify(body))
}