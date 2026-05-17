// login.js

const loginButton =
    document.getElementById("loginButton");

loginButton.addEventListener("click", login);

async function login(){

    const correo =
        document.getElementById("correo").value;

    const password =
        document.getElementById("password").value;

    if(correo === "" || password === ""){

        alert("Todos los campos son obligatorios");

        return;

    }

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/auth/login",
            {
                method: "POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body: JSON.stringify({
                    correo: correo,
                    password: password
                })
            }
        );

        const data = await response.json();

        if(data.success){

            localStorage.setItem(
                "usuario",
                JSON.stringify(data.data)
            );

            window.location.href =
                "dashboard.html";

        }else{

            alert(data.message);

        }

    }catch(error){

        console.log(error);

        alert("Error del servidor");

    }

}