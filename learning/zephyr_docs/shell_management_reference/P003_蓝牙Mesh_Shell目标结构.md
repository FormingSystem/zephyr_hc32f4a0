---
id: learning.zephyr-docs.shell-management-reference.page-3
title: 蓝牙Mesh_Shell目标结构
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__shell__target.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙Mesh\_Shell目标结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__shell__target.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙Mesh Shell、mcumgr Shell管理与SMP传输接口。源码跟踪译注与官方原文分开标示。

Mesh Shell的目标上下文（Target Context）。

```c
#include <zephyr/bluetooth/mesh/shell.h>
```

<a id="details"></a>

Mesh Shell的目标上下文（Target Context）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a48a9039d99fefb8a536c427161359485"></a>

```c
uint16_t dst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst](#a48a9039d99fefb8a536c427161359485)。

<a id="r_a2cb816bbfd493656d327cd604254fdbd"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#a2cb816bbfd493656d327cd604254fdbd)。

<a id="r_a52c511cf9843512ec6d8db7cec6f6fa1"></a>

```c
uint16_t app_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[app_idx](#a52c511cf9843512ec6d8db7cec6f6fa1)。

## 3.2\_详细说明（Detailed Documentation）

<a id="a52c511cf9843512ec6d8db7cec6f6fa1"></a>

### `app_idx`

```c
uint16_t bt_mesh_shell_target::app_idx
```

<a id="a48a9039d99fefb8a536c427161359485"></a>

### `dst`

```c
uint16_t bt_mesh_shell_target::dst
```

<a id="a2cb816bbfd493656d327cd604254fdbd"></a>

### `net_idx`

```c
uint16_t bt_mesh_shell_target::net_idx
```

## 3.3\_源码定位与版本边界

源码定位：[include/zephyr/bluetooth/mesh/shell.h](../../../include/zephyr/bluetooth/mesh/shell.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：该头文件集中声明Mesh Shell所用模型对象和当前目标上下文；extern是对其他文件所定义对象的引用，并不在此创建新的模型实例。

> 译注——源码核对：健康发布宏把最大故障数量常量4传给BT_MESH_HEALTH_PUB_DEFINE。目标结构的dst、net_idx和app_idx分别保存当前目标地址、网络索引和应用索引；字段解释来自本册源码页中保留的普通注释。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/shell.h](P002_蓝牙Mesh_Shell头文件源码.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_蓝牙Mesh_Shell头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_mcumgr_Shell管理接口.md)
