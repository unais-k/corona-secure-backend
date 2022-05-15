/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.6.12-log : Database - covicare
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`covicare` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `covicare`;

/*Table structure for table `asha_worker` */

DROP TABLE IF EXISTS `asha_worker`;

CREATE TABLE `asha_worker` (
  `asha_worker_id` int(11) NOT NULL AUTO_INCREMENT,
  `health_login_id` int(11) DEFAULT NULL,
  `asha_worker_name` varchar(50) DEFAULT NULL,
  `asha_worker_login_id` int(11) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `aadhar_no` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`asha_worker_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `asha_worker` */

insert  into `asha_worker`(`asha_worker_id`,`health_login_id`,`asha_worker_name`,`asha_worker_login_id`,`photo`,`address`,`phone`,`email`,`pin`,`gender`,`aadhar_no`) values 
(1,2,'Unais K',3,'3.jpg','Kattungal house,chungam,feroke(p.o),calicut','7594022964','unais01@mail.com','673631','Male','102030405060');

/*Table structure for table `emergency_option` */

DROP TABLE IF EXISTS `emergency_option`;

CREATE TABLE `emergency_option` (
  `emergency_id` int(11) NOT NULL AUTO_INCREMENT,
  `emergency_option` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `emergency_option` */

insert  into `emergency_option`(`emergency_id`,`emergency_option`) values 
(1,'FOOD'),
(2,'COUGH'),
(3,'FEVER'),
(4,'UNCONSIOUS');

/*Table structure for table `emergency_request` */

DROP TABLE IF EXISTS `emergency_request`;

CREATE TABLE `emergency_request` (
  `requestid` int(11) NOT NULL AUTO_INCREMENT,
  `emergency_id` int(11) DEFAULT NULL,
  `member_logid` int(11) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Pending',
  PRIMARY KEY (`requestid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `emergency_request` */

insert  into `emergency_request`(`requestid`,`emergency_id`,`member_logid`,`date`,`status`) values 
(1,1,5,'2022-03-30','Pending');

/*Table structure for table `health_reg` */

DROP TABLE IF EXISTS `health_reg`;

CREATE TABLE `health_reg` (
  `health_department_id` int(11) NOT NULL AUTO_INCREMENT,
  `health_name` varchar(50) DEFAULT NULL,
  `health_login_id` int(11) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `license` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`health_department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `health_reg` */

insert  into `health_reg`(`health_department_id`,`health_name`,`health_login_id`,`address`,`phone`,`license`,`email`) values 
(1,'chungam dispensery',2,'feroke,calicut','9988776601','KL85A01','chungam01@gmail.com');

/*Table structure for table `health_status` */

DROP TABLE IF EXISTS `health_status`;

CREATE TABLE `health_status` (
  `status_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_login_id` int(11) DEFAULT NULL,
  `temperature` varchar(100) DEFAULT NULL,
  `heartbeat` varchar(200) DEFAULT NULL,
  `cough` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `health_status` */

/*Table structure for table `house` */

DROP TABLE IF EXISTS `house`;

CREATE TABLE `house` (
  `house_id` int(11) NOT NULL AUTO_INCREMENT,
  `house_name` varchar(50) DEFAULT NULL,
  `house_no` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `ration_card_no` varchar(50) DEFAULT NULL,
  `ashaworker_login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`house_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `house` */

insert  into `house`(`house_id`,`house_name`,`house_no`,`address`,`ration_card_no`,`ashaworker_login_id`) values 
(1,'vattathil house','011','vattathil house chungam','12312345',3),
(2,'','','','',3),
(3,'padath house','012','padath house,feroke','1231234',3);

/*Table structure for table `house_members` */

DROP TABLE IF EXISTS `house_members`;

CREATE TABLE `house_members` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `house_id` int(11) DEFAULT NULL,
  `member_name` varchar(50) DEFAULT NULL,
  `member_login_id` int(11) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `covid_positive` varchar(50) DEFAULT NULL,
  `aadhar_no` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `house_members` */

insert  into `house_members`(`member_id`,`house_id`,`member_name`,`member_login_id`,`gender`,`age`,`photo`,`covid_positive`,`aadhar_no`) values 
(1,1,'amjad',5,'','20','5.jpg','no','112233');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`log_id`,`email`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'chungam01@gmail.com','chungam01','health'),
(3,'unais01@gmail.com','unais01','ashaworker'),
(4,'sahad01@gmail.com','sahad01','volunteer'),
(5,'amjad','112233','member');

/*Table structure for table `medicine_request` */

DROP TABLE IF EXISTS `medicine_request`;

CREATE TABLE `medicine_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_lid` int(11) NOT NULL,
  `medicine_name` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `medicine_request` */

insert  into `medicine_request`(`request_id`,`member_lid`,`medicine_name`,`description`,`date`,`status`) values 
(1,5,'paracetamol 500','fever','2022-03-30','Pending'),
(2,5,'krishna thulasi','cough','2022-03-30','Pending');

/*Table structure for table `quarantine_duration` */

DROP TABLE IF EXISTS `quarantine_duration`;

CREATE TABLE `quarantine_duration` (
  `did` int(11) DEFAULT NULL,
  `houseid` int(11) DEFAULT NULL,
  `datein` varchar(20) DEFAULT NULL,
  `dateout` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `quarantine_duration` */

insert  into `quarantine_duration`(`did`,`houseid`,`datein`,`dateout`) values 
(NULL,0,'2022-03-30',''),
(NULL,3,'2022-03-30','2022-04-13');

/*Table structure for table `volunter_reg` */

DROP TABLE IF EXISTS `volunter_reg`;

CREATE TABLE `volunter_reg` (
  `volunteer_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `volunteer_login_id` int(11) DEFAULT NULL,
  `health_login_id` int(11) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`volunteer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `volunter_reg` */

insert  into `volunter_reg`(`volunteer_id`,`user_name`,`volunteer_login_id`,`health_login_id`,`address`,`phone`,`email`,`photo`,`age`) values 
(1,'Sahad M',4,2,'Madanayil,chaliyam,kozhikode','9887755440','sahad01@gmail.com','4.jpg','20');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
