// import React from 'react';
import productStore from "../store/productStore.js";
import {useParams} from "react-router-dom";
import {useEffect} from "react";
import MasterLayout from "../components/layout/MasterLayout.jsx";
import ProductList from "../components/product/productList.jsx";

const ProductByBrand = () => {
    const {ListByCategoryRequest}  = productStore()
    const {category_ID } = useParams();

    useEffect(() => {
        (async ()=>{
            await ListByCategoryRequest(category_ID);
        })()
    }, []);

    return (
        <MasterLayout>
            <ProductList/>
        </MasterLayout>
    );
};

export default ProductByBrand;