-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2024 at 10:05 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `students`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Name` varchar(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `mname` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Mobile` bigint(20) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `paddress` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `religion` varchar(50) NOT NULL,
  `voter` varchar(50) NOT NULL,
  `cat` varchar(50) NOT NULL,
  `caste` varchar(50) NOT NULL,
  `subcaste` varchar(50) NOT NULL,
  `income` varchar(50) NOT NULL,
  `incomecertif` varchar(50) NOT NULL,
  `sem` int(11) NOT NULL,
  `aadhar` varchar(50) NOT NULL,
  `blood` varchar(50) NOT NULL,
  `parentsmobile` bigint(20) NOT NULL,
  `usn` varchar(50) NOT NULL,
  `Batch` year(4) NOT NULL,
  `Branch` varchar(50) NOT NULL,
  `scheme` year(4) NOT NULL,
  `Course` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `rank` varchar(50) NOT NULL,
  `regno` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `categorya` varchar(50) NOT NULL,
  `admission` date NOT NULL,
  `fees` varchar(50) NOT NULL,
  `marks` varchar(50) NOT NULL,
  `num` varchar(50) NOT NULL,
  `programme` varchar(50) NOT NULL,
  `school` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` ();

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`usn`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
