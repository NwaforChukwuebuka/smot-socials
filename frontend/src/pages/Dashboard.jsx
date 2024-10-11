import { useState } from "react";
import { FaBars, FaTimes, FaFacebook, FaInstagram, FaYoutube, FaCog, FaLifeRing, FaCommentDots, FaUserCircle, FaTwitter } from 'react-icons/fa'; // Importing more icons
import { Link } from 'react-router-dom';
import  Logo from "../assets/Logo.png"


const Dashboard = () => {
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);

    const toggleSidebar = () => {
        setIsSidebarOpen(!isSidebarOpen);
    };

    return (
        <div className="flex flex-col md:flex-row h-screen">
            {/* Sidebar */}
            <aside className={`fixed md:relative w-64 bg-white p-4 shadow-md transition-transform transform ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'} md:translate-x-0 z-50`}>
                <div className="flex justify-between items-center mb-6">
                    <div className="flex items-center">
                        <img src="https://placehold.co/40x40" alt="Logo" className="rounded-full mr-2" />
                        <img src={Logo} alt="Smot Social Logo" />
                        {/* <span className="text-xl font-bold">Smot Social</span> */}
                    </div>
                    <button onClick={toggleSidebar} className="md:hidden p-2">
                        <FaTimes className="text-2xl" />
                    </button>
                </div>
                {/* Navigation */}
                <nav>
                    <ul>
                        <li className="mb-4 flex items-center space-x-2">
                            <FaUserCircle className="text-blue-500" />
                            <a href="#" className="text-blue-500">Overview</a>
                        </li>
                        <li className="mb-4 flex items-center space-x-2">
                            <FaCommentDots />
                            <a href="/createpost">Post</a>
                        </li>
                        <li className="mb-4 flex items-center space-x-2">
                            <FaFacebook className="text-blue-500" />
                            <a href="#">Facebook</a>
                        </li>
                        <li className="mb-4 flex items-center space-x-2">
                            <FaYoutube className="text-red-500" />
                            <a href="#">YouTube</a>
                        </li>
                        <li className="mb-4 flex items-center space-x-2">
                            <FaInstagram className="text-pink-500" />
                            <a href="#">Instagram</a>
                        </li>
                        <li className="mb-4 flex items-center space-x-2">
                            <FaCog />
                            <a href="#">Settings</a>
                        </li>
                        <li className="mb-4 flex items-center space-x-2">
                            <FaLifeRing />
                            <a href="#">Support</a>
                        </li>
                    </ul>
                </nav>
            </aside>

            {/* Main Content */}
            <main className="flex-1 p-4 md:p-6">
                <header className="flex justify-between items-center mb-6">
                    <button onClick={toggleSidebar} className="md:hidden p-2">
                        {isSidebarOpen ? <FaTimes className="text-2xl" /> : <FaBars className="text-2xl" />}
                    </button>
                    <h1 className="text-2xl font-bold">Hi, Michael Ebuka</h1>
                    <div className="flex items-center">
                       <Link to="/createpost"> <button className="bg-blue-500 text-white px-4 py-2 rounded mr-4">New Post</button> </Link> 
                        <img src="https://placehold.co/40x40" alt="User Avatar" className="rounded-full mr-2" />
                        <span>Michael Ebuka</span>
                    </div>
                </header>

                {/* Stats Section */}
                <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 mb-6">
                    <div className="bg-white p-4 shadow-md flex items-center space-x-4">
                        <FaFacebook className="text-blue-500 text-3xl" />
                        <div>
                            <h2 className="text-lg font-bold">Facebook</h2>
                            <p className="text-2xl font-bold">4k</p>
                            <p className="text-green-500">Followers ↑ 12%</p>
                        </div>
                    </div>
                    <div className="bg-white p-4 shadow-md flex items-center space-x-4">
                        <FaInstagram className="text-pink-500 text-3xl" />
                        <div>
                            <h2 className="text-lg font-bold">Instagram</h2>
                            <p className="text-2xl font-bold">1k</p>
                            <p className="text-green-500">Followers ↑ 3%</p>
                        </div>
                    </div>
                    <div className="bg-white p-4 shadow-md flex items-center space-x-4">
                        <FaYoutube className="text-red-500 text-3xl" />
                        <div>
                            <h2 className="text-lg font-bold">YouTube</h2>
                            <p className="text-2xl font-bold">200</p>
                            <p className="text-green-500">Subscribers ↑ 5%</p>
                        </div>
                    </div>
                    <div className="bg-white p-4 shadow-md flex items-center space-x-4">
                        <FaTwitter className="text-blue-400 text-3xl" />
                        <div>
                            <h2 className="text-lg font-bold">X</h2>
                            <p className="text-2xl font-bold">67</p>
                            <p className="text-green-500">Followers ↑ 2%</p>
                        </div>
                    </div>
                </section>

                {/* Posts Section */}
                <section className="flex flex-col md:flex-row">
                    <div className="flex-1 bg-white p-6 shadow-md mb-6 md:mb-0 md:mr-6">
                        <h2 className="text-lg font-bold mb-4">X #smot123</h2>
                        <p className="mb-4">We started Socially for Trade Group</p>
                        <div className="border-t pt-4">
                            <p>Likes: 10</p>
                            <p>Comments: 4</p>
                            <p>Shares: 2</p>
                        </div>
                    </div>
                    <div className="w-full md:w-1/3 bg-white p-6 shadow-md">
                        <h2 className="text-lg font-bold mb-4">Recent Notifications</h2>
                        <ul>
                            <li className="mb-4 p-4 bg-blue-100 rounded">
                                <p><strong>@getopa255</strong> Started following you</p>
                                <p className="text-gray-500">15 min ago</p>
                            </li>
                            <li className="mb-4 p-4 bg-blue-100 rounded">
                                <p><strong>@gwlmac205</strong> Commented on your post</p>
                                <p className="text-gray-500">19 min ago</p>
                            </li>
                            <li className="mb-4 p-4 bg-blue-100 rounded">
                                <p><strong>@Mwica195</strong> Liked your post</p>
                                <p className="text-gray-500">1 hour ago</p>
                            </li>
                            <li className="mb-4 p-4 bg-blue-100 rounded">
                                <p><strong>@Mwica195</strong> Liked your post</p>
                                <p className="text-gray-500">30 min ago</p>
                            </li>
                        </ul>
                        <a href="#" className="text-blue-500">View all</a>
                    </div>
                </section>
            </main>
        </div>
    );
};

export default Dashboard;
