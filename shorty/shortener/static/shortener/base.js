console.log("Welcome to Localhost.")

const encodeURL = () => {
    const inputURL = document.querySelector("#input-url");
    console.log(inputURL.value)
}

const encodeButton = () => {
    const inputButton = document.querySelector("#input-button");
    inputButton.addEventListener("click", () => {
        encodeURL();
    })
}

// const showLastHash = async () => {
//     const myParams = new URLSearchParams(window.location.search);
//     const last = myParams.get("last");
//     const short_active = myParams.get("short_active");
//     if (last !== null && short_active !== null) {
//         document.querySelector(".")
//     }
// }

const copyShortURL = () => {
    const myParams = new URLSearchParams(window.location.search);
    const last = myParams.get("last");
    const shortActive = myParams.get("short_active");

    if (last === "yes" && shortActive === "yes") {
        const short_url = document.querySelector(".ewl-short-url").innerText;
        return short_url
    }
}

const copyShortURLHandler = () => {
    document.querySelector(".ewl-short-btn").addEventListener("click", (event) => {
        const shortURL = copyShortURL();
        navigator.clipboard.writeText(shortURL).then(function(){
            console.log("Copied successfully");
        }, function(err) {
            alert("Could not copy to Clipboard");
        })
        console.log(shortURL);
    })
}

copyShortURLHandler();

encodeButton();