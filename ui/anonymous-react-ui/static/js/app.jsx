
const app = document.getElementById("app")

const App = () => {


    return (

        <div className="">
            <div>
                <Loading />
            </div>
            <div className="lew-main-container">
                <Navbar />
                <HashForm />
                <Footer />
            </div>
        </div>
    )
}

const root = ReactDOM.createRoot(app);
root.render(<App />);
