//--------------------ELEMENTOS--------------------//
const chatbox = document.getElementById("chatbox");

const userInput = document.getElementById("userInput");

const sendButton = document.getElementById("sendButton");

const welcomeMessage = document.querySelector(".welcome_message");


//--------------------OBTENER HORA--------------------//
function getCurrentTime(){

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: '2-digit',
        minute: '2-digit'
    });

}


//--------------------CREAR MENSAJE--------------------//
function createMessage(content, type){

    //Grupo
    const group = document.createElement("div");

    group.classList.add("message_group");

    //Mensaje
    const message = document.createElement("div");

    message.classList.add(type);

    message.innerText = content;

    //Hora
    const time = document.createElement("div");

    time.classList.add("message_time");

    time.innerText = getCurrentTime();

    //Agregar
    group.appendChild(message);

    group.appendChild(time);

    //Alinear usuario
    if(type === "message_user"){
        group.style.alignItems = "flex-end";
    }

    if(type === "message_ai"){

        const container = document.createElement("div");

        container.classList.add("ai_message_container");

        const avatar = document.createElement("div");

        avatar.classList.add("ai_avatar");

        avatar.innerText = "D";

        container.appendChild(avatar);

        container.appendChild(group);

        chatbox.appendChild(container);

    }
    else{

        chatbox.appendChild(group);

    }

}


//--------------------LOADING IA--------------------//
function createTypingLoader(){

    const typing = document.createElement("div");

    typing.classList.add("typing_container");

    typing.id = "typingLoader";

    typing.innerHTML = `
        <div class="typing_dot"></div>
        <div class="typing_dot"></div>
        <div class="typing_dot"></div>
    `;

    chatbox.appendChild(typing);

    chatbox.scrollTop = chatbox.scrollHeight;

}


//--------------------REMOVER LOADER--------------------//
function removeTypingLoader(){

    const loader = document.getElementById("typingLoader");

    if(loader){
        loader.remove();
    }

}


//--------------------ENVIAR MENSAJE--------------------//
async function sendMessage(){

    const message = userInput.value.trim();

    if(message === ""){
        return;
    }

    //--------------------OCULTAR WELCOME--------------------//
    if(welcomeMessage){
        welcomeMessage.style.display = "none";
    }

    //--------------------MENSAJE USER--------------------//
    createMessage(message, "message_user");

    //--------------------LIMPIAR INPUT--------------------//
    userInput.value = "";

    //--------------------SCROLL--------------------//
    chatbox.scrollTop = chatbox.scrollHeight;

    //--------------------MOSTRAR LOADER--------------------//
    createTypingLoader();

    try{

        //--------------------PETICION BACKEND--------------------//
        const response = await fetch("http://127.0.0.1:5000/ai/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: message
            })

        });

        //--------------------CONVERTIR JSON--------------------//
        const data = await response.json();

        //--------------------REMOVER LOADER--------------------//
        removeTypingLoader();

        //--------------------MOSTRAR RESPUESTA--------------------//
        if(data.success){

            createMessage(data.response, "message_ai");

        }else{

            createMessage(
                "No se encontraron documentos relacionados.",
                "message_ai"
            );

        }

        //--------------------SCROLL--------------------//
        chatbox.scrollTop = chatbox.scrollHeight;

        //--------------------GUARDAR HISTORIAL--------------------//
        saveHistory(message);

    }catch(error){

        removeTypingLoader();

        createMessage(
            "Error conectando con el servidor.",
            "message_ai"
        );

        console.error(error);

    }

}

//--------------------GUARDAR HISTORIAL--------------------//
function saveHistory(message){

    const historyContainer =
        document.querySelector(".history_container");

    const historyItem =
        document.createElement("div");

    historyItem.classList.add("history_item");

    historyItem.innerText = message;

    historyContainer.prepend(historyItem);

}


//--------------------BOTON--------------------//
sendButton.addEventListener("click", sendMessage);


//--------------------ENTER--------------------//
userInput.addEventListener("keypress", function(event){

    if(event.key === "Enter"){
        sendMessage();
    }

});