function logout() {
    document.getElementById('signOutBtn').click();
}

function validate() {
    let login = document.getElementById('id_login').value;
    let password = document.getElementById('id_password').value;

    if (login.trim() === "") {
        alert("Email must be filled out");
        return false;
    }
    if (password.trim() === "") {
        alert("Password must be filled out");
        return false;
    }

    return true;
}