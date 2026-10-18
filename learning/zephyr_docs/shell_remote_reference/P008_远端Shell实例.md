---
id: learning.zephyr-docs.shell-remote-reference.page-8
title: 远端Shell实例
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_远端Shell实例

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

用于存储远端Shell实例配置的结构（Instance Configuration Structure）。

```c
#include <zephyr/shell/shell_remote.h>
```

<a id="details"></a>

用于存储远端Shell实例配置的结构（Instance Configuration Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_aa815345346bb54a610b8422232e78106"></a>

```c
const char * name
```

相关声明：[name](#aa815345346bb54a610b8422232e78106)。

远端Shell实例的名称，即命令语法名称（Command Syntax）。

<a id="r_abc23c07899d59c1b942a6e50b814b8b1"></a>

```c
const struct device * ipc
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[ipc](#abc23c07899d59c1b942a6e50b814b8b1)。

进程间通信设备（IPC Device）。

<a id="r_a599061c03ce6e626e57d91be5100783b"></a>

```c
struct ipc_ept_cfg ep_cfg
```

相关声明：[ipc_ept_cfg](../intercore_reference/P114_IPC服务端点配置.md)、[ep_cfg](#a599061c03ce6e626e57d91be5100783b)。

IPC端点配置（Endpoint Configuration）。

## 8.2\_详细说明（Detailed Documentation）

<a id="a599061c03ce6e626e57d91be5100783b"></a>

### `ep_cfg`

```c
struct ipc_ept_cfg shell_remote::ep_cfg
```

IPC端点配置（Endpoint Configuration）。

<a id="abc23c07899d59c1b942a6e50b814b8b1"></a>

### `ipc`

```c
const struct device* shell_remote::ipc
```

进程间通信设备（IPC Device）。

<a id="aa815345346bb54a610b8422232e78106"></a>

### `name`

```c
const char* shell_remote::name
```

远端Shell实例的名称，即命令语法名称（Command Syntax）。

## 8.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote.h](../../../include/zephyr/shell/shell_remote.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：远端Shell通过IPC端点传递命令和结果。CONN宏声明静态运行数据及可遍历段中的配置，设备通过DEVICE_DT_GET取得；宏展开本身不证明端点已绑定。ready字段原文写作bounded，这里按绑定事件（Bound Event）解释。

> 译注——源码核对：远端命令运行数据只保留两个命令槽，即当前命令和父命令。语法及帮助文本复制到固定大小临时缓冲区；现有实现对过长帮助文本作截断，并对语法长度使用断言。它不是可无限缓存整棵远端命令树的容器。

> 译注——源码核对：打印消息接收后按8字节对齐在堆上复制，再提交工作项处理；打印结束后释放副本并发送结果确认。字段注释称work为工作队列，而声明实际是struct k_work工作项，由系统工作队列执行。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 8.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_remote.h](P003_远端Shell头文件源码.md)
- [device](../device_reference/P002_设备对象结构.md)
- [ipc_ept_cfg](../intercore_reference/P114_IPC服务端点配置.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_远端Shell公共头文件源码.md) · [返回大纲](大纲.md) · [下一章](P009_远端Shell命令.md)
