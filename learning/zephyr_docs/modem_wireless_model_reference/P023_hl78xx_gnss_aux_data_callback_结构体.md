---
id: learning.zephyr-docs.modem-wireless-model-reference.page-23
title: hl78xx_gnss_aux_data_callback_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__gnss__aux__data__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_hl78xx\_gnss\_aux\_data\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__gnss__aux__data__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（GNSS）辅助数据的回调结构。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

GNSS 辅助数据回调结构体，用于注册接收 GNSS 辅助数据的回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_adcf42adad65b781ea9e5816c2f10b0db"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#adcf42adad65b781ea9e5816c2f10b0db)。

如果非 `NULL`，则将回调限定为仅接收此设备的 GNSS 数据。

<a id="r_a2037bb2cfa4c6fb4d9e84489b8e48b8a"></a>

```c
hl78xx_gnss_aux_data_callback_t callback
```

相关声明：[hl78xx_gnss_aux_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9198bafcc7c78243fc72ca2b0bc926ed)、[callback](#a2037bb2cfa4c6fb4d9e84489b8e48b8a)。

发布 GNSS 辅助数据时调用的回调。

## 23.2\_详细说明（Detailed Documentation）

<a id="a2037bb2cfa4c6fb4d9e84489b8e48b8a"></a>

### `callback`

```c
hl78xx_gnss_aux_data_callback_t hl78xx_gnss_aux_data_callback::callback
```

发布 GNSS 辅助数据时调用的回调。

<a id="adcf42adad65b781ea9e5816c2f10b0db"></a>

### `dev`

```c
const struct device* hl78xx_gnss_aux_data_callback::dev
```

如果非 `NULL`，则将回调限定为仅接收此设备的 GNSS 数据。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [hl78xx_gnss_aux_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9198bafcc7c78243fc72ca2b0bc926ed)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_hl78xx_evt_monitor_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_hl78xx_gnss_nmea_aux_data_结构体.md)
