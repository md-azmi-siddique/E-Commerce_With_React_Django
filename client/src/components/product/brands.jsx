import React from 'react';
import productStore from "../../store/productStore.js";
import BrandSkeleton from "../../skeleton/brandSkeleton.jsx";
import {Link} from "react-router-dom";

const Brands = () => {
    const {BrandList} = productStore()
    if (!BrandList || BrandList.length === 0) {
        return <BrandSkeleton/>
    }
    else {
        return (
            <div className="section">
                <div className="container">
                    <div className="row">
                        <h1 className="headline-4 text-center my-2 p-0">Top Brands</h1>
                        <span
                            className="bodySmal mb-5 text-center">Explore a World of Choices Across Our Most Popular <br
                        />Shopping Categories </span>
                        {
                            BrandList.map((item, index)=>{
                                return (
                                    <div key={index} className="col-2 col-lg-8r text-center col-md-8r p-2">
                                        <Link to={`/by-brand/$item["id"]`} className="card h-100 rounded-3 bg-white">
                                            <div className="card-body">
                                                <img className="w-30" src={item['brand_img']} alt="img"/>
                                                <p className="bodySmal mt-3">{item['brand_name']}</p>
                                            </div>
                                        </Link>
                                    </div>
                                )
                            })
                        }
                    </div>
                </div>
            </div>
        );
    }

};

export default Brands;