// create_document.js

async function createDocument(){

    const codigo_documento =
        document.getElementById(
            "codigo_documento"
        ).value;

    const titulo =
        document.getElementById(
            "titulo"
        ).value;

    const descripcion =
        document.getElementById(
            "descripcion"
        ).value;

    if(
        codigo_documento === "" ||
        titulo === "" ||
        descripcion === ""
    ){

        alert("Todos los campos son obligatorios");

        return;

    }

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/doc/create",
            {
                method: "POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body: JSON.stringify({

                    codigo_documento:
                        codigo_documento,

                    titulo:
                        titulo,

                    descripcion:
                        descripcion

                })
            }
        );

        const data = await response.json();

        alert(data.message);

        if(data.success){

            window.location.href =
                "documents.html";

        }

    }catch(error){

        console.log(error);

    }

}