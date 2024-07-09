import React from 'react';
import SliderSkeleton from "../../skeleton/sliderSkeleton.jsx";
import productStore from "../../store/productStore.js";
import { Link } from 'react-router-dom'; // Add this line if Link is from react-router-dom

const Slider = () => {
    const { SliderList } = productStore();

    // Conditionally render based on SliderList length
    if (!SliderList || SliderList.length === 0) {
        return <SliderSkeleton />;
    } else {
        return (
            <div id="carouselExampleDark" className="carousel hero-bg carousel-dark slide">
                <div className="carousel-indicators">
                    {SliderList.map((item, index) => (
                        <button
                            key={index}
                            type="button"
                            data-bs-target="#carouselExampleDark"
                            data-bs-slide-to={index}
                            className={index === 0 ? "active" : ""}
                            aria-current={index === 0 ? "true" : "false"}
                            aria-label={`Slide ${index + 1}`}
                        ></button>
                    ))}
                </div>
                <div className="carousel-inner py-5">
                    {SliderList.map((item, index) => (
                        <div key={index} className={`carousel-item ${index === 0 ? "active" : ""}`} data-bs-interval="10000">
                            <div className="container">
                                <div className="row justify-content-center">
                                    <div className="col-12 col-lg-5 col-sm-12 col-md-5 p-5">
                                        <h1 className="headline-1">{item["title"]}</h1>
                                        <p>{item["des"]}</p>
                                        <Link to={item.link} className="btn text-white btn-success px-5">Buy Now</Link>
                                    </div>
                                    <div className="col-12 col-lg-5 col-sm-12 col-md-5 p-5">
                                        <img src={item["img"]} className="w-100" alt={item["title"]}/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
                <button className="carousel-control-prev btn rounded-5" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next btn" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
            </div>
        );
    }
};

export default Slider;
