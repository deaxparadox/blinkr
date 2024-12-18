const remove_invalid = async function(values) {
    const new_values = [];
    values.forEach(element => {
        if (element) {
            new_values.push(element)
        }
    });
}

const search = async() => {
    // const searchInput = document.querySelector("#search-input");
    // const searchButton = document.querySelector("#search-button");

    // searchButton.addEventListener("onmouseover", async () => {
    //     const values = searchInput.value.split(" ").filter(e => e!= " ").filter(e => e != '').join("+");
    //     let href = searchButton.getAttribute("href");
    //     href = `${href}?q=${values}`;
    //     searchButton.setAttribute("href", href);
        
    // })
}

search();