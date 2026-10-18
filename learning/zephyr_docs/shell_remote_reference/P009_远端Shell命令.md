---
id: learning.zephyr-docs.shell-remote-reference.page-9
title: 远端Shell命令
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_远端Shell命令

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__cmd.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

用于存储远端Shell命令数据的结构（Command Data Structure）。

```c
#include <zephyr/shell/shell_remote.h>
```

<a id="details"></a>

用于存储远端Shell命令数据的结构（Command Data Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a10d9f55e316984f5c5e1d89ce112b7ec"></a>

```c
struct shell_static_entry cmd
```

相关声明：[shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)、[cmd](#a10d9f55e316984f5c5e1d89ce112b7ec)。

命令条目（Command Entry）。

<a id="r_a7a7817a33d740d6b458338f551eb5328"></a>

```c
const struct shell_static_entry * rem_cmd
```

相关声明：[shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)、[rem_cmd](#a7a7817a33d740d6b458338f551eb5328)。

父级远端命令（Parent Remote Command）的指针。

<a id="r_a6563d0ec7c942d974802759b4f5f506f"></a>

```c
char tmp_buf [128]
```

相关声明：[tmp_buf](#a6563d0ec7c942d974802759b4f5f506f)。

用于命令语法和帮助文本的临时缓冲区（Temporary Buffer）。

## 9.2\_详细说明（Detailed Documentation）

<a id="a10d9f55e316984f5c5e1d89ce112b7ec"></a>

### `cmd`

```c
struct shell_static_entry shell_remote_cmd::cmd
```

命令条目（Command Entry）。

<a id="a7a7817a33d740d6b458338f551eb5328"></a>

### `rem_cmd`

```c
const struct shell_static_entry* shell_remote_cmd::rem_cmd
```

父级远端命令（Parent Remote Command）的指针。

<a id="a6563d0ec7c942d974802759b4f5f506f"></a>

### `tmp_buf`

```c
char shell_remote_cmd::tmp_buf[128]
```

用于命令语法和帮助文本的临时缓冲区（Temporary Buffer）。

## 9.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote.h](../../../include/zephyr/shell/shell_remote.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：远端Shell通过IPC端点传递命令和结果。CONN宏声明静态运行数据及可遍历段中的配置，设备通过DEVICE_DT_GET取得；宏展开本身不证明端点已绑定。ready字段原文写作bounded，这里按绑定事件（Bound Event）解释。

> 译注——源码核对：远端命令运行数据只保留两个命令槽，即当前命令和父命令。语法及帮助文本复制到固定大小临时缓冲区；现有实现对过长帮助文本作截断，并对语法长度使用断言。它不是可无限缓存整棵远端命令树的容器。

> 译注——源码核对：打印消息接收后按8字节对齐在堆上复制，再提交工作项处理；打印结束后释放副本并发送结果确认。字段注释称work为工作队列，而声明实际是struct k_work工作项，由系统工作队列执行。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 9.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_remote.h](P003_远端Shell头文件源码.md)
- [shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_远端Shell实例.md) · [返回大纲](大纲.md) · [下一章](P010_远端Shell运行数据.md)
