import React from 'react'
import { Link } from 'react-router-dom';
import  Logo from "../assets/Logo.png"


function RegisterPage() {
	return (
		<div>
			<header className="bg-blue-100 p-4 flex justify-between items-center">
				<div className="flex items-center">
					<img src={Logo} alt="Smot Social logo" className="mr-2"/>
				</div>
				<Link to="/signin">
					<span className="text-sm">Have a Smot Account? <a href="#" className="text-red-500 font-bold">SIGN IN</a></span>
				</Link>
			</header>
			<main className="flex justify-center items-center h-screen">
				<div className="w-full max-w-md">
					<h1 className="text-3xl font-bold mb-6 text-center">Get Started Now</h1>
					<form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
						<div className="mb-4">
							<label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="name">
								Name
							</label>
							<input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="name" type="text" placeholder="Enter your name"/>
						</div>
						<div className="mb-4">
							<label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
								Email address
							</label>
							<input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="Enter your email"/>
						</div>
						<div className="mb-4">
							<label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
								Password
							</label>
							<input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Enter your password"/>
						</div>
						<div className="mb-4">
							<label className="inline-flex items-center">
								<input type="checkbox" className="form-checkbox"/>
								<span className="ml-2 text-sm text-gray-700">I agree to the <a href="#" className="text-blue-500">terms & policy</a></span>
							</label>
						</div>
						<div className="mb-4">
						<Link to="/signin">
						<button className="bg-blue-100 hover:bg-blue-200 text-black font-bold py-2 px-4 rounded w-full" type="button">
								Signup
							</button>
						</Link>
							
						</div>
						<div className="text-center text-gray-500 text-sm mb-4">Or</div>
						<div className="mb-4">
							<button className="bg-white border border-gray-300 text-gray-700 font-bold py-2 px-4 rounded w-full flex items-center justify-center" type="button">
								<img src="https://placehold.co/20x20" alt="Google logo" className="mr-2"/>
								Sign in with Google
							</button>
						</div>
						<div className="text-center text-sm">
							Have an account? <a href="#" className="text-blue-500">Sign In</a>
						</div>
					</form>
				</div>
			</main>
		</div>
	);
}

export default RegisterPage