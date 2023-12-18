const username ="fatah"
const password = "123"

function auth(){
    let userInput = document.getElementById('username').value
    let paswordInput = document.getElementById('password').value
    let form = document.getElementById('form')

    if(userInput == username && paswordInput == password){
        alert("Login Berhasil!")
        form.submit()
    } else{
        alert("Login Gagal!")
    }
}