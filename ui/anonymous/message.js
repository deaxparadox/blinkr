
const listAttributes = {
    classlist: 'toast align-items-center fade show message-toast text-bg-warning list-unstyled fw-bold shadow lew-message-list-item'.split(" "),
    attribute: {
        role: "alert",
        ariaLive: "assertive",
        ariaAtomic :"true"
    }
}
const listDivAttributes = {
    classlist: 'd-flex'.split(" "),
    attribute: {

    }
}
const listDivDivAttributes = {
    classlist: 'toast-body'.split(" "),
    attribute: {

    }
}
const listDivDivButtonAttributes = {
    classlist: "btn-close me-2 m-auto".split(" "),
    attribute: {
        type: "button",
        dataBsDismiss: "toast",
        ariaLabel: "Close"
    }
}


// Create element functions

const list = async () => {
    let listElement = document.createElement("li");
    listAttributes.classlist.forEach(async e => [
        listElement.classList.add(e)
    ]);
    listElement.setAttribute("role", listAttributes.attribute.role);
    listElement.setAttribute("aria-live", listAttributes.attribute.ariaLive);
    listElement.setAttribute("aria-atomic", listAttributes.attribute.ariaAtomic);
    return listElement
}

const listDiv = async () => {
    let divElement = document.createElement("div");
    listDivAttributes.classlist.forEach(async e => [
        divElement.classList.add(e)
    ]);
    return divElement
}


const listDivDiv = async () => {
    let divElement = document.createElement("div");
    listDivDivAttributes.classlist.forEach(async e => [
        divElement.classList.add(e)
    ]);
    return divElement
}

const listDivDivButton = async () => {
    let buttonElement = document.createElement("button");
    listDivDivButtonAttributes.classlist.forEach(async e => [
        buttonElement.classList.add(e)
    ]);
    
    buttonElement.setAttribute("type", listDivDivButtonAttributes.attribute.type);
    buttonElement.setAttribute("data-bs-dismiss", listDivDivButtonAttributes.attribute.dataBsDismiss);
    buttonElement.setAttribute("aria-label", listDivDivButtonAttributes.attribute.ariaLabel);
    return buttonElement
}

const createElements = async (message) => {
    const listitem4 = await listDivDivButton();
    const listitem3 = await listDivDiv();
    const listitem2 = await listDiv();
    const listitem1 = await list();
    
    listitem3.innerText = message;
    listitem2.appendChild(listitem3);
    listitem2.appendChild(listitem4)
    listitem1.appendChild(listitem2);
    // console.log(listitem1, listitem2)
    return listitem1
}

const renderListItem = async(message) => {
    document.querySelector(".lew-message-list").appendChild(await createElements(message));
}

// Dynamic message handler
const triggerMessage = async () => {
    document.querySelector(".lew-button").addEventListener("click", async (e) => {
        console.log("active")
        const messsage = "Test message";
        await renderListItem(messsage);
    })
}


// Message handler
const submitHandler = async () => {
    document.querySelector(".lew-url-btn").addEventListener("click", async (e) => {
        await renderListItem("Shortening the url...");
    })
}
const resetHandler = async () => {
    document.querySelector(".lew-url-reset-btn").addEventListener("click", async (e) => {
        await renderListItem("Form cleared");
    })
}
const copyHandler = async () => {
    document.querySelector(".lew-hash-copy").addEventListener("click", async (e) => {
        await renderListItem("Copied!");
    })
}


const sleep = async (delay) => {
    setTimeout(async () => {}, delay);
}

// Message disappearing handlers
const hideMessage = async() => {
    const hideMessageInterval = setInterval(async () => {
        const messageList = document.querySelector(".lew-message-list");
        // console.log(messageList.childNodes)
        if (messageList.hasChildNodes) {
            for (let element of messageList.children) {
                if (element.classList.contains("show")) {
                    element.classList.remove("show");
                    element.classList.add("hide");
                    console.log(element);

                    // 
                    break
                    // sleep(1000);
                    
                }
            }
        }
    }, 2500)
}


// Run
submitHandler();
copyHandler();
resetHandler();
hideMessage();