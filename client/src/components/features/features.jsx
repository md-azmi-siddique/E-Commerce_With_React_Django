import React from 'react';
import featureStore from "../../store/featureStore.js";
import FeatureSkeleton from "../../skeleton/featureSkeleton.jsx";

const Features = () => {
    const {FeatureList} = featureStore()
    // console.log(FeatureList.length)
    if (!FeatureList || FeatureList.length === 0) {
        return <FeatureSkeleton/>
    }else {
        return (
            <div className="container section">
                <div className="row">
                    <div className="col-6 p-2 col-md-3 col-lg-3 col-sm-6">
                        <div className="card shadow-sm">
                            <div className="card-body">
                                <div className="row">
                                    <div className="col-3">
                                        <img className="w-100" src=""/>
                                    </div>
                                    <div className="col-9">
                                        <h3 className="bodyXLarge">name</h3>
                                        <span className="bodySmal">description</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

};

export default Features;