import React from 'react';
import ProductSkeleton from "../../skeleton/productSkeleton.jsx";
import productStore from "../../store/productStore.js";

const Products = () => {
    const {ProductListByRemark} = productStore()
    if (!ProductListByRemark || ProductListByRemark.length === 0) {
        return <ProductSkeleton/>
    }
    else {
        return (
            <div>
                Hello Product data is here
            </div>
        );
    }
};

export default Products;