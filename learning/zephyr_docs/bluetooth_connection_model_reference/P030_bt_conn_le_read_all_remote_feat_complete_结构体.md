---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-30
title: bt_conn_le_read_all_remote_feat_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__read__all__remote__feat__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_bt\_conn\_le\_read\_all\_remote\_feat\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__read__all__remote__feat__complete.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

读取全部远端功能（Read All Remote Features）完成回调的参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

读取全部远端功能（Read All Remote Features）完成回调的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a0dbbd0144cc6990b45d662896862cce7"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a0dbbd0144cc6990b45d662896862cce7)。

低功耗读取所有远端特性完成事件（LE Read All Remote Features Complete）的主机控制器接口状态（HCI Status）。

<a id="r_a1554bd9035619cc4dbdb2d04fd9105ad"></a>

```c
uint8_t max_remote_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_remote_page](#a1554bd9035619cc4dbdb2d04fd9105ad)。

远端设备支持的页数（Pages supported）。

<a id="r_a996e2600fd41bf1b6d95b6ee5873f6ce"></a>

```c
uint8_t max_valid_page
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_valid_page](#a996e2600fd41bf1b6d95b6ee5873f6ce)。

从远端设备获取的页数（Pages fetched）。

<a id="r_a7a8db1d0c0656e8953da8b8aa4bec2c7"></a>

```c
const uint8_t * features
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#a7a8db1d0c0656e8953da8b8aa4bec2c7)。

指向大小为 248 的数组的指针，数组中保存远端支持特性的特性位（Feature bits）。

## 30.2\_详细说明（Detailed Documentation）

<a id="a7a8db1d0c0656e8953da8b8aa4bec2c7"></a>

### `features`

```c
const uint8_t* bt_conn_le_read_all_remote_feat_complete::features
```

指向大小为 248 的数组的指针，数组中保存远端支持特性的特性位（Feature bits）。

第 0 页占 8 字节，其后的 10 页每页占 24 字节。取值参见 `BT_LE_FEAT_BIT_*`，比较取值时参见 `BT_FEAT_LE_*` 宏。另见蓝牙核心规范（Bluetooth Core Specification）第 6 卷 B 部分第 4.6 节。

<a id="a1554bd9035619cc4dbdb2d04fd9105ad"></a>

### `max_remote_page`

```c
uint8_t bt_conn_le_read_all_remote_feat_complete::max_remote_page
```

远端设备支持的页数（Pages supported）。

<a id="a996e2600fd41bf1b6d95b6ee5873f6ce"></a>

### `max_valid_page`

```c
uint8_t bt_conn_le_read_all_remote_feat_complete::max_valid_page
```

从远端设备获取的页数（Pages fetched）。

<a id="a0dbbd0144cc6990b45d662896862cce7"></a>

### `status`

```c
uint8_t bt_conn_le_read_all_remote_feat_complete::status
```

低功耗读取所有远端特性完成事件（LE Read All Remote Features Complete）的主机控制器接口状态（HCI Status）。

若 `status` 不是 `BT_HCI_ERR_SUCCESS`，则其余参数保持不变。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_HCI_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a27c890210eded48f159073cccef8582a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_bt_conn_le_phy_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_bt_conn_le_remote_info_结构体.md)
