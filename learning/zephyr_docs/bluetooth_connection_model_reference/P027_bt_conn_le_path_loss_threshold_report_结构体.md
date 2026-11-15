---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-27
title: bt_conn_le_path_loss_threshold_report_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__path__loss__threshold__report.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_bt\_conn\_le\_path\_loss\_threshold\_report\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__path__loss__threshold__report.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 路径损耗监测阈值变化报告（Path Loss Monitoring Threshold Change Report）结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 路径损耗监测阈值变化报告（Path Loss Monitoring Threshold Change Report）结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_ab2b71b7ddccc40ced56657a548b98e77"></a>

```c
enum bt_conn_le_path_loss_zone zone
```

相关声明：[bt_conn_le_path_loss_zone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)、[zone](#ab2b71b7ddccc40ced56657a548b98e77)。

核心规范（Core Spec.）中定义的路径损耗区域（Path Loss zone）。

<a id="r_abe631b07816d6c18bacba64bfbd1e844"></a>

```c
uint8_t path_loss
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[path_loss](#abe631b07816d6c18bacba64bfbd1e844)。

当前路径损耗（Path loss），单位为 dB。

## 27.2\_详细说明（Detailed Documentation）

<a id="abe631b07816d6c18bacba64bfbd1e844"></a>

### `path_loss`

```c
uint8_t bt_conn_le_path_loss_threshold_report::path_loss
```

当前路径损耗（Path loss），单位为 dB。

<a id="ab2b71b7ddccc40ced56657a548b98e77"></a>

### `zone`

```c
enum bt_conn_le_path_loss_zone bt_conn_le_path_loss_threshold_report::zone
```

核心规范（Core Spec.）中定义的路径损耗区域（Path Loss zone）。

5.4 版第 4 卷 E 部分第 7.7.65.32 节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_conn_le_path_loss_zone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_bt_conn_le_path_loss_reporting_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_bt_conn_le_phy_info_结构体.md)
