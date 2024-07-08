import React from 'react';
import productStore from "../../store/productStore.js";
import CategorySkeleton from "../../skeleton/categorySkeleton.jsx";

const Categories = () => {
    const {CategoryList} = productStore()
    if (!CategoryList || CategoryList.length === 0) {
        return <CategorySkeleton/>
    }
    else {
        return (
            <div>
                Hello Category data is here
            </div>
        );
    }
};

export default Categories;