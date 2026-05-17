// edit_document.js

const id_documento =
    localStorage.getItem(
        "edit_document_id"
    );

//--------------------CARGAR DATOS--------------------//
async function loadDocument(){

    try{

        const response = await fetch(
            `http://127.0.0.1:5000/doc/view/${id_documento}`
        );

        const data = await response.json();

        if(data.success){

            document.getElementById(
                "codigo_documento"
            ).value =
                data.data.codigo_documento;

            document.getElementById(
                "titulo"
            ).value =
                data.data.titulo;

            document.getElementById(
                "descripcion"
            ).value =
                data.data.descripcion;

        }

    }catch(error){

        console.log(error);

    }

}

//--------------------ACTUALIZAR--------------------//
async function updateDocument(){

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

    try{

        const response = await fetch(
            `http://127.0.0.1:5000/doc/view/${id_documento}/update`,
            {
                method: "PUT",

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

//--------------------INICIO--------------------//
loadDocument();