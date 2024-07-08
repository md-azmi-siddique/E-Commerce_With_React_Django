import React from 'react';
import MasterLayout from "../components/layout/MasterLayout.jsx";
import SliderSkeleton from "../skeleton/sliderSkeleton.jsx";
import FeatureSkeleton from "../skeleton/featureSkeleton.jsx";
import CategorySkeleton from "../skeleton/categorySkeleton.jsx";
import ProductSkeleton from "../skeleton/productSkeleton.jsx";
import BrandSkeleton from "../skeleton/brandSkeleton.jsx";

const HomePage = () => {
    return (
        <MasterLayout>
            <SliderSkeleton/>
            <FeatureSkeleton/>
            <CategorySkeleton/>
            <ProductSkeleton/>
            <BrandSkeleton/>
        </MasterLayout>
    );
};

export default HomePage;