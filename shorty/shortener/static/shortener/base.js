console.log("Welcome to Localhost.")

const encodeURL = async () => {
    const inputURL = document.querySelector("#input-url");
    console.log(inputURL.value)
}

const encodeButton = async () => {
    const inputButton = document.querySelector("#input-button");
    inputButton.addEventListener("click", async () => {
        await encodeURL();
    })
}

encodeButton();