const baseUrl = "/api/users/?"
const submit = document.getElementById("usernameButton")
const userData = document.getElementById("userData")

const getData = async (query) => {
	url = baseUrl + query
	res = await fetch(url)
	return res.json()
}

const processData = async (query) => {
	rawData = await getData(query)
	data = rawData[0]
	for (const [key, value] of Object.entries(data)) {
		console.log(`${key} - ${value}`)
		html = `<li>${key} - ${value}</li>`
		userData.insertAdjacentHTML("beforeend", html)
	}
	divide = `<hr>`
	userData.insertAdjacentHTML("beforeend", divide)
}

submit.addEventListener("click", function (e) {
	e.preventDefault()
	username = document.getElementById("username").value
	query = `username=${username}`
	processData(query)
})
