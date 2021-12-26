-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-12-16 17:31:06
-- 服务器版本： 5.6.50-log
-- PHP 版本： 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `timepill`
--

-- --------------------------------------------------------

--
-- 表的结构 `article_article`
--

CREATE TABLE `article_article` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `square_open` tinyint(1) NOT NULL,
  `expire_time` datetime(6) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `diary_type` varchar(8) NOT NULL,
  `add_date` datetime(6) NOT NULL,
  `mod_date` datetime(6) NOT NULL,
  `author_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `article_article`
--

INSERT INTO `article_article` (`id`, `title`, `content`, `square_open`, `expire_time`, `status`, `diary_type`, `add_date`, `mod_date`, `author_id_id`) VALUES
(1, '12313', '12321313', 1, NULL, 1, 'primary', '2021-12-16 09:07:13.715994', '2021-12-16 09:07:13.716997', 1),
(2, '1231231', '12313131', 1, '2021-12-16 09:07:39.000000', 1, 'pill', '2021-12-16 09:07:31.189746', '2021-12-16 09:07:46.127747', 1);

-- --------------------------------------------------------

--
-- 表的结构 `article_comment`
--

CREATE TABLE `article_comment` (
  `id` bigint(20) NOT NULL,
  `comment_content` longtext NOT NULL,
  `comment_time` datetime(6) NOT NULL,
  `article_id` int(11) NOT NULL,
  `comment_author_id` int(11) NOT NULL,
  `pre_comment_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `article_comment`
--

