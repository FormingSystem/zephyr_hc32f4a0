---
id: learning.zephyr-docs.api-file-reference.page-29
title: zephyr__net__canbus.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_net\_\_canbus.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/canbus_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CAN总线套接字（Bus Socket）的API定义。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/socketcan.h>
#include <zephyr/drivers/can.h>
```

查看此文件的源码。

CAN总线套接字（Bus Socket）的API定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 29.1\_数据结构（Data Structures）

<a id="r_canbus_5Fapi"></a>

```c
struct canbus_api
```

相关声明：[canbus_api](../network_service_model_reference/P001_canbus_api_结构体.md)。

CAN第二层（L2）网络驱动API。


## 29.2\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [zephyr/net/socketcan.h](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h_source.html)
- [zephyr/drivers/can.h](../can_driver_reference/P002_CAN驱动头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P008_canbus.h_源码浏览.md)
- [canbus_api](../network_service_model_reference/P001_canbus_api_结构体.md)

<a id="header-details"></a>

---

[上一章](P028_zephyr__bluetooth__mesh__keys.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__drivers__ieee802154__cc1200.h_文件参考.md)
