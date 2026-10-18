---
id: learning.zephyr-docs.api-file-interface-reference.page-59
title: zephyr__drivers__sensor__tmp108.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tmp108_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_zephyr\_\_drivers\_\_sensor\_\_tmp108.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tmp108_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI TMP108温度传感器（Temperature Sensor）的扩展公共API。

查看此文件的源码。

<a id="details"></a>

TI TMP108 温度传感器的扩展公共 API。提供 TMP108 的属性，可用于设置片上温度模式（Temperature Mode）及警报参数（alert parameters）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 59.1\_枚举（Enumerations）

<a id="r_a27e0be5adff7e6b9ddee08ab329263ac"></a>

```c
enum sensor_attribute_tmp_108 { SENSOR_ATTR_TMP108_ONE_SHOT_MODE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_TMP108_SHUTDOWN_MODE , SENSOR_ATTR_TMP108_CONTINUOUS_CONVERSION_MODE , SENSOR_ATTR_TMP108_ALERT_POLARITY }
```

相关声明：[sensor_attribute_tmp_108](#a27e0be5adff7e6b9ddee08ab329263ac)、[SENSOR_ATTR_TMP108_ONE_SHOT_MODE](#a27e0be5adff7e6b9ddee08ab329263aca7d3aaeefef79d21d14b094a73859aad5)、[SENSOR_ATTR_TMP108_SHUTDOWN_MODE](#a27e0be5adff7e6b9ddee08ab329263aca77ad914dd8719431e411c521ba439f51)、[SENSOR_ATTR_TMP108_CONTINUOUS_CONVERSION_MODE](#a27e0be5adff7e6b9ddee08ab329263aca15ffb18b0a416692f198df2974695845)、[SENSOR_ATTR_TMP108_ALERT_POLARITY](#a27e0be5adff7e6b9ddee08ab329263aca7368db02e4565f72373efbcf8d671feb)。

## 59.2\_详细说明（Detailed Documentation）

<a id="a27e0be5adff7e6b9ddee08ab329263ac"></a>

### `sensor_attribute_tmp_108`

```c
enum sensor_attribute_tmp_108
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_TMP108_ONE_SHOT_MODE` | 启用省电／单次采样模式（power saving/one shot mode）。 |
| `SENSOR_ATTR_TMP108_SHUTDOWN_MODE` | 关闭传感器（Shutdown the Sensor）。 |
| `SENSOR_ATTR_TMP108_CONTINUOUS_CONVERSION_MODE` | 启用连续转换（Continuous Conversion）。 |
| `SENSOR_ATTR_TMP108_ALERT_POLARITY` | 设置警报引脚极性（alert pin polarity）。 |


## 59.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P872_tmp108.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a27e0be5adff7e6b9ddee08ab329263aca7d3aaeefef79d21d14b094a73859aad5"></a>
<a id="a27e0be5adff7e6b9ddee08ab329263aca77ad914dd8719431e411c521ba439f51"></a>
<a id="a27e0be5adff7e6b9ddee08ab329263aca15ffb18b0a416692f198df2974695845"></a>
<a id="a27e0be5adff7e6b9ddee08ab329263aca7368db02e4565f72373efbcf8d671feb"></a>

---

[上一章](P058_zephyr__bluetooth__audio__tmap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P060_zephyr__drivers__console__uart_console.h_文件参考.md)
