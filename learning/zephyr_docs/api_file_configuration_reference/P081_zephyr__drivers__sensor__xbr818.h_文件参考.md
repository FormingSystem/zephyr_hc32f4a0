---
id: learning.zephyr-docs.api-file-configuration-reference.page-81
title: zephyr__drivers__sensor__xbr818.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xbr818_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_zephyr\_\_drivers\_\_sensor\_\_xbr818.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xbr818_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

XBR818传感器的扩展API头文件（Extended Sensor API Header）。

查看此文件的源码。

<a id="details"></a>

XBR818 传感器扩展应用程序编程接口（Extended Sensor API）的头文件。它公开用于配置该集成电路（IC）的 4 个附加属性（Additional Attributes）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 81.1\_枚举（Enumerations）

<a id="r_ga2f524848967d71fe6c7557355a064bec"></a>

```c
enum sensor_attribute_xbr818 { SENSOR_ATTR_XBR818_DELAY_TIME = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_XBR818_LOCK_TIME , SENSOR_ATTR_XBR818_NOISE_FLOOR , SENSOR_ATTR_XBR818_RF_POWER }
```

相关声明：[sensor_attribute_xbr818](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#ga2f524848967d71fe6c7557355a064bec)、[SENSOR_ATTR_XBR818_DELAY_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064becaa9f1b6389623e1f197b4e9d41ce784ed)、[SENSOR_ATTR_XBR818_LOCK_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064beca69b529d03c9898dd1dad0907ea090434)、[SENSOR_ATTR_XBR818_NOISE_FLOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064beca7fdfc87ccda9cbf8c1dc5c5b3b093467)、[SENSOR_ATTR_XBR818_RF_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064beca91dd8effcc638ecdf035ef5c051f75ad)。

XBR818 的自定义传感器属性（Custom Sensor Attributes）。


## 81.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P931_xbr818.h_源码浏览.md)
- [sensor_attribute_xbr818](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#ga2f524848967d71fe6c7557355a064bec)
- [SENSOR_ATTR_XBR818_DELAY_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064becaa9f1b6389623e1f197b4e9d41ce784ed)
- [SENSOR_ATTR_XBR818_LOCK_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064beca69b529d03c9898dd1dad0907ea090434)
- [SENSOR_ATTR_XBR818_NOISE_FLOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064beca7fdfc87ccda9cbf8c1dc5c5b3b093467)
- [SENSOR_ATTR_XBR818_RF_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__xbr818__interface.html#gga2f524848967d71fe6c7557355a064beca91dd8effcc638ecdf035ef5c051f75ad)

<a id="header-details"></a>

---

[上一章](P080_zephyr__drivers__sensor__wsen_pads_2511020213301.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P082_zephyr__mgmt__mcumgr__grp__zephyr__zephyr_basic.h_文件参考.md)