INSERT INTO `article_comment` (`id`, `comment_content`, `comment_time`, `article_id`, `comment_author_id`, `pre_comment_id`) VALUES
(1, '评论测试', '2021-12-16 09:19:57.147564', 1, 1, NULL),
(2, '回复测试', '2021-12-16 09:20:06.021810', 1, 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add 用户', 7, 'add_user'),
(26, 'Can change 用户', 7, 'change_user'),
(27, 'Can delete 用户', 7, 'delete_user'),
(28, 'Can view 用户', 7, 'view_user'),
(29, 'Can add 确认码', 8, 'add_confirmstring'),
(30, 'Can change 确认码', 8, 'change_confirmstring'),
(31, 'Can delete 确认码', 8, 'delete_confirmstring'),
(32, 'Can view 确认码', 8, 'view_confirmstring'),
(33, 'Can add captcha store', 9, 'add_captchastore'),
(34, 'Can change captcha store', 9, 'change_captchastore'),
(35, 'Can delete captcha store', 9, 'delete_captchastore'),
(36, 'Can view captcha store', 9, 'view_captchastore'),
(37, 'Can add article', 10, 'add_article'),
(38, 'Can change article', 10, 'change_article'),
(39, 'Can delete article', 10, 'delete_article'),
(40, 'Can view article', 10, 'view_article'),
(41, 'Can add comment', 11, 'add_comment'),
(42, 'Can change comment', 11, 'change_comment'),
(43, 'Can delete comment', 11, 'delete_comment'),
(44, 'Can view comment', 11, 'view_comment');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$poPMxqV6Ecn8v2w3mphHtw$gdJ0+G/NP5xMgLIlVSwWyyMsRY0AZGUWD0+95Oum3cM=', '2021-12-16 09:03:57.810134', 1, 'seddon', '', '', 'seddon@mail.nwpu.edu.cn', 1, 1, '2021-12-16 09:03:50.581223');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `captcha_captchastore`
--

CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'article', 'article'),
(11, 'article', 'comment'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(9, 'captcha', 'captchastore'),
(5, 'contenttypes', 'contenttype'),
(8, 'login', 'confirmstring'),
(7, 'login', 'user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-16 09:03:21.228257'),
(2, 'auth', '0001_initial', '2021-12-16 09:03:23.483395'),
(3, 'admin', '0001_initial', '2021-12-16 09:03:24.093839'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-12-16 09:03:24.180487'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-16 09:03:24.269710'),
(6, 'login', '0001_initial', '2021-12-16 09:03:24.344698'),
(7, 'login', '0002_confirmstring_user', '2021-12-16 09:03:25.004948'),
(8, 'article', '0001_initial', '2021-12-16 09:03:25.073954'),
(9, 'article', '0002_article_comment', '2021-12-16 09:03:26.214277'),
(10, 'contenttypes', '0002_remove_content_type_name', '2021-12-16 09:03:26.576196'),
(11, 'auth', '0002_alter_permission_name_max_length', '2021-12-16 09:03:26.743051'),
(12, 'auth', '0003_alter_user_email_max_length', '2021-12-16 09:03:26.946196'),
(13, 'auth', '0004_alter_user_username_opts', '2021-12-16 09:03:27.032545'),
(14, 'auth', '0005_alter_user_last_login_null', '2021-12-16 09:03:27.209715'),
(15, 'auth', '0006_require_contenttypes_0002', '2021-12-16 09:03:27.284083'),
(16, 'auth', '0007_alter_validators_add_error_messages', '2021-12-16 09:03:27.476102'),
(17, 'auth', '0008_alter_user_username_max_length', '2021-12-16 09:03:27.655190'),
(18, 'auth', '0009_alter_user_last_name_max_length', '2021-12-16 09:03:27.816964'),
(19, 'auth', '0010_alter_group_name_max_length', '2021-12-16 09:03:27.993044'),
(20, 'auth', '0011_update_proxy_permissions', '2021-12-16 09:03:28.185346'),
(21, 'auth', '0012_alter_user_first_name_max_length', '2021-12-16 09:03:28.390177'),
(22, 'captcha', '0001_initial', '2021-12-16 09:03:28.711340'),
(23, 'sessions', '0001_initial', '2021-12-16 09:03:28.991520'),
(24, 'article', '0003_alter_comment_pre_comment', '2021-12-16 09:18:11.184762');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4mqjz418cyhag79uqaic4t5v885kwate', '.eJxVjDsOwjAQBe_iGlnrLw4lfc5gre1dHECOFCcV4u4QKQW0b2beS0Tc1hq3TkucirgIJU6_W8L8oLaDcsd2m2We27pMSe6KPGiX41zoeT3cv4OKvX5rN3Cg7AkMFWXZMGgOJtkSIDiApMBok4PzjrXzXNDbBNYDBhzOxrJ4fwDXWTc_:1mxmg9:4I6k2QpQRjdvVPKTSu0lI_9fCAtfq2ioRz9OnL0OC2c', '2021-12-30 09:03:57.851829'),
('qeypzvb2o9uh2jthmhqw0n7g15co2r4p', 'eyJpc19sb2dpbiI6dHJ1ZSwidXNlcl9pZCI6MSwidXNlcl9uYW1lIjoic2VkZG9uIn0:1mxn0X:SxppXZYYEPI0_v94PQzzT-urq6xhnqqVAO1wmstbL8Y', '2021-12-30 09:25:01.751955'),
('sh520d12fn9i23n10zcp174qmgs3ytrq', 'eyJpc19sb2dpbiI6dHJ1ZSwidXNlcl9pZCI6MSwidXNlcl9uYW1lIjoic2VkZG9uIn0:1mxmjB:dZgTVQK4NPPOG4u1cLdVkQXQulywKQCavrrSsPbEtDc', '2021-12-30 09:07:05.891015');

-- --------------------------------------------------------

--
-- 表的结构 `login_confirmstring`
--

CREATE TABLE `login_confirmstring` (
  `id` int(11) NOT NULL,
  `code` varchar(256) NOT NULL,
  `c_time` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `login_user`
--

CREATE TABLE `login_user` (
  `id` int(11) NOT NULL,
  `name` varchar(128) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(254) NOT NULL,
  `sex` varchar(32) NOT NULL,
  `c_time` datetime(6) NOT NULL,
  `has_confirmed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `login_user`
--

INSERT INTO `login_user` (`id`, `name`, `password`, `email`, `sex`, `c_time`, `has_confirmed`) VALUES
(1, 'seddon', 'f6a39e4cf9017b65042c4ca33a054db8304d541b211874976c2d0913d6150a69', '283481855@qq.com', 'male', '2021-12-16 09:04:31.098268', 1);

--
-- 转储表的索引
--

--
-- 表的索引 `article_article`
--
ALTER TABLE `article_article`
  ADD PRIMARY KEY (`id`),
  ADD KEY `article_article_author_id_id_84c11256_fk_login_user_id` (`author_id_id`);

--
-- 表的索引 `article_comment`
--
ALTER TABLE `article_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `article_comment_article_id_4fa145bf_fk_article_article_id` (`article_id`),
  ADD KEY `article_comment_comment_author_id_83b96475_fk_login_user_id` (`comment_author_id`),
  ADD KEY `article_comment_pre_comment_id_a11661ba_fk_article_comment_id` (`pre_comment_id`);

--
-- 表的索引 `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 表的索引 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- 表的索引 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- 表的索引 `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- 表的索引 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- 表的索引 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- 表的索引 `captcha_captchastore`
--
ALTER TABLE `captcha_captchastore`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hashkey` (`hashkey`);

--
-- 表的索引 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- 表的索引 `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- 表的索引 `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- 表的索引 `login_confirmstring`
--
ALTER TABLE `login_confirmstring`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- 表的索引 `login_user`
--
ALTER TABLE `login_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `email` (`email`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `article_article`
--
ALTER TABLE `article_article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用表AUTO_INCREMENT `article_comment`
--
ALTER TABLE `article_comment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用表AUTO_INCREMENT `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- 使用表AUTO_INCREMENT `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `captcha_captchastore`
--
ALTER TABLE `captcha_captchastore`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- 使用表AUTO_INCREMENT `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- 使用表AUTO_INCREMENT `login_confirmstring`
--
ALTER TABLE `login_confirmstring`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `login_user`
--
ALTER TABLE `login_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 限制导出的表
--

--
-- 限制表 `article_article`
--
ALTER TABLE `article_article`
  ADD CONSTRAINT `article_article_author_id_id_84c11256_fk_login_user_id` FOREIGN KEY (`author_id_id`) REFERENCES `login_user` (`id`);

--
-- 限制表 `article_comment`
--
ALTER TABLE `article_comment`
  ADD CONSTRAINT `article_comment_article_id_4fa145bf_fk_article_article_id` FOREIGN KEY (`article_id`) REFERENCES `article_article` (`id`),
  ADD CONSTRAINT `article_comment_comment_author_id_83b96475_fk_login_user_id` FOREIGN KEY (`comment_author_id`) REFERENCES `login_user` (`id`),
  ADD CONSTRAINT `article_comment_pre_comment_id_a11661ba_fk_article_comment_id` FOREIGN KEY (`pre_comment_id`) REFERENCES `article_comment` (`id`);

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `login_confirmstring`
--
ALTER TABLE `login_confirmstring`
  ADD CONSTRAINT `login_confirmstring_user_id_3eaf7be1_fk_login_user_id` FOREIGN KEY (`user_id`) REFERENCES `login_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
