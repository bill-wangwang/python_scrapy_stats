# 使用说明
- 该爬虫为2016年最新的统计数据（这是本人学python以来第一次完成的练手项目，要求别太高^_^）
- 环境要求 python3 + scrapy1.4 
- 使用步骤
    - 导入下面的sql语句(注意host为localhost user为root 密码为123456)
    - 进入工作目录（cd到与scrapy.cfg所在的目录）
    - scrapy crawl area1
    - scrapy crawl area2
    - scrapy crawl area3
    - scrapy crawl area4
    - scrapy crawl area5
    - 执行到area5时需要注意改下 settings.py 中的 ITEM_PIPELINES （具体见注意事项）
    - 以上命令必须按顺序一个个执行，并且等前一个执行完成才可以执行后面的



# 建库建表sql
```

CREATE DATABASE IF NOT EXISTS `stats` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `stats`;

CREATE TABLE `2016_area` (
	`id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
	`area_id` BIGINT(10) UNSIGNED NOT NULL COMMENT '行政区域id（身份证前6位）',
	`parent_id` BIGINT(20) UNSIGNED NOT NULL COMMENT '父类id',
	`level` TINYINT(3) UNSIGNED NOT NULL COMMENT '级别（1-省份 2-城市 3-县区 4-镇 5-村委会/居委会）',
	`name` VARCHAR(50) NOT NULL COMMENT '行政区名称',
	`category_code` INT(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT '城乡分类3位代码(level=5时有效) 城镇-1xx  乡村-2xx（111-主城区 112-城乡结合区 121-镇中心区 122-镇乡结合区 123-特殊区域 210-乡中心区 220-村庄）',
	`href` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '下级链接地址',
	PRIMARY KEY (`id`),
	UNIQUE INDEX `area_id` (`area_id`),
	INDEX `parent_id` (`parent_id`),
	INDEX `level` (`level`)
)
COMMENT='2016年统计局行政区域数据'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=1;
```
温馨提示： **stats/out/stats_sql.zip** 为采集好的数据，可以直接用
# 注意事项
- 一共有5个爬虫，
- **area1** 省份爬虫
- **area2** 城市爬虫
- **area3** 区县爬虫
- **area4** 城镇爬虫
- **area5** 村委会/居委会爬虫
 
crawl **area1** **area2** **area3** **area4** 时的setting如下
```
ITEM_PIPELINES = {
   'stats.pipelines.AreaPipeline': 300,
   # 'stats.pipelines.Area5Pipeline': 100,
}
```
crawl  **area5** 时的 **setting** 如下
```
ITEM_PIPELINES = {
   # 'stats.pipelines.AreaPipeline': 300,
   'stats.pipelines.Area5Pipeline': 100,
}
```