CREATE DATABASE main;
USE main;
CREATE TABLE `exchange_rates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `base_currency` varchar(10) NOT NULL,
  `to_exchange_currency` varchar(10) NOT NULL,
  `exchange_rate` float NOT NULL,
  `date` date DEFAULT NULL,
  `tbl_timestamp` timestamp NOT NULL DEFAULT NOW(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;