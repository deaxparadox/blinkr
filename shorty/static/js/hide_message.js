// Message disappearing handlers
const hideMessage = async() => {
    const hideMessageInterval = setInterval(async () => {
        const messageList = document.querySelector(".lew-message-list");
        // console.log(messageList.childNodes)
        if (messageList.hasChildNodes) {
            for (let element of messageList.children) {
                if (element.classList.contains("show")) {
                    element.classList.remove("show");
                    element.classList.add("hide");
                    // console.log(element);

                    // 
                    break
                    // sleep(1000);
                    
                }
            }
        }
    }, 2000)
}
hideMessage();