-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: mysql-secdb2.csacono2fbuh.us-east-2.rds.amazonaws.com    Database: musecdb
-- ------------------------------------------------------
-- Server version	5.6.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `musecdb`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `musecdb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `musecdb`;

--
-- Table structure for table `Jurisdiction`
--

DROP TABLE IF EXISTS `Jurisdiction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Jurisdiction` (
  `PatientID` int(11) NOT NULL DEFAULT '0',
  `ID` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`PatientID`,`ID`),
  KEY `ID` (`ID`),
  CONSTRAINT `Jurisdiction_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `Patient` (`PatientID`),
  CONSTRAINT `Jurisdiction_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `User` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jurisdiction`
--

LOCK TABLES `Jurisdiction` WRITE;
/*!40000 ALTER TABLE `Jurisdiction` DISABLE KEYS */;
INSERT INTO `Jurisdiction` VALUES (1013,2501),(1014,2501),(1015,2501),(1018,2501),(1019,2501),(1010,2507),(1011,2507),(1012,2507),(1016,2507),(1017,2507);
/*!40000 ALTER TABLE `Jurisdiction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Patient` (
  `SSN` int(11) NOT NULL,
  `FirstName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Gender` varchar(225) DEFAULT NULL,
  `Prescriptions` text,
  `Height` int(11) DEFAULT NULL,
  `Weight` int(11) DEFAULT NULL,
  `Conditions` text,
  `PatientID` int(11) NOT NULL AUTO_INCREMENT,
  `ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`PatientID`),
  KEY `fk_user_id` (`ID`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`ID`) REFERENCES `User` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1020 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
INSERT INTO `Patient` VALUES (101010101,'Daniel','Dunn','1995-03-10','Male','None',69,190,'Sprained Ankle',1010,2500),(111111111,'Jane','Smith','1963-02-17','Female','Oxycodone, 70mg',65,125,'Broken Arm',1011,2514),(222222222,'David','Emily','1988-09-27','Male','Viagra, 50mg',71,200,'Erectile Dysfunction',1012,2504),(333333333,'Elizabeth','Sharpe','1992-10-25','Female','Azithrymyacin, 200mg',64,130,'Bronchitis',1013,2513),(444444444,'Trevor','Leach','1990-12-12','Male','Penicillin, 120mg',67,160,'Sinusitis',1014,2502),(555555555,'Joe','Chandler','1956-07-21','Male','Medicine stuff, 90mg',70,165,'Some condition',1015,2506),(666666666,'Cersei','Lannister','1979-04-20','Female','None',62,125,'Psychopathy',1016,2512),(777777777,'Dmitrii','Chemodanov','1983-01-11','Male','None',69,170,'None',1017,2505),(888888888,'Margaery','Tyrell','1984-08-23','Female','Skin Paste, 1 tube',63,120,'Severe burns',1018,2511),(999999999,'Andrew','Krall','2000-06-30','Male','Bosley',68,165,'Hair Loss',1019,2503);
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `FirstName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `AuthType` varchar(255) NOT NULL,
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2523 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('dpdbp7@mail.missouri.edu','$6$rounds=656000$xra1Gr/zoxlRSPki$mhh/7HaZygHSAgNRSps6JqB5mwSZ9RS.YiJE1QSXyWy8WZxOVB0zmgZGhBGLph3FPyIQxz4XLqTzc2r7tk.y80','Daniel','Dunn','Patient',2500),('calyamp@missouri.edu','$6$rounds=656000$LkH/TQJWX.z/ZyR9$TxscAN27OWxucy.oH.Ca99jodlzjIMXxbTQurchW7BLQxUoAwJVuFGiOEVa3Pw7kNJ8Hp/d5y66nZlSZvAlhK1','Prasad','Calyam','Doctor',2501),('tklzqd@mail.missouri.edu','$6$rounds=656000$6CEbDh6jZ57OqMZ8$6ceK/li7qBRXnhgCgcWIAVf7jo7IdHNzu9x1ozxu6on4sVvPFqahetCmV4DasdFgp2pIVFBwr/gvqygWX9KvC1','Trevor','Leach','Patient',2502),('ankwdf@mail.missouri.edu','$6$rounds=656000$RAeTSyzVwOoV0ZFq$512v.NMtAR5R4k3IbsqXV36T7.Ombga/eozZ7CJN7NYQU0CVAk3LhYVgF8NQsj7vXSU4rM.LRaR81wLRUw9sd.','Andrew','Krall','Patient',2503),('daeth5@mail.missouri.edu','$6$rounds=656000$qWjfw15vqv8DHCwO$cUCyBZsac95Qz/bjwBkZosKM7GYDJSKM4gG316VXxTOmD4Gv6nBxvPmCroO82RGGHl3f36GYbjJvrxbdPHIHf.','David','Emily','Patient',2504),('dycbt4@mail.missouri.edu','$6$rounds=656000$7bI6H2qob6Z8wJrz$vWzm.97P5ymquDWFlQCI0ytUO1FLY6XHONNDbeP7syhnIqtVuMpJs6W3qmRgxRHa0ppGd6gH.2VYYsOEwXazF/','Dmitrii','Chemodanov','Patient',2505),('jacvzb@mail.missouri.edu','$6$rounds=656000$cud.JJX89KwIbDje$2N8UKCPnG6ogcA5xLnzc19SHk2YQM8A44J8ZEGyJhg9xqq.qFb9TIWH0rrACSET/7/nqUjt7JRBu7flMyNUH91','Joseph','Chandler','Patient',2506),('muffinman@mail.missouri.edu','$6$rounds=656000$9SsadFGJ4HZTyVKc$xVfuKxJBDZvezzxnn8QuTyYVBvBjoQRSVdFBxuuBheqWnaCuc/po8qCJiHcloYgDpxTZtToXus/2MXfeLnK6P1','Muffin','TheMan','Doctor',2507),('larrybird@mail.missouri.edu','$6$rounds=656000$piB8D3TIwNKagUjU$ZMLKIvH03GJ/TVxodcqAY/4vPo70Y1SNonysxBXo7mhQdYctnnmDRmDa0dOonMCCmPX5EuYDdVYrnKnVsPwdD1','Larry','Bird','SysAdmin',2508),('markduckerberg@harvard.edu','$6$rounds=656000$yzWZuNOPoJoCuOYG$H85XqkvMqpF4Q4fH/nDWK7mHiU6y3qVAMS1p298jOjXOpDUK2cBUhCcFnVRGZtOqbIjnxJjW0qfEfb9Zn..Ey1','Mark','Duckerberg','SysAdmin',2510),('daqueenbee@westeros.org','$6$rounds=656000$CYcKdMifetYAUnW6$LzLBghwgHO.rjpp9VXEr5mJSsGTSXY.2qn3qBTGHDZyvnS1nglplb13iKaa/Yothm8tENhq6q3QASV25SQI9w0','Margaery','Tyrell','Patient',2511),('queenmother@7kingdoms.com','$6$rounds=656000$CI8WOTayk7jLRCym$3Uc/ae3Tn.zpTX6ApXAzNDvAXwtV15csxN/mIp1zkxVE0lifie7WaXuY6DPyKoplWu8JMJiyCR3mTDUe7/OCd0','Cersei','Lannister','Patient',2512),('lizysharp@yahoo.com','$6$rounds=656000$Pdc90RoJQGFzzj9Z$aGG.pqL/HZcioDaLtmjvw9k1P7OUisgq97GEG0Jj5e/YB0sKGVU9qve3yZAWvE7EkZUnTgI3oV/uqusqeGTWJ.','Elizabeth','Sharpe','Patient',2513),('jane.smith@gmail.com','$6$rounds=656000$xKjsltJGOAq/BgXH$ARTeS1gVhoKNpgFVs0dqmcwosm2KwnFnYg3VxlZbx.jLg04p/Ri3KNputtgFCIpcf0qbT9l0Tvr5G6JC8fODZ.','Jane','Smith','Patient',2514),('test','$6$rounds=656000$w47DSxnhfM38PE/W$JBT8qKwsw0nVOLUgeA2oOJogvmJSYZUjSNRVx/rS6Us.nn0..07txzgDM8kwsNoGUg96QOOLYOfzCePxENSoO.','Trevor','Leach','Patient',2522);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-09  8:10:58
