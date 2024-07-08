// import React from 'react';
import SliderSkeleton from "../../skeleton/sliderSkeleton.jsx";
import productStore from "../../store/productStore.js";

const Slider = () => {
    const { SliderList } = productStore();

    // Conditionally render based on SliderList length
    if (!SliderList || SliderList.length=== 0) {
        return <SliderSkeleton />;

    } else {
        return (
            <div>
                Hello Product data is here
            </div>
        );

    }
};

export default Slider;

