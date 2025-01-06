
const app = document.getElementById("app")

const App = () => {


    return (

        <div>
            <Loading />
            <HashForm />
        </div>
    )
}

const root = ReactDOM.createRoot(app);
root.render(<App />);
