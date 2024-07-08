import React from 'react';
import Lottie from "lottie-react";
import ImagePlaceHolder from "../assets/images/image.json";
import Skeleton from "react-loading-skeleton";

const BrandSkeleton = () => {
    return (
        <div className="section">
            <div className="container">
                <div className="row">
                    <h1 className="headline-4 text-center my-2 p-0">Top Brands</h1>
                    <span className="bodySmal mb-5 text-center">Explore a World of Choices Across Our Most Popular <br
                    />Shopping Categories </span>
                    {
                        Array.from({ length: 4 }).map((_,index)=>{
                            return (
                                <div key={index} className="col-md-3 p-2 col-lg-3 col-sm-6 col-12">
                                    <div className="card shadow-sm h-100 rounded-3 bg-white">
                                        <Lottie className="w-100" animationData={ImagePlaceHolder} loop={true}/>
                                        <div className="card-body">
                                            <Skeleton count={3}/>
                                        </div>
                                    </div>
                                </div>
                            )
                        })
                    }
                </div>
            </div>
        </div>
    );
};

export default BrandSkeleton;