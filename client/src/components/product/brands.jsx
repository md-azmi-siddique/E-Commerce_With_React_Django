import React from 'react';
import productStore from "../../store/productStore.js";
import BrandSkeleton from "../../skeleton/brandSkeleton.jsx";

const Brands = () => {
    const {BrandList} = productStore()
    if (BrandList === null) {
        return <BrandSkeleton/>
    }
    else {
        return (
            <div>
Hello Brand data is here
            </div>
        );
    }

};

export default Brands;