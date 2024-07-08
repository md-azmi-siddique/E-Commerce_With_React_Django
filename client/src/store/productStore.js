import create from 'zustand';
import axios from 'axios';
// const baseURL = "http://127.0.0.1:8000/api";
import baseURL from './baseURL';

const productStore = create((set)=>({
    BrandList: null,
    BrandListRequest:async ()=>{
        let res = await axios.get(`${baseURL}/brands`)
        if(res.status === 200){
            set({BrandList: res.data})
            // console.log(res.data)
        }
    },

    CategoryList: null,
    CategoryListRequest:async ()=>{
        let res = await axios.get(`${baseURL}/categories`)
        if(res.status === 200){
            set({CategoryList: res.data})
            // console.log(res.data)
        }
    },

    SliderList: null,
    SliderListRequest:async ()=>{
        let res = await axios.get(`${baseURL}/products/slider`)
        if(res.status === 200){
            set({SliderList: res.data})
        }
    },

    ProductListByRemark: null,
    ProductListByRemarkRequest:async (remark_ID)=>{
        let res = await axios.get(`${baseURL}/products/remark/${remark_ID}`)
        if(res.status === 200){
            set({ProductList: res.data})
            console.log(res.data)
        }
    }
}))

export default productStore;