// src/components/Sidebar.jsx
import { FaTimes, FaHome, FaRegPaperPlane, FaFacebook, FaYoutube, FaInstagram, FaCog, FaQuestionCircle, FaLifeRing } from "react-icons/fa";
import { Link } from "react-router-dom";

const Sidebar = ({ isOpen, toggleSidebar }) => {
  return (
    <aside
      className={`fixed inset-y-0 left-0 transform ${
        isOpen ? "translate-x-0" : "-translate-x-full"
      } transition-transform duration-300 ease-in-out w-64 bg-white p-4 shadow-md z-50 md:relative md:translate-x-0`}
    >
      {/* Close Button (Visible on Mobile) */}
      <div className="flex justify-between items-center mb-6 md:hidden">
        <div className="flex items-center">
          <img src="https://placehold.co/40x40" alt="Logo" className="rounded-full mr-2" />
          <span className="text-xl font-bold">Smot Social</span>
        </div>
        <button onClick={toggleSidebar} className="text-gray-700 focus:outline-none" aria-label="Close Sidebar">
          <FaTimes size={24} />
        </button>
      </div>

      {/* Sidebar Content */}
      <nav className="mt-8">
        <ul>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaHome className="mr-2" />
              Overview
            </Link>
          </li>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaRegPaperPlane className="mr-2" />
              Post
            </Link>
          </li>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaFacebook className="mr-2" />
              Facebook
            </Link>
          </li>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaYoutube className="mr-2" />
              Youtube
            </Link>
          </li>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaInstagram className="mr-2" />
              Instagram
            </Link>
          </li>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaCog className="mr-2" />
              Settings
            </Link>
          </li>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaQuestionCircle className="mr-2" />
              Support
            </Link>
          </li>
          <li className="mb-4">
            <Link to="#" className="flex items-center text-gray-700 hover:text-blue-500">
              <FaLifeRing className="mr-2" />
              Help
            </Link>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
