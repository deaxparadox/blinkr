const names = [
    "Nitish",
    "Paradox",
    "Alien-X"
]

let suggested = false


// Added event listener to suggested list item,
// click on the items to added them automatically
// in the input field.
const inputSuggestionToForm = () => {
    let username = document.querySelector("#register-username-suggestion-box");
    username.childNodes.forEach(e => {
        e.addEventListener("click", (e) => {
            document.querySelector("#register-username").value = e.target.innerText;
        })
    })
}

// Suggest some good username to the user.
const suggestUsername = () => {
    if (!suggested) {
        let username = document.querySelector("#register-username-suggestion-box");
        for (let n of names) {
            let listitem = document.createElement("li");
            listitem.innerText = n;
            username.appendChild(listitem);
        }
        suggested = true;

        // Input to username event,
        // for register username.
        inputSuggestionToForm();
    }
}

// Trigger function for username input suggestion.
const triggerOnFocus = () => {
    let username = document.querySelector("#register-username");

    username.addEventListener("focusin", () => {
        suggestUsername();
    })

    
    // username.addEventListener("input", (e) => {
    //     console.log(e.target.value);
    // })
}

triggerOnFocus();