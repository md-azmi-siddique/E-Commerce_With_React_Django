import create from 'zustand';
import axios from 'axios';

const productStore = create((set)=>({
    BrandList: null,
    BrandListRequest:async ()=>{
        let res = await axios.get(`/api/brands`)
        if(res.status === 200){
            set({BrandList: res.data})
        }
    },

    CategoryList: null,
    CategoryListRequest:async ()=>{
        let res = await axios.get(`/api/categories`)
        if(res.status === 200){
            set({CategoryList: res.data})
        }
    },

    SliderList: null,
    SliderListRequest:async ()=>{
        let res = await axios.get(`/api/products/slider`)
        if(res.status === 200){
            set({SliderList: res.data})
        }
    },

    ProductList: null,
    ProductListRequest:async ()=>{
        let res = await axios.get(`/api/products`)
        if(res.status === 200){
            set({ProductList: res.data})
        }
    }
}))

export default productStore;