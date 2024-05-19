console.log("API Endpoints")


const copyButtons = async () => {
    document.querySelectorAll(".copy-button").forEach(async (e) => {
        e.addEventListener("click", () => {
            const endpoint = e.parentNode.parentNode.children[1].innerText;
            navigator.clipboard.writeText(endpoint).then(function(){
                console.log("Copied successfully");
            }, function(err) {
                alert("Could not copy to Clipboard");
            })
            console.log(endpoint);
        })
        
    })
}

copyButtons();