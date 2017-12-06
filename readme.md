# sql 建表语句
```
CREATE TABLE `2016_area` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `area_id` bigint(10) unsigned NOT NULL,
 `parent_id` int(10) unsigned NOT NULL,
 `name` varchar(50) NOT NULL,
 `href` varchar(255) NOT NULL,
 PRIMARY KEY (`id`),
 UNIQUE KEY `area_id` (`area_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='2016年统计局行政区域数据'
```
