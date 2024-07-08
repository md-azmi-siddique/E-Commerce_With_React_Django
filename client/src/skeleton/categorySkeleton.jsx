import React from 'react';
import Lottie from "lottie-react";
import Skeleton from "react-loading-skeleton";
import ImagePlaceHolder from '../assets/images/image.json';

const CategorySkeleton = () => {
    return (
        <div className="section">
            <div className="container">
                <div className="row">
                    <h1 className="headline-4 text-center my-2 p-0">Top Categories</h1>
                    <span className="bodySmal mb-5 text-center">Explore a World of Choices Across Our Most Popular <br />Shopping Categories</span>
                    {
                        Array.from(Array(16)).map((_,index) => {
                            return (
                                // eslint-disable-next-line react/jsx-key
                                <div key={index} className="col-6 p-2 col-md-3 col-lg-3 col-sm-6">
                                    <div className="card shadow-sm">
                                        <div className="card-body">
                                            <div className="row">
                                                <Lottie className="w-100" animationData={ImagePlaceHolder}
                                                        loop={true}/>
                                                <div className="col">
                                                    <Skeleton count={2}/>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            );
                        })
                    }
                </div>
            </div>
        </div>
    );
};

export default CategorySkeleton;
