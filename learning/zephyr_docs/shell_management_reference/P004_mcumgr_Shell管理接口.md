---
id: learning.zephyr-docs.shell-management-reference.page-4
title: mcumgr_Shell管理接口
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__shell__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_mcumgr\_Shell管理接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__shell__mgmt.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙Mesh Shell、mcumgr Shell管理与SMP传输接口。源码跟踪译注与官方原文分开标示。

MCUmgr Shell管理API（Shell Management API）。

<a id="details"></a>

MCUmgr Shell管理API（Shell Management API）。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_shell_5Fmgmt_2Eh"></a>

```c
file shell_mgmt.h
```

相关声明：[shell_mgmt.h](P005_Shell管理头文件参考.md)。

MCUmgr Shell管理组API（Shell Management Group API）的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.2\_枚举（Enumerations）

<a id="r_gac37bf991450de1611ae54fd671b61581"></a>

```c
enum shell_mgmt_err_code_t { SHELL_MGMT_ERR_OK = 0 , SHELL_MGMT_ERR_UNKNOWN , SHELL_MGMT_ERR_COMMAND_TOO_LONG , SHELL_MGMT_ERR_EMPTY_COMMAND }
```

相关声明：[shell_mgmt_err_code_t](#gac37bf991450de1611ae54fd671b61581)、[SHELL_MGMT_ERR_OK](#ggac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51)、[SHELL_MGMT_ERR_UNKNOWN](#ggac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02)、[SHELL_MGMT_ERR_COMMAND_TOO_LONG](#ggac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205)、[SHELL_MGMT_ERR_EMPTY_COMMAND](#ggac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881)。

Shell管理组的命令结果码（Command Result Codes）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.3\_Shell管理组命令编号（Command IDs）

<a id="r_ga5b360507490dd79996c59bb51b0bb791"></a>

```c
#define SHELL_MGMT_ID_EXEC 0
```

相关声明：[SHELL_MGMT_ID_EXEC](#ga5b360507490dd79996c59bb51b0bb791)。

执行Shell命令行（Command Line Execute）。

## 4.4\_详细说明（Detailed Documentation）

<a id="ga5b360507490dd79996c59bb51b0bb791"></a>

### `SHELL_MGMT_ID_EXEC`

```c
#define SHELL_MGMT_ID_EXEC 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h>
```

执行Shell命令行（Command Line Execute）。

<a id="gac37bf991450de1611ae54fd671b61581"></a>

### `shell_mgmt_err_code_t`

```c
enum shell_mgmt_err_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h>
```

Shell管理组的命令结果码（Command Result Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SHELL_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `SHELL_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `SHELL_MGMT_ERR_COMMAND_TOO_LONG` | 提供的待执行命令过长。 |
| `SHELL_MGMT_ERR_EMPTY_COMMAND` | 未提供待执行的命令。 |

## 4.5\_源码定位与版本边界

源码定位：[include/zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h](../../../include/zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h)、[subsys/mgmt/mcumgr/grp/shell_mgmt/src/shell_mgmt.c](../../../subsys/mgmt/mcumgr/grp/shell_mgmt/src/shell_mgmt.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：Shell管理组接收执行命令请求；通过Shell传输SMP协议则是另一层接口。本册将两者分开，不能把管理组的执行结果码当成串口收帧状态。

> 译注——源码核对：当前管理实现通过虚拟后端执行命令，执行前清除缓存输出，执行后读取输出并将命令返回值写入响应。命令输出使用o字段；返回码通常为ret，启用遗留兼容配置时使用rc。

> 译注——源码核对：当前实现把argv中的文本用空格连接成命令行，再交给Shell解析。列表元素边界与Shell最终参数边界不能无条件等同；需要保留空格或引号语义时应结合Shell解析规则。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.6\_原页交叉引用（Cross References）

- [shell_mgmt.h](P005_Shell管理头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51"></a>
<a id="ggac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02"></a>
<a id="ggac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205"></a>
<a id="ggac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881"></a>

---

[上一章](P003_蓝牙Mesh_Shell目标结构.md) · [返回大纲](大纲.md) · [下一章](P005_Shell管理头文件参考.md)
