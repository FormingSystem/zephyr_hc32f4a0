---
id: learning.zephyr-docs.api-file-reference.page-237
title: zephyr__net__net_l2.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__l2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第237章\_zephyr\_\_net\_\_net\_l2.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__l2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络第二层接口（Network L2 Interface）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/capture.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

网络第二层接口（Network L2 Interface）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 237.1\_数据结构（Data Structures）

<a id="r_net_5Fl2"></a>

```c
struct net_l2
```

相关声明：[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

网络第二层（Network L2）结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 237.2\_枚举（Enumerations）

<a id="r_gac7db0cc6c56d371a5803873074ec2516"></a>

```c
enum net_l2_flags { NET_L2_MULTICAST = BIT(0) , NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE = BIT(1) , NET_L2_PROMISC_MODE = BIT(2) , NET_L2_POINT_TO_POINT = BIT(3) }
```

相关声明：[net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)、[NET_L2_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231)、[NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1)、[NET_L2_PROMISC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8)、[NET_L2_POINT_TO_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1)。

第二层标志（L2 Flags）。


## 237.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/net/capture.h](../api_source_supplement_reference/P022_capture.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P575_net_l2.h_源码浏览.md)
- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [NET_L2_MULTICAST](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231)
- [NET_L2_MULTICAST_SKIP_JOIN_SOLICIT_NODE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1)
- [NET_L2_PROMISC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8)
- [NET_L2_POINT_TO_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1)

<a id="header-details"></a>

---

[上一章](P236_zephyr__dt-bindings__clock__mtk_mt8188_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P238_zephyr__net__net_offload.h_文件参考.md)
