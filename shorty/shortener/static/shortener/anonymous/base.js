console.log("Anonymous Session :)");


let URL = "";

const requestURL = "http://localhost:8000/api/create/"


// Make a fetch request, for hashing the URL.
const makeHashRequest = async (new_url) => {
    
    const newBody = new FormData();
    newBody.append("full_url", new_url)

    return await fetch(requestURL, {
        method: "post",
        body: newBody
    })
}

// Extract the full_url, and make fetch request.
const getUrl = async () => {
    document.querySelector(".lew-url-btn").addEventListener("click", async e => {
        e.preventDefault();

        const curValue = document.querySelector(".lew-url-input").value;

        const f = await makeHashRequest(curValue);
        f.then(e => {
            console.log(e.json())
        }).catch(e => {
            console.log(e)
        }).finally(e => {
            console.log("Let's verify.")
        })
    })
}

getUrl()