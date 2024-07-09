import React from 'react';
import productStore from "../../store/productStore.js";
import CategorySkeleton from "../../skeleton/categorySkeleton.jsx";
import {Link} from "react-router-dom";

const Categories = () => {
    const {CategoryList} = productStore()
    if (!CategoryList || CategoryList.length === 0) {
        return <CategorySkeleton/>
    }
    else {
        return (
            <div className="section">
                <div className="container">
                    <div className="row">
                        <h1 className="headline-4 text-center my-2 p-0">Top Categories</h1>
                        <span
                            className="bodySmal mb-5 text-center">Explore a World of Choices Across Our Most Popular <br
                        />Shopping Categories </span>
                        {
                            CategoryList.map((item, index)=>{
                                return (
                                    <div key={index} className="col-2 col-lg-8r text-center col-md-8r p-2">
                                        <Link to={`/by-category/${item["id"]}`} className="card h-100 border-0 bg-light">
                                            <div className="card-body">
                                                <img alt="" className="w-50" src={item["category_img"]}/>
                                                <p className="bodySmal mt-3">{item["category_name"]}</p>
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

export default Categories;