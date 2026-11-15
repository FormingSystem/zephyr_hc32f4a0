---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-69
title: ubx_mon_ver_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__mon__ver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_ubx\_mon\_ver\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__mon__ver.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_aa0495c27ac850d56ddaa92bc4689ba7f"></a>

```c
char sw_ver [30]
```

相关声明：[sw_ver](#aa0495c27ac850d56ddaa92bc4689ba7f)。

<a id="r_a07a2fdbe52fa48e9412f39bff1256318"></a>

```c
char hw_ver [10]
```

相关声明：[hw_ver](#a07a2fdbe52fa48e9412f39bff1256318)。

## 69.2\_详细说明（Detailed Documentation）

<a id="a07a2fdbe52fa48e9412f39bff1256318"></a>

### `hw_ver`

```c
char ubx_mon_ver::hw_ver[10]
```

<a id="aa0495c27ac850d56ddaa92bc4689ba7f"></a>

### `sw_ver`

```c
char ubx_mon_ver::sw_ver[30]
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_ubx_mon_gnss_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_ubx_nav_pvt_结构体.md)
