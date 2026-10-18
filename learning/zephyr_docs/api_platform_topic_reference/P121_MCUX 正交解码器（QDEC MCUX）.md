---
id: learning.zephyr-docs.api-platform-topic-reference.page-121
title: MCUX 正交解码器（QDEC MCUX）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__qdec__mcux.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第121章\_MCUX 正交解码器（QDEC MCUX）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__qdec__mcux.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP MCUX 正交解码器（QDEC）传感器。

<a id="details"></a>

NXP MCUX 正交解码器（QDEC）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 121.1\_文件（Files）

<a id="r_qdec_5Fmcux_2Eh"></a>

```c
file qdec_mcux.h
```

相关声明：[qdec_mcux.h](../api_file_supplement_reference/P096_zephyr__drivers__sensor__qdec_mcux.h_文件参考.md)。

QDEC MCUX传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 121.2\_枚举（Enumerations）

<a id="r_ga93f4f84af3e5a42381e9152750c46286"></a>

```c
enum sensor_attribute_qdec_mcux { SENSOR_ATTR_QDEC_MOD_VAL = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_QDEC_ENABLE_SINGLE_PHASE }
```

相关声明：[sensor_attribute_qdec_mcux](#ga93f4f84af3e5a42381e9152750c46286)、[SENSOR_ATTR_QDEC_MOD_VAL](#gga93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2)、[SENSOR_ATTR_QDEC_ENABLE_SINGLE_PHASE](#gga93f4f84af3e5a42381e9152750c46286afac8fcee81dcca4ce5f5717b09a18cb4)。

QDEC MCUX 的扩展传感器属性（Extended Sensor Attributes）。

## 121.3\_详细说明（Detailed Documentation）

<a id="ga93f4f84af3e5a42381e9152750c46286"></a>

### `sensor_attribute_qdec_mcux`

```c
enum sensor_attribute_qdec_mcux
```

```c
#include <zephyr/drivers/sensor/qdec_mcux.h>
```

QDEC MCUX 的扩展传感器属性（Extended Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_QDEC_MOD_VAL` | 每转计数（Counts per revolution）。 |
| `SENSOR_ATTR_QDEC_ENABLE_SINGLE_PHASE` | 单相计数（Single Phase Counting）。 |


## 121.4\_原页交叉引用（Cross References）

- [qdec_mcux.h](../api_file_supplement_reference/P096_zephyr__drivers__sensor__qdec_mcux.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2"></a>
<a id="gga93f4f84af3e5a42381e9152750c46286afac8fcee81dcca4ce5f5717b09a18cb4"></a>

---

[上一章](P120_SDHC 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P122_SENT 驱动后端 API.md)
