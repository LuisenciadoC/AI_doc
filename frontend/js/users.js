// users.js

async function createUser(){

    const nombre =
        document.getElementById("nombre").value;

    const correo =
        document.getElementById("correo").value;

    const password =
        document.getElementById("password").value;

    const id_rol =
        document.getElementById("id_rol").value;

    if(
        nombre === "" ||
        correo === "" ||
        password === "" ||
        id_rol === ""
    ){

        alert("Todos los campos son obligatorios");

        return;

    }

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/user/create",
            {
                method: "POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body: JSON.stringify({

                    nombre: nombre,

                    correo: correo,

                    password: password,

                    id_rol: id_rol

                })
            }
        );

        const data = await response.json();

        alert(data.message);

    }catch(error){

        console.log(error);

    }

}