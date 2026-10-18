---
id: learning.zephyr-docs.platform-security-model-reference.page-24
title: otp_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structotp__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_otp\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structotp__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：一次性可编程存储器（OTP）驱动操作。

```c
#include <zephyr/drivers/otp.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：一次性可编程存储器（OTP）驱动操作。这是每个 OTP 驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a5372b65914f5d9d02b7a1f9db3bcde5d"></a>

```c
otp_api_read read
```

相关声明：[otp_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#ga2dd11aba59cbe417973d98503d67b343)、[read](#a5372b65914f5d9d02b7a1f9db3bcde5d)。

必需（REQ）：从 OTP 存储器读取数据。

<a id="r_ac3bf2e91c385c713739e8be04ae0264d"></a>

```c
otp_api_program program
```

相关声明：[otp_api_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#gae4eff2ba1959c2817f684a3306427e09)、[program](#ac3bf2e91c385c713739e8be04ae0264d)。

可选（OPT）：向指定的 OTP 存储器编程写入数据。

## 24.2\_详细说明（Detailed Documentation）

<a id="ac3bf2e91c385c713739e8be04ae0264d"></a>

### `program`

```c
otp_api_program otp_driver_api::program
```

可选（OPT）：向指定的 OTP 存储器编程写入数据。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_OTP_PROGRAM`。

<a id="a5372b65914f5d9d02b7a1f9db3bcde5d"></a>

### `read`

```c
otp_api_read otp_driver_api::read
```

必需（REQ）：从 OTP 存储器读取数据。

本数据类型文档由以下文件生成：

- `zephyr/drivers/otp.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/drivers/otp.h](https://docs.zephyrproject.org/latest/doxygen/html/otp_8h_source.html)
- [otp_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#ga2dd11aba59cbe417973d98503d67b343)
- [otp_api_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#gae4eff2ba1959c2817f684a3306427e09)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)
- [CONFIG_OTP_PROGRAM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP_PROGRAM)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_nxp_rtxxx_dsp_ctrl_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_pcie_bar_结构体.md)
