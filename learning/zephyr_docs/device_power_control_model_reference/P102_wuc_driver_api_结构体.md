---
id: learning.zephyr-docs.device-power-control-model-reference.page-102
title: wuc_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwuc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_wuc\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwuc__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：唤醒控制器（WUC）驱动操作。

```c
#include <zephyr/drivers/wuc.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：唤醒控制器（Wakeup Controller，WUC）驱动操作。这是每个 WUC 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 102.1\_数据成员（Data Fields）

<a id="r_ab4a5c36416c1e1ccc86a784cb477fdb4"></a>

```c
wuc_api_enable_wakeup_source enable
```

相关声明：[wuc_api_enable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga94ca8c28ef9f1328ddddd3a5489204e2)、[enable](#ab4a5c36416c1e1ccc86a784cb477fdb4)。

`REQ`：启用唤醒源（Wakeup source）。

<a id="r_a8b3036c2a04f94c467688f7cd880c5ae"></a>

```c
wuc_api_disable_wakeup_source disable
```

相关声明：[wuc_api_disable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#gad36d204bead7c8ce4999858d16dca3ad)、[disable](#a8b3036c2a04f94c467688f7cd880c5ae)。

`REQ`：禁用唤醒源。

<a id="r_a0662ddbad43d57e2a0beaa8f30643721"></a>

```c
wuc_api_check_wakeup_source_triggered triggered
```

相关声明：[wuc_api_check_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga821a6abcc315fcd10e88e2f45641127e)、[triggered](#a0662ddbad43d57e2a0beaa8f30643721)。

`OPT`：检查唤醒源是否已触发。

<a id="r_ad95894cabddb42e772887ec38f0b11b7"></a>

```c
wuc_api_clear_wakeup_source_triggered clear
```

相关声明：[wuc_api_clear_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga52c4fa3a73d2f3ef392c61b6c0133f6b)、[clear](#ad95894cabddb42e772887ec38f0b11b7)。

`OPT`：清除唤醒源的已触发状态。

## 102.2\_详细说明（Detailed Documentation）

<a id="ad95894cabddb42e772887ec38f0b11b7"></a>

### `clear`

```c
wuc_api_clear_wakeup_source_triggered wuc_driver_api::clear
```

`OPT`：清除唤醒源的已触发状态。

<a id="a8b3036c2a04f94c467688f7cd880c5ae"></a>

### `disable`

```c
wuc_api_disable_wakeup_source wuc_driver_api::disable
```

`REQ`：禁用唤醒源。

<a id="ab4a5c36416c1e1ccc86a784cb477fdb4"></a>

### `enable`

```c
wuc_api_enable_wakeup_source wuc_driver_api::enable
```

`REQ`：启用唤醒源（Wakeup source）。

<a id="a0662ddbad43d57e2a0beaa8f30643721"></a>

### `triggered`

```c
wuc_api_check_wakeup_source_triggered wuc_driver_api::triggered
```

`OPT`：检查唤醒源是否已触发。

本数据类型文档由以下文件生成：

- `zephyr/drivers/wuc.h`

## 102.3\_原页交叉引用（Cross References）

- [zephyr/drivers/wuc.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h_source.html)
- [wuc_api_enable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga94ca8c28ef9f1328ddddd3a5489204e2)
- [wuc_api_disable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#gad36d204bead7c8ce4999858d16dca3ad)
- [wuc_api_check_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga821a6abcc315fcd10e88e2f45641127e)
- [wuc_api_clear_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html#ga52c4fa3a73d2f3ef392c61b6c0133f6b)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P101_usbc_vbus_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P103_wuc_dt_spec_结构体.md)
