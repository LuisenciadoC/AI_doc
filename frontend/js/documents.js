// documents.js

const table =
    document.getElementById("documentsTable");

//--------------------CARGAR DOCUMENTOS--------------------//
async function loadDocuments(){

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/doc/view"
        );

        const data = await response.json();

        table.innerHTML = "";

        if(data.success){

            data.data.forEach(doc => {

                table.innerHTML += `
                    <tr>

                        <td>${doc.id_documento}</td>

                        <td>${doc.codigo_documento}</td>

                        <td>${doc.titulo}</td>

                        <td>${doc.descripcion}</td>

                        <td>

                            <button onclick="editDocument(${doc.id_documento})">
                                Editar
                            </button>

                            <button onclick="deleteDocument(${doc.id_documento})">
                                Eliminar
                            </button>

                            <button onclick="restoreDocument(${doc.id_documento})">
                                Restaurar
                            </button>

                        </td>

                    </tr>
                `;

            });

        }

    }catch(error){

        console.log(error);

    }

}

//--------------------BUSCAR DOCUMENTO--------------------//
async function searchDocument(){

    const search =
        document.getElementById("searchInput").value;

    if(search === ""){
        loadDocuments();
        return;
    }

    try{

        const response = await fetch(
            `http://127.0.0.1:5000/doc/view/${search}`
        );

        const data = await response.json();

        table.innerHTML = "";

        if(data.success){

            const doc = data.data;

            table.innerHTML += `
                <tr>

                    <td>${doc.id_documento}</td>

                    <td>${doc.codigo_documento}</td>

                    <td>${doc.titulo}</td>

                    <td>${doc.descripcion}</td>

                    <td>

                        <button onclick="editDocument(${doc.id_documento})">
                            Editar
                        </button>

                        <button onclick="deleteDocument(${doc.id_documento})">
                            Eliminar
                        </button>

                    </td>

                </tr>
            `;

        }else{

            alert(data.message);

        }

    }catch(error){

        console.log(error);

    }

}

//--------------------ELIMINAR--------------------//
async function deleteDocument(id){

    const confirmDelete =
        confirm("¿Eliminar documento?");

    if(!confirmDelete){
        return;
    }

    try{

        const response = await fetch(
            `http://127.0.0.1:5000/doc/view/${id}`,
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        alert(data.message);

        loadDocuments();

    }catch(error){

        console.log(error);

    }

}

//--------------------RESTAURAR--------------------//
async function restoreDocument(id){

    try{

        const response = await fetch(
            `http://127.0.0.1:5000/doc/view/${id}/restore`,
            {
                method: "PUT"
            }
        );

        const data = await response.json();

        alert(data.message);

        loadDocuments();

    }catch(error){

        console.log(error);

    }

}

//--------------------EDITAR--------------------//
function editDocument(id){

    localStorage.setItem(
        "edit_document_id",
        id
    );

    window.location.href =
        "edit_document.html";

}

//--------------------INICIO--------------------//
loadDocuments();