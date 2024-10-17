import React from 'react'
import { Link } from 'react-router-dom';
import  Logo from "../assets/Logo.png"


function LoginPage() {
	return (
		<div className="min-h-screen flex flex-col">
			<header className="bg-blue-100 py-4">
				<div className="container mx-auto flex justify-between items-center">
					<div className="flex items-center">
						<img src={Logo} alt="Logo"/>
					</div>
					<Link to="signin">
						<span className="text-sm">Don't Have an Account? <a href="#" className="text-red-500 font-bold">SIGN UP</a></span>
					</Link>
				</div>
			</header>
			<main className="flex-grow flex items-center justify-center">
				<div className="bg-white p-8 rounded shadow-md w-full max-w-md">
					<h1 className="text-2xl font-bold mb-2">Welcome back!</h1>
					<p className="text-gray-600 mb-6">Please enter your login details</p>
					<form>
						<div className="mb-4">
							<label className="block text-gray-700">Email address</label>
							<input type="email" placeholder="Enter your email" className="w-full px-3 py-2 border rounded"/>
						</div>
						<div className="mb-4">
							<label className="block text-gray-700">Password</label>
							<input type="password" placeholder="Password" className="w-full px-3 py-2 border rounded"/>
							<a href="#" className="text-sm text-blue-500 float-right mt-1">forget password</a>
						</div>
						<div className="mb-4 flex items-center">
							<input type="checkbox" id="remember" className="mr-2"/>
							<label htmlFor="remember" className="text-gray-700">Remember this device</label>
						</div>
						<Link to="/dashboard">
						<button type="submit" className="w-full bg-blue-100 text-blue-700 py-2 rounded">Login</button></Link>
					</form>
					<div className="my-6 text-center text-gray-500">Or</div>
					<button className="w-full flex items-center justify-center border py-2 rounded">
						<img src="https://placehold.co/20x20" alt="Google Logo" className="h-5 w-5 mr-2"/>
						Sign in with Google
					</button>
					<p className="mt-6 text-center text-gray-700">Don't have an account? <a href="#" className="text-blue-500 font-bold">Sign Up</a></p>
				</div>
			</main>
		</div>
	);
}

export default LoginPage