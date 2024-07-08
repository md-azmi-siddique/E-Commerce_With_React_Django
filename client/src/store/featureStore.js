import create from 'zustand';
import axios from 'axios';

const FeatureStore = create((set)=>({
    FeatureList: null,
    FeatureListRequest:async ()=>{
        let res = await axios.get(`/api/feature`)
        if(res.status === 200){
            set({FeatureList: res.data})
        }
    }
}))

export default FeatureStore;