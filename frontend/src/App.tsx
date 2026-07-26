import GenerateForm from "./components/GenerateForm";

function App() {
    return (
        <div
            style={{
                minHeight: "100vh",
                background: "#f4f6f9",
                padding: "50px 20px",
            }}
        >
            <div
                style={{
                    maxWidth: "900px",
                    margin: "0 auto",
                }}
            >
                <h1
                    style={{
                        fontSize: "2.5rem",
                        marginBottom: "10px",
                    }}
                >
                    Mini Content Engine
                </h1>

                <p
                    style={{
                        color: "#666",
                        marginBottom: "40px",
                    }}
                >
                    Generate AI-powered marketing images from your product details.
                </p>

                <GenerateForm />
            </div>
        </div>
    );
}

export default App;