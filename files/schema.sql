CREATE TABLE `draw` (
  `id` bigint(20) NOT NULL,
  `createdDate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `numberOfTheDay` int(11) NOT NULL,
  `isActive` varchar(255) NOT NULL DEFAULT 'N'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `mobileMoney` (
  `id` bigint(20) NOT NULL,
  `createdDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `company` varchar(255) DEFAULT NULL,
  `operator` varchar(255) DEFAULT NULL,
  `txnId` varchar(255) DEFAULT NULL,
  `paybillNumber` varchar(255) DEFAULT NULL,
  `receipt` varchar(255) DEFAULT NULL,
  `msisdn` varchar(255) DEFAULT NULL,
  `amount` int(11) NOT NULL,
  `reference` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `numberChoice` varchar(255) DEFAULT NULL,
  `statusId` int(11) NOT NULL,
  `transactionTypeId` int(11) NOT NULL,
  `playerId` bigint(20) NOT NULL,
  `processed` varchar(1) NOT NULL DEFAULT 'N',
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `momoStatus` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `momoStatus` (`id`, `name`) VALUES
(1, 'New'),
(2, 'Reserved'),
(3, 'Completed'),
(4, 'Failure');

CREATE TABLE `player` (
  `id` bigint(20) NOT NULL,
  `msisdn` varchar(255) NOT NULL,
  `operator` varchar(255) DEFAULT NULL,
  `createdDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `lastPlayedDate` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `transaction` (
  `id` bigint(20) NOT NULL,
  `ticket` varchar(255) DEFAULT NULL,
  `numberOfTheDay` int(11) DEFAULT NULL,
  `jackpotNumber` int(11) DEFAULT NULL,
  `createdDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `updatedDate` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
  `playerId` bigint(20) DEFAULT NULL,
  `mobileMoneyId` bigint(20) DEFAULT NULL,
  `drawId` bigint(20) DEFAULT NULL,
  `isPaid` varchar(1) NOT NULL DEFAULT 'N',
  `numberChoice` varchar(255) DEFAULT NULL,
  `winningAmount` int(11) NOT NULL DEFAULT 0,
  `payoutAmount` int(11) NOT NULL DEFAULT 0,
  `luckNumberId` int(11) DEFAULT NULL,
  `createdAt` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `transactionType` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `transactionType` (`id`, `name`) VALUES
(1, 'Debit'),
(2, 'Deposit');

CREATE TABLE `rtp` (
  `id` bigint(20) NOT NULL,
  `createdAt` timestamp NULL DEFAULT current_timestamp(),
  `collection` double NOT NULL DEFAULT 0,
  `payout` double NOT NULL DEFAULT 0,
  `rtp` double NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `draw`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `mobileMoney`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `momoStatus`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `player`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `transactionType`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `draw`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `mobileMoney`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `momoStatus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

ALTER TABLE `player`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `transaction`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `transactionType`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `rtp`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `rtp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
