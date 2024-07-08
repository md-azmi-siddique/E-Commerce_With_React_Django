import React from 'react';
import SliderSkeleton from "../../skeleton/sliderSkeleton.jsx";
import productStore from "../../store/productStore.js";

const Slider = () => {
    const {SliderList} = productStore()
    if (SliderList === null) {
        return <SliderSkeleton/>
    }
    else {
        return (
            <div>
                Hello data is here
            </div>
        );
    }
};

export default Slider;