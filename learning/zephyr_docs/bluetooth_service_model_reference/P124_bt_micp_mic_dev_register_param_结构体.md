---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-124
title: bt_micp_mic_dev_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__mic__dev__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_bt\_micp\_mic\_dev\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__mic__dev__register__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

麦克风控制服务（Microphone Control Service）的注册参数结构。

```c
#include <zephyr/bluetooth/audio/micp.h>
```

<a id="details"></a>

麦克风控制服务（Microphone Control Service）的注册参数结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 124.1\_数据成员（Data Fields）

<a id="r_a8153e3e59f830a3746d3545b9262ae50"></a>

```c
struct bt_aics_register_param aics_param [0U]
```

相关声明：[bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)、[aics_param](#a8153e3e59f830a3746d3545b9262ae50)。

音频输入控制服务（Audio Input Control Services）的注册参数结构体。

<a id="r_adbb6cf96e7f1d3e48b88cd3fbc5fd71a"></a>

```c
struct bt_micp_mic_dev_cb * cb
```

相关声明：[bt_micp_mic_dev_cb](P123_bt_micp_mic_dev_cb_结构体.md)、[cb](#adbb6cf96e7f1d3e48b88cd3fbc5fd71a)。

麦克风控制规范（Microphone Control Profile）回调结构体。

## 124.2\_详细说明（Detailed Documentation）

<a id="a8153e3e59f830a3746d3545b9262ae50"></a>

### `aics_param`

```c
struct bt_aics_register_param bt_micp_mic_dev_register_param::aics_param[0U]
```

音频输入控制服务（Audio Input Control Services）的注册参数结构体。

<a id="adbb6cf96e7f1d3e48b88cd3fbc5fd71a"></a>

### `cb`

```c
struct bt_micp_mic_dev_cb* bt_micp_mic_dev_register_param::cb
```

麦克风控制规范（Microphone Control Profile）回调结构体。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/micp.h`

## 124.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/micp.h](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h_source.html)
- [bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)
- [bt_micp_mic_dev_cb](P123_bt_micp_mic_dev_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P123_bt_micp_mic_dev_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P125_bt_nus_cb_结构体.md)
