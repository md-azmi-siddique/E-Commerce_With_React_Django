// import React from 'react';
import AppNavBar from "./appNavBar.jsx";
import Footer from "./footer.jsx";

const MasterLayout = (props) => {
    return (
        <>
            <AppNavBar/>
            {/* eslint-disable-next-line react/prop-types */}
            {props.children}
            <Footer/>
            
        </>
    );
};

export default MasterLayout;