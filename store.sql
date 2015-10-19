-- phpMyAdmin SQL Dump
-- version 4.2.12deb2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 19, 2015 at 03:18 AM
-- Server version: 5.6.25-0ubuntu0.15.04.1
-- PHP Version: 5.6.4-4ubuntu6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `store`
--

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE IF NOT EXISTS `items` (
`id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` float NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `name`, `price`, `user_id`) VALUES
(1, 'beer', 133, 1),
(3, 'whiskey', 4, 1),
(5, 'jagermeister', 2.5, 2),
(6, 'cocktail', 5.5, 2),
(7, 'much wine', 149.88, 1),
(17, 'asdfasd', 333, 1),
(20, 'ss', 3, 2),
(22, 'asdf', 33, 2),
(23, 'asdf', 2, 2),
(24, 'asdf', 2, 2),
(25, 'asdf', 1, 2),
(26, 'adsf', 1, 2),
(27, 'asdf', 1, 2),
(28, 'asdf', 1, 2),
(29, 'adsf', 1, 2),
(30, 'asdf', 3, 2),
(31, 'sadf', 1, 2),
(32, 'wr', 2, 2),
(33, 'sfd', 2, 2),
(34, 'qe3', 3, 2),
(35, 'ee', 555, 2),
(36, 'ee', 555, 2),
(37, 'ww', 2, 2),
(38, 's', 3, 2),
(39, '2', 3, 2),
(40, '3', 3, 2),
(41, '3', 3, 2),
(42, '3', 3, 2),
(43, '3', 3, 2),
(44, '3', 3, 2),
(45, '3', 3, 2),
(46, '3', 3, 2),
(47, '3', 3, 2),
(48, '3', 3, 2),
(49, '3', 3, 2),
(50, '3', 3, 2),
(51, '43', 34, 2),
(52, '2345', 2345, 2),
(53, '2345', 22345, 2),
(54, '2345', 2345, 2),
(55, '2345', 2354, 2),
(56, '2345', 2345, 2),
(57, '2345', 2345, 2),
(58, '2345', 2345, 2),
(59, '2345', 4334, 2),
(60, '2435', 2345, 2),
(61, '2345', 2345, 2),
(62, '2345', 2345, 2),
(63, '453', 2345, 2),
(64, '2345', 2345, 2),
(65, '2435', 345, 2),
(66, '2345', 2345, 2),
(67, '2345', 2345, 2),
(68, '2345', 2345, 2),
(69, '23423', 2345, 2),
(70, '2345', 234, 2),
(71, '2435', 2345, 2),
(72, '23452345', 4253, 2),
(73, '2435', 2345, 2),
(74, '243', 52435, 2),
(75, '234', 52345, 2),
(76, '2345', 2345, 2),
(77, '2435', 2345, 2),
(78, '2345', 2345, 2),
(79, '2345', 2345, 2),
(80, '2345', 2345, 2),
(81, '123', 42134100, 2),
(82, '1234', 1234, 2),
(83, '1234', 1342, 2),
(84, '1234', 1234, 2),
(85, '1234', 1243, 2),
(86, '1234', 2143, 2),
(87, '1234', 3412, 2),
(88, '1234', 1243, 2),
(89, '1234', 1234, 2),
(90, '1234', 1234, 2),
(91, 'sander', 222, 2),
(92, 'gerrit', 22, 2),
(93, 'test', 222, 2),
(94, '333', 333, 2),
(95, '33', 22, 2),
(96, 'dd', 33, 2),
(97, 'asdfasd', 32323, 2),
(98, '3233', 2222, 2),
(99, '333', 222, 2),
(100, 'sss', 333, 2),
(101, 'asdf', 222, 2),
(102, '333', 222, 2),
(103, '222', 222, 2),
(108, 'ss', 333, 2),
(109, 'www', 222, 2),
(110, 'rest', 22, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
`id` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(128) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `firstName`, `lastName`) VALUES
(1, 'gerritruiter@live.nl', 'a719ce1110a31d930a8532c25ee59d0eb475b8fcf8252183842098afb18dd4cc364977d29d636c49c347b794dfa886c8944f84fe320458a369e56a40546c677d', 'Gerrit', 'Ruiter'),
(2, 'admin@live.nl', 'a719ce1110a31d930a8532c25ee59d0eb475b8fcf8252183842098afb18dd4cc364977d29d636c49c347b794dfa886c8944f84fe320458a369e56a40546c677d', 'Ad', 'Min'),
(3, 'test@test.nl', 'admin', 'test1', 'test2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `items`
--
ALTER TABLE `items`
 ADD PRIMARY KEY (`id`), ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=111;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `items`
--
ALTER TABLE `items`
ADD CONSTRAINT `FK_ITEMS_USER_ID_USERS` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
