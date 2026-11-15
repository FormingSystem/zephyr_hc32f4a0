---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-6
title: zephyr__drivers__i3c__error_types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_i3c\_\_error\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.1\_枚举（Enumerations）

<a id="r_a79ba58b71019ccd9b76f65aaf4ebe1b0"></a>

```c
enum i3c_sdr_controller_error_types { I3C_ERROR_CE0 , I3C_ERROR_CE1 , I3C_ERROR_CE2 , I3C_ERROR_CE3 , I3C_ERROR_CE_UNKNOWN , I3C_ERROR_CE_NONE , I3C_ERROR_CE_MAX = I3C_ERROR_CE_UNKNOWN , I3C_ERROR_CE_INVALID }
```

相关声明：[i3c_sdr_controller_error_types](#a79ba58b71019ccd9b76f65aaf4ebe1b0)、[I3C_ERROR_CE0](#a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282)、[I3C_ERROR_CE1](#a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb)、[I3C_ERROR_CE2](#a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574)、[I3C_ERROR_CE3](#a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f)、[I3C_ERROR_CE_UNKNOWN](#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502)、[I3C_ERROR_CE_NONE](#a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707)、[I3C_ERROR_CE_MAX](#a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7)、[I3C_ERROR_CE_INVALID](#a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0)。

I3C 单数据速率（SDR）控制器错误类型（Controller Error Types）。

<a id="r_a176c3429a9a5b786639223eea9221f91"></a>

```c
enum i3c_sdr_target_error_types { I3C_ERROR_TE0 , I3C_ERROR_TE1 , I3C_ERROR_TE2 , I3C_ERROR_TE3 , I3C_ERROR_TE4 , I3C_ERROR_TE5 , I3C_ERROR_TE6 , I3C_ERROR_DBR , I3C_ERROR_TE_UNKNOWN , I3C_ERROR_TE_NONE , I3C_ERROR_TE_MAX = I3C_ERROR_TE_UNKNOWN , I3C_ERROR_TE_INVALID }
```

相关声明：[i3c_sdr_target_error_types](#a176c3429a9a5b786639223eea9221f91)、[I3C_ERROR_TE0](#a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a)、[I3C_ERROR_TE1](#a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe)、[I3C_ERROR_TE2](#a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e)、[I3C_ERROR_TE3](#a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3)、[I3C_ERROR_TE4](#a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd)、[I3C_ERROR_TE5](#a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f)、[I3C_ERROR_TE6](#a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e)、[I3C_ERROR_DBR](#a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285)、[I3C_ERROR_TE_UNKNOWN](#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791)、[I3C_ERROR_TE_NONE](#a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a)、[I3C_ERROR_TE_MAX](#a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7)、[I3C_ERROR_TE_INVALID](#a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a)。

I3C 单数据速率（SDR）目标设备错误类型（Target Error Types）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0"></a>

### `i3c_sdr_controller_error_types`

```c
enum i3c_sdr_controller_error_types
```

I3C 单数据速率（SDR）控制器错误类型（Controller Error Types）。

这些是 I3C 规范定义的错误类型（Error Types）。

`I3C_ERROR_CE_UNKNOWN` 和 `I3C_ERROR_CE_NONE` 不是规范中的正式错误类型。它们仅用于辅助与 I3C 驱动及子系统交互时的错误处理（Error Handling）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `I3C_ERROR_CE0` | 发送通用命令码（CCC）之后的事务（Transaction）。 |
| `I3C_ERROR_CE1` | 监测错误（Monitoring Error）。 |
| `I3C_ERROR_CE2` | 广播地址（Broadcast Address）`0x7E` 无响应。 |
| `I3C_ERROR_CE3` | 控制器交接失败（Failed Controller Handoff）。 |
| `I3C_ERROR_CE_UNKNOWN` | 未知错误（Unknown Error），不是正式错误类型。 |
| `I3C_ERROR_CE_NONE` | 无错误（No Error），不是正式错误类型。 |
| `I3C_ERROR_CE_MAX` |  |
| `I3C_ERROR_CE_INVALID` |  |

<a id="a176c3429a9a5b786639223eea9221f91"></a>

### `i3c_sdr_target_error_types`

```c
enum i3c_sdr_target_error_types
```

I3C 单数据速率（SDR）目标设备错误类型（Target Error Types）。

这些是 I3C 规范定义的错误类型（Error Types）。

`I3C_ERROR_TE_UNKNOWN` 和 `I3C_ERROR_TE_NONE` 不是规范中的正式错误类型。它们仅用于辅助与 I3C 驱动及子系统交互时的错误处理（Error Handling）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `I3C_ERROR_TE0` | 广播地址无效，或动态地址（DA）分配后的动态地址无效（Invalid Broadcast Address or Dynamic Address）。 |
| `I3C_ERROR_TE1` | 通用命令码类型（CCC Type）。 |
| `I3C_ERROR_TE2` | 写数据（Write Data）。 |
| `I3C_ERROR_TE3` | 动态地址仲裁（Dynamic Address Arbitration）期间分配的地址。 |
| `I3C_ERROR_TE4` | 动态地址仲裁（Dynamic Address Arbitration）期间，重复起始（RESTART）之后缺少 `0x7E/R`。 |
| `I3C_ERROR_TE5` | 检测到通用命令码（CCC）之后的事务（Transaction）。 |
| `I3C_ERROR_TE6` | 监测错误（Monitoring Error）。 |
| `I3C_ERROR_DBR` | 失效总线恢复（Dead Bus Recovery）。 |
| `I3C_ERROR_TE_UNKNOWN` | 未知错误（Unknown Error），不是正式错误类型。 |
| `I3C_ERROR_TE_NONE` | 无错误（No Error），不是正式错误类型。 |
| `I3C_ERROR_TE_MAX` |  |
| `I3C_ERROR_TE_INVALID` |  |


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P233_error_types.h_源码浏览.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7"></a>
<a id="a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0"></a>
<a id="a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a"></a>
<a id="a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe"></a>
<a id="a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e"></a>
<a id="a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3"></a>
<a id="a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd"></a>
<a id="a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f"></a>
<a id="a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e"></a>
<a id="a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285"></a>
<a id="a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791"></a>
<a id="a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a"></a>
<a id="a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7"></a>
<a id="a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a"></a>

---

[上一章](P005_zephyr__dt-bindings__sensor__icm566xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__ethernet__eth_adin2111.h_文件参考.md)
