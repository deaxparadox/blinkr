// const readyLoad = () => {
//     loadingHandler({active: true});
//     setTimeout(() => {
//         loadingHandler({active: false});
//     }, 2000)
// }

const Loading = () => {
    return (
        <div className="lew-loading-container-outer">
            <div className="lew-loading-container">
                <div className="lew-loading-inner">
                    <div className="lew-loading-wrapper">
                        <div className="lew-loading">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}


const loadingHandler = ({ active }) => {
    if (active) {
        document.querySelector(".lew-loading-container-outer").style.display = "block";
    } else {
        document.querySelector(".lew-loading-container-outer    ").style.display = "none";
    }

}