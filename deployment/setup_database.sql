-- MySQL Database Setup Script for Electrical Machines Q&A Platform

CREATE DATABASE IF NOT EXISTS electrical_machines_qa CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create a dedicated user for the application
CREATE USER IF NOT EXISTS 'emqa_user'@'localhost' IDENTIFIED BY 'secure_password_here';
GRANT ALL PRIVILEGES ON electrical_machines_qa.* TO 'emqa_user'@'localhost';
FLUSH PRIVILEGES;

-- Use the database
USE electrical_machines_qa;

-- The tables will be created by Django migrations
