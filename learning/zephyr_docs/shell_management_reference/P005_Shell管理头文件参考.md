---
id: learning.zephyr-docs.shell-management-reference.page-5
title: Shell管理头文件参考
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Shell管理头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__mgmt_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙Mesh Shell、mcumgr Shell管理与SMP传输接口。源码跟踪译注与官方原文分开标示。

MCUmgr Shell管理组API（Shell Management Group API）的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr Shell管理组API（Shell Management Group API）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### Shell管理组命令编号（Command IDs）

<a id="r_ga5b360507490dd79996c59bb51b0bb791"></a>

```c
#define SHELL_MGMT_ID_EXEC 0
```

相关声明：[SHELL_MGMT_ID_EXEC](P004_mcumgr_Shell管理接口.md#ga5b360507490dd79996c59bb51b0bb791)。

执行Shell命令行（Command Line Execute）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.2\_枚举（Enumerations）

<a id="r_gac37bf991450de1611ae54fd671b61581"></a>

```c
enum shell_mgmt_err_code_t { SHELL_MGMT_ERR_OK = 0 , SHELL_MGMT_ERR_UNKNOWN , SHELL_MGMT_ERR_COMMAND_TOO_LONG , SHELL_MGMT_ERR_EMPTY_COMMAND }
```

相关声明：[shell_mgmt_err_code_t](P004_mcumgr_Shell管理接口.md#gac37bf991450de1611ae54fd671b61581)、[SHELL_MGMT_ERR_OK](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51)、[SHELL_MGMT_ERR_UNKNOWN](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02)、[SHELL_MGMT_ERR_COMMAND_TOO_LONG](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205)、[SHELL_MGMT_ERR_EMPTY_COMMAND](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881)。

Shell管理组的命令结果码（Command Result Codes）。

## 5.3\_源码定位与版本边界

源码定位：[include/zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h](../../../include/zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h)、[subsys/mgmt/mcumgr/grp/shell_mgmt/src/shell_mgmt.c](../../../subsys/mgmt/mcumgr/grp/shell_mgmt/src/shell_mgmt.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：Shell管理组接收执行命令请求；通过Shell传输SMP协议则是另一层接口。本册将两者分开，不能把管理组的执行结果码当成串口收帧状态。

> 译注——源码核对：当前管理实现通过虚拟后端执行命令，执行前清除缓存输出，执行后读取输出并将命令返回值写入响应。命令输出使用o字段；返回码通常为ret，启用遗留兼容配置时使用rc。

> 译注——源码核对：当前实现把argv中的文本用空格连接成命令行，再交给Shell解析。列表元素边界与Shell最终参数边界不能无条件等同；需要保留空格或引号语义时应结合Shell解析规则。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [查看此文件的源码](P006_Shell管理头文件源码.md)
- [SHELL_MGMT_ID_EXEC](P004_mcumgr_Shell管理接口.md#ga5b360507490dd79996c59bb51b0bb791)
- [shell_mgmt_err_code_t](P004_mcumgr_Shell管理接口.md#gac37bf991450de1611ae54fd671b61581)
- [SHELL_MGMT_ERR_OK](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51)
- [SHELL_MGMT_ERR_UNKNOWN](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02)
- [SHELL_MGMT_ERR_COMMAND_TOO_LONG](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205)
- [SHELL_MGMT_ERR_EMPTY_COMMAND](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881)

<a id="header-details"></a>

---

[上一章](P004_mcumgr_Shell管理接口.md) · [返回大纲](大纲.md) · [下一章](P006_Shell管理头文件源码.md)
