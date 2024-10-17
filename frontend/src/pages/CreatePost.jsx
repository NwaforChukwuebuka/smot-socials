import React, { useState } from 'react';
import { FaImage, FaVideo, FaFacebook, FaInstagram, FaTwitter, FaYoutube } from 'react-icons/fa';
import { FaBars, FaTimes,  FaCog, FaLifeRing, FaCommentDots, FaUserCircle, FaLinkedin } from 'react-icons/fa'; // Importing more icons

function CreatePost() {
	

   
  const [postContent, setPostContent] = useState('');
  const [images, setImages] = useState([]);
  const [videos, setVideos] = useState([]);
  const [selectedPlatforms, setSelectedPlatforms] = useState({
    facebook: false,
    instagram: false,
    twitter: false,
    youtube: false,
  });

 
  const handleImageUpload = (e) => {
    const files = Array.from(e.target.files);
    setImages((prevImages) => [...prevImages, ...files]);
  };

  const handleVideoUpload = (e) => {
    const files = Array.from(e.target.files);
    setVideos((prevVideos) => [...prevVideos, ...files]);
  };

  const handlePlatformChange = (e) => {
    const { name, checked } = e.target;
    setSelectedPlatforms((prevPlatforms) => ({
      ...prevPlatforms,
      [name]: checked,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you would handle the submission logic, e.g., sending data to your backend.
    console.log({
      postContent,
      images,
      videos,
      selectedPlatforms,
    });
    // Reset the form
    setPostContent('');
    setImages([]);
    setVideos([]);
    setSelectedPlatforms({
      facebook: false,
      instagram: false,
      twitter: false,
      youtube: false,
    });
  };

  return (
    <div className="w-full mx-auto p-6 bg-white shadow-md rounded-md">
	<header className="flex justify-between items-center mb-6">
                    <button className="md:hidden p-2">
                         <FaTimes className="text-2xl" /> : <FaBars className="text-2xl" />
                    </button>
                    <h1 className="text-2xl font-bold">Hi, Michael Ebuka</h1>
                    <div className="flex items-center">

                        <img src="https://placehold.co/40x40" alt="User Avatar" className="rounded-full mr-2" />
                        <span>Michael Ebuka</span>
                    </div>
                </header>
      <h2 className="text-2xl font-bold mb-4">Create a New Post</h2>
      <form onSubmit={handleSubmit}>
        {/* Text Area */}
        <div className="mb-4">
          <label htmlFor="postContent" className="block text-gray-700 mb-2">
            Post Content
          </label>
          <textarea
            id="postContent"
            value={postContent}
            onChange={(e) => setPostContent(e.target.value)}
            rows="4"
            className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="What's on your mind?"
            required
          ></textarea>
        </div>

        {/* Image Upload */}
        <div className="mb-4">
          <label className="block text-gray-700 mb-2  items-center">
            <FaImage className="mr-2" /> Upload Images
          </label>
          <input
            type="file"
            accept="image/*"
            multiple
            onChange={handleImageUpload}
            className="w-full"
          />
        </div>

        {/* Video Upload */}
        <div className="mb-4">
          <label className="block text-gray-700 mb-2 flex items-center">
            <FaVideo className="mr-2" /> Upload Videos
          </label>
          <input
            type="file"
            accept="video/*"
            multiple
            onChange={handleVideoUpload}
            className="w-full"
          />
        </div>

        {/* Platform Selection */}
        <div className="mb-4">
          <span className="block text-gray-700 mb-2">Select Platforms</span>
          <div className="flex items-center space-x-4">
            <label className="flex items-center">
              <input
                type="checkbox"
                name="facebook"
                checked={selectedPlatforms.facebook}
                onChange={handlePlatformChange}
                className="form-checkbox h-5 w-5 text-blue-600"
              />
              <FaFacebook className="ml-2 text-blue-600" />
            </label>
            <label className="flex items-center">
              <input
                type="checkbox"
                name="instagram"
                checked={selectedPlatforms.instagram}
                onChange={handlePlatformChange}
                className="form-checkbox h-5 w-5 text-pink-600"
              />
              <FaInstagram className="ml-2 text-pink-600" />
            </label>
            <label className="flex items-center">
              <input
                type="checkbox"
                name="twitter"
                checked={selectedPlatforms.twitter}
                onChange={handlePlatformChange}
                className="form-checkbox h-5 w-5 text-blue-400"
              />
              <FaTwitter className="ml-2 text-blue-400" />
            </label>
            <label className="flex items-center">
              <input
                type="checkbox"
                name="youtube"
                checked={selectedPlatforms.youtube}
                onChange={handlePlatformChange}
                className="form-checkbox h-5 w-5 text-red-600"
              />
              <FaYoutube className="ml-2 text-red-600" />
            </label>
          </div>
        </div>

        {/* Preview Section */}
        <div className="mb-4">
          <span className="block text-gray-700 mb-2">Preview</span>
          {/* Image Previews */}
          {images.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-2">
              {images.map((image, index) => (
                <img
                  key={index}
                  src={URL.createObjectURL(image)}
                  alt={`Preview ${index + 1}`}
                  className="w-24 h-24 object-cover rounded-md"
                />
              ))}
            </div>
          )}
          {/* Video Previews */}
          {videos.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-2">
              {videos.map((video, index) => (
                <video
                  key={index}
                  controls
                  className="w-48 h-32 object-cover rounded-md"
                >
                  <source src={URL.createObjectURL(video)} type={video.type} />
                  Your browser does not support the video tag.
                </video>
              ))}
            </div>
          )}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition duration-200"
        >
          Share Post
        </button>
      </form>
    </div>
  );
}

export default CreatePost;
