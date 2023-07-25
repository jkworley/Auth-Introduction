import React from "react";
import ReactDOM from "react-dom/client";

import App from './components/App'

function Router() {

    return (
        <App />
    )
}

const root = ReactDOM.createRoot(document.querySelector('#root'))
root.render(<Router />)
