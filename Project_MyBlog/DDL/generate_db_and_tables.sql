CREATE DATABASE IF NOT EXISTS `blog`;
USE blog;

CREATE TABLE IF NOT EXISTS `posts`
(
    `id`			smallint														 NOT NULL AUTO_INCREMENT,
    `title`         varchar(100)	CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `content`  		text 			CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `created_at`	timestamp                                                 		 NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `post_id_idx` (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;