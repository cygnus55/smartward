-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 28, 2019 at 01:42 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12

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
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dob_year` int(4) NOT NULL,
  `dob_month` int(2) NOT NULL,
  `dob_date` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `username`, `password`, `dob_year`, `dob_month`, `dob_date`) VALUES
(1, 'Admin', 'Admin', 'admin', 'admin', 2019, 12, 28),
(2, 'Mahendra Singh', 'Dhoni', 'msd183', 'mahi', 1981, 7, 7),
(6, 'Hero', 'Hero', 'hero', 'hero', 2015, 12, 13),
(8, 'Hello', 'Hello', 'asdf', 'asfdf', 1676, 11, 11),
(9, 'Rahul', 'KL', 'imklrahul', 'klrahul', 1990, 12, 25),
(11, 'Rohit', 'Sharma', 'hitman', 'hitman', 1988, 4, 11),
(12, 'Virat ', 'Kohli', 'imvkohli', 'kohli100', 1988, 11, 5),
(13, 'Shreyas', 'Iyer', 'shreyas1994', 'iyer1994', 1994, 12, 6),
(14, 'Shikhar', 'Dhawan', 'sdhawan', 'gabbarisback', 1986, 12, 5),
(15, 'Ravindra', 'Jadeja', 'rjadeja', 'rockstar', 1988, 12, 6),
(16, 'Virat', 'Singh', 'vsingh', 'singhvjharkhand', 1994, 10, 3),
(17, 'Ajyinka', 'Rahane', 'amrahane88', 'rhne88', 1988, 10, 3),
(20, 'Ricky', 'Ponting', 'rponting100', 'rpont', 1975, 3, 4),
(21, 'Kapil', 'Dev', 'kapildev1983', 'wc1983', 1965, 10, 4),
(22, 'Sunil', 'Gavaskar', 'smgavaskar', 'gavaskar83', 1951, 10, 23),
(23, 'Hi', 'Hi', 'hi', 'hi', 1999, 1, 2),
(24, 'Myname', 'Myname', 'myname', 'myname', 1234, 5, 6),
(28, 'Smartward', 'Smartward', 'smartward', 'smartward', 2019, 12, 1),
(29, 'Why', 'Why', 'app', 'Hello', 1223, 12, 3),
(30, 'Asdfghj', 'Asdfghj', 'asdfghj', 'asdfghj', 1223, 3, 4),
(31, 'App', 'Sss', 'sdf', 'hello', 1223, 4, 5),
(32, 'Jasprit', 'Bumrah', 'bum_rah', 'boomboom', 1993, 12, 6),
(34, 'Hari', 'Prasad', 'hprasad', 'prasadi', 2000, 3, 4),
(35, 'Deependra', 'Gupta', 'dgupta', 'deependra12', 1222, 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `wada`
--

CREATE TABLE `wada` (
  `id` int(11) NOT NULL,
  `wada_name` varchar(100) NOT NULL,
  `wada_address` varchar(100) NOT NULL,
  `wada_info` varchar(1000) NOT NULL,
  `current` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `wada`
--

INSERT INTO `wada` (`id`, `wada_name`, `wada_address`, `wada_info`, `current`) VALUES
(18, 'Ward no. 1', 'Dhulikhel', 'The elders of the tourism town Dhulikhel Municipality, Ward 4, Sabit Devitar Village Development Committee, are made up of 1,3,3,3,3,8. The population here is 5 Representative of the people of this ward Ramesh Prasad Ghorasine was elected from the local election of the ward. This ward is mainly based in agriculture area, especially in Tamang, Brahmin, Chhetri.', 1),
(20, 'Ward no. 4', 'Banepa', 'third wada', 0),
(21, 'Ward no. 5', 'Bhaktapur', 'This is the nearest ward office in this municipality. I do not know the remaining details of this ward office.Thank you. ', 0),
(22, 'Ward no. 2', 'Madhyapur Thimi', 'Hello Boys', 0),
(23, 'Ward no. 3', 'Sallaghari', 'ss dsfsf sdgdag', 0),
(24, 'Ward no. 10', 'Banepa', 'This is a test.', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `wada`
--
ALTER TABLE `wada`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `wada`
--
ALTER TABLE `wada`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
