import {useEffect} from 'react';
import MasterLayout from "../components/layout/MasterLayout.jsx";
import productStore from "../store/productStore.js";
import Brands from "../components/product/brands.jsx";
import Categories from "../components/product/categories.jsx";
import Slider from "../components/product/slider.jsx";
import Products from "../components/product/products.jsx";

const HomePage = () => {

    const {BrandListRequest, CategoryListRequest, SliderListRequest, ProductListByRemarkRequest} = productStore()
    useEffect(() => {
        (async ()=>{
            await BrandListRequest();
            await SliderListRequest()
            await CategoryListRequest()
            await ProductListByRemarkRequest(1)
        })()
    }, []);
    return (
        <MasterLayout>
            <Slider/>
            <Brands/>
            <Categories/>
            <Products/>

        </MasterLayout>
    );
};

export default HomePage;