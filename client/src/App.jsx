import React from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import HomePage from "./pages/homePage.jsx";
import ProductByBrand from "./pages/productByBrand.jsx";
import ProductByCategory from "./pages/productByCategory.jsx";

const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/by-brand/:brand_ID" element={<ProductByBrand />} />
                <Route path="/by-category/:category_ID" element={<ProductByCategory />} />
            </Routes>

        </BrowserRouter>
    );
};

export default App;