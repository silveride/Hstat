/**
 * Created by mmathew on 7/25/2017.
 */

/* Checks the login credential of the user. *
/  The idea is to create an md5 and send to the auth server
*/


function validate_user(username, password) {

    return true;
}

var userInput = document.getElementsByName('username');
var passInput =   document.getElementsByName('password');
var btn = document.querySelector('button');
btn.onclick = function() {
    var username = userInput.value;
    var password = passInput.value;
    var statusCode = ""

    if (validate_user(username,password)) {
        statusCode = "login succeded"

        /* Next page */
        window.location.href = "dashboard.html";
    }

    btn.textContent = "Login Failed. Retry ?"
}
