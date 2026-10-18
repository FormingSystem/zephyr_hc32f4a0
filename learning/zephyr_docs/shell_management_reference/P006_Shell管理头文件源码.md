---
id: learning.zephyr-docs.shell-management-reference.page-6
title: Shell管理头文件源码
kind: reference
status: maintained
domains: [zephyr, shell, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__mgmt_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Shell管理头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__mgmt_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P005_Shell管理头文件参考.md)和[公共接口](P004_mcumgr_Shell管理接口.md)；访问语义和生命周期见本页译注。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00038"></a>
<a id="agroup__mcumgr__shell__mgmt_html_gac37bf991450de1611ae54fd671b61581"></a>
<a id="agroup__mcumgr__shell__mgmt_html_ggac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205"></a>
<a id="agroup__mcumgr__shell__mgmt_html_ggac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881"></a>
<a id="agroup__mcumgr__shell__mgmt_html_ggac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02"></a>
<a id="agroup__mcumgr__shell__mgmt_html_ggac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018-2021 mcumgr authors
<a id="l00003"></a> * Copyright (c) 2023 Nordic Semiconductor ASA
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SHELL_MGMT_SHELL_MGMT_H_
<a id="l00015"></a>#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SHELL_MGMT_SHELL_MGMT_H_
<a id="l00016"></a>
<a id="l00023"></a>
<a id="l00024"></a>#ifdef __cplusplus
<a id="l00025"></a>extern "C" {
<a id="l00026"></a>#endif
<a id="l00027"></a>
<a id="l00032"></a>#define SHELL_MGMT_ID_EXEC 0
<a id="l00034"></a>
<a id="l00038"></a>enum shell_mgmt_err_code_t {
<a id="l00040"></a>        SHELL_MGMT_ERR_OK = 0,
<a id="l00041"></a>
<a id="l00043"></a>        SHELL_MGMT_ERR_UNKNOWN,
<a id="l00044"></a>
<a id="l00046"></a>        SHELL_MGMT_ERR_COMMAND_TOO_LONG,
<a id="l00047"></a>
<a id="l00049"></a>        SHELL_MGMT_ERR_EMPTY_COMMAND,
<a id="l00050"></a>};
<a id="l00051"></a>
<a id="l00052"></a>#ifdef __cplusplus
<a id="l00053"></a>}
<a id="l00054"></a>#endif
<a id="l00055"></a>
<a id="l00059"></a>
<a id="l00060"></a>#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SHELL_MGMT_SHELL_MGMT_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018-2021 mcumgr authors；Copyright (c) 2023 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_SHELL_MGMT_SHELL_MGMT_H_头文件包含保护结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `shell_mgmt_err_code_t`

```c
shell_mgmt_err_code_t
```

Shell管理组的命令结果码（Command Result Codes）。

定义位置（Definition）：shell_mgmt.h:38。

符号定位：[shell_mgmt_err_code_t](P004_mcumgr_Shell管理接口.md#gac37bf991450de1611ae54fd671b61581)。

### `SHELL_MGMT_ERR_COMMAND_TOO_LONG`

```c
@ SHELL_MGMT_ERR_COMMAND_TOO_LONG
```

提供的待执行命令过长。

定义位置（Definition）：shell_mgmt.h:46。

符号定位：[SHELL_MGMT_ERR_COMMAND_TOO_LONG](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205)。

### `SHELL_MGMT_ERR_EMPTY_COMMAND`

```c
@ SHELL_MGMT_ERR_EMPTY_COMMAND
```

未提供待执行的命令。

定义位置（Definition）：shell_mgmt.h:49。

符号定位：[SHELL_MGMT_ERR_EMPTY_COMMAND](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881)。

### `SHELL_MGMT_ERR_UNKNOWN`

```c
@ SHELL_MGMT_ERR_UNKNOWN
```

发生未知错误（Unknown Error）。

定义位置（Definition）：shell_mgmt.h:43。

符号定位：[SHELL_MGMT_ERR_UNKNOWN](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02)。

### `SHELL_MGMT_ERR_OK`

```c
@ SHELL_MGMT_ERR_OK
```

没有错误；如果响应中没有ret值，就隐含表示此结果。

定义位置（Definition）：shell_mgmt.h:40。

符号定位：[SHELL_MGMT_ERR_OK](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51)。

## 6.4\_源码跟踪译注

> 译注——Shell管理组接收执行命令请求；通过Shell传输SMP协议则是另一层接口。本册将两者分开，不能把管理组的执行结果码当成串口收帧状态。

> 译注——当前管理实现通过虚拟后端执行命令，执行前清除缓存输出，执行后读取输出并将命令返回值写入响应。命令输出使用o字段；返回码通常为ret，启用遗留兼容配置时使用rc。

> 译注——当前实现把argv中的文本用空格连接成命令行，再交给Shell解析。列表元素边界与Shell最终参数边界不能无条件等同；需要保留空格或引号语义时应结合Shell解析规则。

头文件定位：[include/zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h](../../../include/zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h)，关联实现／接口：[subsys/mgmt/mcumgr/grp/shell_mgmt/src/shell_mgmt.c](../../../subsys/mgmt/mcumgr/grp/shell_mgmt/src/shell_mgmt.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/mgmt/mcumgr/grp/shell_mgmt/shell_mgmt.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/shell_mgmt/src/shell_mgmt.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_Shell管理头文件参考.md)
- [shell_mgmt_err_code_t](P004_mcumgr_Shell管理接口.md#gac37bf991450de1611ae54fd671b61581)
- [SHELL_MGMT_ERR_OK](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51)
- [SHELL_MGMT_ERR_UNKNOWN](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02)
- [SHELL_MGMT_ERR_COMMAND_TOO_LONG](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205)
- [SHELL_MGMT_ERR_EMPTY_COMMAND](P004_mcumgr_Shell管理接口.md#ggac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881)

---

[上一章](P005_Shell管理头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_mcumgr_Shell传输接口.md)
