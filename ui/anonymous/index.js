console.log("Anonymous Session :)");


// let URL = "";

const requestURL = "http://localhost:8000/api/create/"


// Make a fetch request, for hashing the URL.
const makeHashRequest = async (new_url) => {
    
    // create request
    const request = new Request(requestURL,
        {
            "method": "POST",
            // headers: {
            //     "Content-Type": "application/json",
            // },
        }
    )

    // create body
    const body = new FormData();
    body.append("full_url", new_url)

    await fetch(request, {
        body: body,
    })
    .then(async e => {
        return await e.json();
    }, async (e) => { console.log(e)})
    .catch(async e => {
        return e
    })
    .finally(async e => {
        console.log("Let's verify.")
    })
}

// Extract the full_url, and make fetch request.
const getUrl = async () => {
    document.querySelector(".lew-url-btn").addEventListener("click", async e => {
        e.preventDefault();

        const curValue = document.querySelector(".lew-url-input").value;
        // console.log(curValue)

        console.log(await makeHashRequest(curValue));

    })
}

getUrl()