import React from 'react';
import ProductSkeleton from "../../skeleton/productSkeleton.jsx";
import productStore from "../../store/productStore.js";

const Products = () => {
    const {ProductListByRemark} = productStore()
    if (ProductListByRemark === null) {
        return <ProductSkeleton/>
    }
    else {
        return (
            <div>
                Hello data is here
            </div>
        );
    }
};

export default Products;