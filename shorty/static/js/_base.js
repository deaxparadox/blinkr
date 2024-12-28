console.log("Welcome to Localhost.")


const fullHeightContent = () => {
    let contentBox = document.querySelector(".content-box");
    if (contentBox.clientHeight < window.innerHeight) {
        contentBox.style.height = `${window.innerHeight}px`;
    }
}

fullHeightContent();