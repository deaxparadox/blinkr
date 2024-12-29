/*
MESSAGE
*/ 


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

const renderListItem = async (message) => {
    document.querySelector(".lew-message-list").appendChild(await createElements(message));
}


/*
COPY
*/


const copyToClipboard = async (message, error) => {

    // Copy to Clipboard
    navigator.clipboard.writeText(message).then(function () {
        // Added to message about successful copy.

        // Implement functionality for unsuccessfull copy.
    }, function (err) {
        alert("Could not copy to Clipboard");
    })
}


const copyHashUrl = async () => {
    const elements = document.querySelectorAll(".lew-copy-btn");
    elements.forEach(async (e) => {
        e.addEventListener("click", async () => {
            const tr = e.parentElement.parentElement;
            // console.log(tr); 
            if (tr.hasChildNodes()) {
                const urlHash = tr.children[2].firstChild.getAttribute('href');
                // console.log();
                copyToClipboard(urlHash);
                await renderListItem("Copied!");
            }
        })
    })
    // const hashUrl = document.querySelector(".lew-short-url").innerText;
        // copyToClipboard(hashUrl, null);
        // await renderListItem("Copied!");
    
}

copyHashUrl();