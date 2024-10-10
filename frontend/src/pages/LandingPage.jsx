import React from 'react'
import { Link } from "react-router-dom";
import  Logo from "../assets/Logo.png"
import socials from "../assets/social-media-platforms.png"

function LandingPage() {
	return (
		<div className="bg-white min-h-screen flex flex-col items-center">
			<header className="w-full bg-blue-100 py-4 flex justify-between items-center px-8">
				<div className="flex items-center">
					<div className="bg-transparent rounded-full  flex items-center justify-center">
						<img src={Logo} alt="Smot Social Logo" />
					</div>
					{/* <span className="ml-2 text-black font-bold">Smot Social</span> */}
				</div>
				<button className="bg-white text-black border border-gray-300 rounded-full px-4 py-2 shadow-md">Get Started</button>
			</header>
			<main className="flex flex-row items-center mt-16">
			<div className='flex flex-col items-center justify-center'>
			<h1 className="text-4xl font-bold text-center">All your social posts, <span className="text-black italic">one easy click</span></h1>
				<p className="text-center text-gray-700 mt-4">Manage your platforms effortlessly and stay connected.</p>
				<Link to="/signup"><button className="bg-blue-500 text-white font-bold py-3 px-6 rounded mt-8">GET STARTED FOR FREE</button></Link>

			</div>
				
				<div className="mt-12">
					<img src={socials} alt="Illustration of a person managing multiple social media platforms" className="w-full max-w-md"/>
				</div>
			</main>
		</div>
	);
}

export default LandingPage