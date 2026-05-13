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


//--------------------RESPUESTA IA SIMULADA--------------------//
function fakeAIResponse(userMessage){

    const responses = [

        "Estoy revisando la documentación relacionada.",

        "Encontré información asociada al procedimiento solicitado.",

        "La política documental contiene datos relacionados con tu consulta.",

        "Docky encontró coincidencias dentro del sistema documental.",

        "Se identificaron documentos vinculados a tu búsqueda."
    ];

    const random =
        responses[Math.floor(Math.random() * responses.length)];

    return `${random}\n\nConsulta realizada: "${userMessage}"`;

}


//--------------------ENVIAR MENSAJE--------------------//
function sendMessage(){

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

    //--------------------RESPUESTA IA--------------------//
    setTimeout(() => {

        removeTypingLoader();

        const response = fakeAIResponse(message);

        createMessage(response, "message_ai");

        chatbox.scrollTop = chatbox.scrollHeight;

        //--------------------GUARDAR HISTORIAL--------------------//
        saveHistory(message);

    }, 1800);

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