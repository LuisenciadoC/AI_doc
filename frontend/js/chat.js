//Contenedor chat
const chatbox = document.getElementById("chatbox");

//Input usuario
const userInput = document.getElementById("userInput");

//Boton enviar
const sendButton = document.getElementById("sendButton");

//Mensaje bienvenida
const welcomeMessage = document.getElementById("welcomeMessage");

//Evento boton
sendButton.addEventListener("click", sendMessage);

//Evento enter
userInput.addEventListener("keypress", function(event){

    if(event.key === "Enter"){
        sendMessage();
    }

});

//Funcion enviar mensaje
function sendMessage(){

    //Guardar texto
    const message = userInput.value.trim();

    //Validar vacio
    if(message === ""){
        return;
    }

    //Ocultar bienvenida
    if(welcomeMessage){
        welcomeMessage.style.display = "none";
    }

    //Crear mensaje usuario
    const userMessage = document.createElement("div");

    userMessage.classList.add("message_user");

    userMessage.textContent = message;

    //Agregar mensaje
    chatbox.appendChild(userMessage);

    //Limpiar input
    userInput.value = "";

    //Scroll automatico
    chatbox.scrollTop = chatbox.scrollHeight;

    //Respuesta temporal IA
    setTimeout(() => {

        const aiMessage = document.createElement("div");

        aiMessage.classList.add("message_ai");

        aiMessage.textContent = "Docky está procesando tu consulta documental...";

        chatbox.appendChild(aiMessage);

        chatbox.scrollTop = chatbox.scrollHeight;

    }, 800);

}