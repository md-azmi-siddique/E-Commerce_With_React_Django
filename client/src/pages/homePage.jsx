import {useEffect} from 'react';
import MasterLayout from "../components/layout/MasterLayout.jsx";
import productStore from "../store/productStore.js";
import Brands from "../components/product/brands.jsx";
import Categories from "../components/product/categories.jsx";
import Slider from "../components/product/slider.jsx";
import Products from "../components/product/products.jsx";
import Features from "../components/features/features.jsx";
import featureStore from "../store/featureStore.js";


const HomePage = () => {

    const {BrandListRequest, CategoryListRequest, SliderListRequest, ListByRemarkRequest} = productStore()
    const {FeatureListRequest} = featureStore()
    useEffect(() => {
        (async ()=>{
            await BrandListRequest();
            await SliderListRequest()
            await CategoryListRequest()
            await ListByRemarkRequest(1)
        })()
    }, []);

    useEffect(() => {
        (async ()=>{
            await FeatureListRequest()
        })()
    }, []);
    return (
        <MasterLayout>
            <Slider/>
            <Brands/>
            <Categories/>
            <Products/>
            <Features/>

        </MasterLayout>
    );
};

export default HomePage;