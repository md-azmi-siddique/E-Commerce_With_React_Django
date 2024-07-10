// import React from 'react';
import productStore from "../store/productStore.js";
import {useParams} from "react-router-dom";
import {useEffect} from "react";
import MasterLayout from "../components/layout/MasterLayout.jsx";
import ProductList from "../components/product/productList.jsx";

const ProductByBrand = () => {
    const {ListByBrandRequest}  = productStore()
    const {brand_ID } = useParams();

    useEffect(() => {
        (async ()=>{
            await ListByBrandRequest(brand_ID);
        })()
    }, []);

    return (
        <MasterLayout>
            <ProductList/>
        </MasterLayout>
    );
};

export default ProductByBrand;