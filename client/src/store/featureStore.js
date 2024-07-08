import create from 'zustand';
import axios from 'axios';

const baseURL = "http://127.0.0.1:8000/api";

const FeatureStore = create((set)=>({
    FeatureList: null,
    FeatureListRequest:async ()=>{
        let res = await axios.get(`${baseURL}/feature`)
        if(res.status === 200){
            set({FeatureList: res.data})
        }
    }
}))

export default FeatureStore;