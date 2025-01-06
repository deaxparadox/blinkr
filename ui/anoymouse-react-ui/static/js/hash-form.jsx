

const submitForm = (url) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(`Submitted: ${url}`);
            // Stop loading
            loadingHandler({active: false});
        }, 2000)
    })
}

const HashForm = () => {
    const [url, setUrl] = React.useState("");
    const [status, setStatus] = React.useState("typing")
    const [loading, setLoading] = React.useState(false);


    const submitHandler = (e) => {
        e.stopPropagation();
        // Starting loading.
        loadingHandler({active: true});
        submitForm(url);
    }

    const onInputChange = (e) => {
        console.log(e.target.value);
        setUrl(e.target.value);
    }

    return (
        <div className="lew-container">
            {/* <Loading /> */}
            <div className="lew-inner">
                <div className="lew-form-box">
                    <form onSubmit={submitHandler} className="lew-url-form">
                        <div className="lew-url-input-box">
                            <label htmlFor="lew-url-input"></label>
                            <input disabled={status === "submitting"} value={url} onChange={onInputChange} type="text" name="lew-url-input" id="lew-url-input" placeholder="Enter your url..."/>
                        </div>
                        <div className="lew-url-btn-btn">
                            <button disabled={url.length === 0 || status === "submitting"} onClick={submitHandler} type="button">Submit</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}