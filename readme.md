# 建表sql
```
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