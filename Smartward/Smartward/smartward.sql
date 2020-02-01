-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 05, 2020 at 02:46 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smartward`
--

-- --------------------------------------------------------

--
-- Table structure for table `ward_registration`
--

CREATE TABLE `ward_registration` (
  `ID` varchar(30) NOT NULL,
  `Municipality` varchar(75) NOT NULL,
  `WardNo` varchar(5) NOT NULL,
  `State` varchar(5) NOT NULL,
  `Address` varchar(150) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `IP_Address` varchar(15) NOT NULL,
  `LogoPath` varchar(150) NOT NULL,
  `Password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ward_registration`
--

INSERT INTO `ward_registration` (`ID`, `Municipality`, `WardNo`, `State`, `Address`, `Phone`, `Email`, `IP_Address`, `LogoPath`, `Password`) VALUES
('03koshirural04', 'Koshi Rural Municipality', '04', '03', 'Mangaltar', '3278326', 'pshreyam@gmail.com', '****', '', '54321'),
('03namobuddha04', 'Namobuddha Municipality', '04', '03', 'Khanalthok', '01231238', 'ch.ramraj35@gmail.com', '127.0.1.1', '', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ward_registration`
--
ALTER TABLE `ward_registration`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
