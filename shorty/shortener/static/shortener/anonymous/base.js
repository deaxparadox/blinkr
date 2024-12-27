console.log("Anonymous Session :)");


// let URL = "";

const requestURL = "http://localhost:8000/api/create/"

let displayPanelStatus = false;

const copyHashUrlToClipboard = async () => {

    document.querySelector(".lew-hash-copy").addEventListener("click", (event) => {


        
        // Process event only if displayPanelStatus is active (true);
        if (displayPanelStatus) {
            // Copy from
            let lewHashAnchor = document.querySelector(".lew-hash");

            // console.log(lewHashAnchor.getAttribute("href"))

            // Copy to Clipboard
            navigator.clipboard.writeText(lewHashAnchor.getAttribute("href")).then(function () {
                // console.log("Copied successfully");

                // Added to message about successful copy.
            }, function (err) {
                alert("Could not copy to Clipboard");
            })


        }
    })

}


const resetDisplayUrlHashPanel = () => {
    document.querySelector(".lew-url-reset-btn").addEventListener("click", async () => {

        if (displayPanelStatus) {
            // reset lew-hash
            let lewHashAnchor = document.querySelector(".lew-hash")
            lewHashAnchor.innerText = "";
            lewHashAnchor.removeAttribute("href")
            lewHashAnchor.removeAttribute("target")

            // reset lew-hash-url-wrapper panel
            let hashPanel = document.querySelector(".lew-hash-url-wrapper")
            hashPanel.style.height = "0px";
            hashPanel.style.padding = "0px";

            //  reset full_url input.
            const curValue = document.querySelector(".lew-url-input");
            curValue.value = ""

            displayPanelStatus = !displayPanelStatus;
        }

    })

}



// display url_hash
const activateDisplayUrlHashPanel = async (url_hash) => {

    // active .lew-hash anchor tag.
    let lewHashAnchor = document.querySelector(".lew-hash")
    lewHashAnchor.innerText = url_hash;
    lewHashAnchor.setAttribute("href", url_hash)
    lewHashAnchor.setAttribute("target", "_blank")

    // Activate display the panel.
    let hashPanel = document.querySelector(".lew-hash-url-wrapper")
    hashPanel.style.height = "50px";
    hashPanel.style.padding = "3px";

}


// Make a fetch request, for hashing the URL.
const makeHashRequest = async (full_url) => {

    // create request
    const request = new Request(requestURL, {
        "method": "POST",
    })

    // create body
    const body = new FormData();
    body.append("full_url", full_url)

    await fetch(request, {
        body: body,
    })
        .then(async e => {
            let json_data = await e.json();

            // Activate hash url panel.
            await activateDisplayUrlHashPanel(json_data.hash);
        })
        .catch(async e => {
            alert(e)
        })
        .finally(async e => {
            console.log("Let's verify.")
        })
}

// Extract the full_url, and make fetch request.
const getUrl = async () => {

    document.querySelector(".lew-url-btn").addEventListener("click", async e => {
        e.preventDefault();

        // Request for hash only when display hash panel
        // status is inactive (false).
        if (!displayPanelStatus) {

            // Get URL to hash, from .lew-url-input.
            const curValue = document.querySelector(".lew-url-input").value;

            if (curValue) {
                // fetch process the response
                // const encoded = encodeURIComponent(curValue);
                // console.log(encoded);
                // await makeHashRequest(encoded);

                // Request for hash
                await makeHashRequest(curValue)

                // 
                displayPanelStatus = !displayPanelStatus;

            } else {
                alert("Invalid URL string.")
            }

        }
    })


}

getUrl();
resetDisplayUrlHashPanel();
copyHashUrlToClipboard();