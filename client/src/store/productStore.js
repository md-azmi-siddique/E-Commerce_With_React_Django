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

    ListByRemark: null,
    ListByRemarkRequest:async (remark_ID)=>{
        set({ListByRemark: null})
        let res = await axios.get(`${baseURL}/products/remark/${remark_ID}`)
        if(res.status === 200){
            set({ListByRemark: res.data})
            // console.log(res.data)
        }
    },


    ListProduct: null,
    ListByBrandRequest:async (brand_ID)=>{
        set({ListProduct: null})
        let res = await axios.get(`${baseURL}/products/brands/${brand_ID}`)
        if(res.status === 200){
            set({ListProduct: res.data})
            // console.log(res.data)
        }
    },

    ListByCategoryRequest:async (category_ID)=>{
        set({ListProduct: null})
        let res = await axios.get(`${baseURL}/products/categories/${category_ID}`)
        if(res.status === 200){
            set({ListProduct: res.data})
            // console.log(res.data)
        }
    }




}))

export default productStore;