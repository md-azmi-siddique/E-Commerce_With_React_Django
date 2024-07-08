import React from 'react';
import productStore from "../../store/productStore.js";
import CategorySkeleton from "../../skeleton/categorySkeleton.jsx";

const Categories = () => {
    const {CategoryList} = productStore()
    if (CategoryList === null) {
        return <CategorySkeleton/>
    }
    else {
        return (
            <div>
                Hello data is here
            </div>
        );
    }
};

export default Categories;